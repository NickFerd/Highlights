"""Highlighter that uses VideoDetails NBA API endpoint to get highlights ids
"""

import time
from typing import List

from nba_api.stats.endpoints.videodetails import VideoDetails
from nba_api.stats.endpoints.videoeventsasset import VideoEventsAsset
from nba_api.stats.library.parameters import ContextMeasureDetailed, ClutchTime
from pydantic import BaseModel

from highlights.domain.common import Player, Link
from highlights.exceptions import ImproperConfiguration, InvalidLink, Abort


class VideoDetailsHighlighter:
    """Highlighter for creating list of links for download
    using VideoDetails endpoint"""

    class Config(BaseModel):
        """config class"""
        sleep_between_nba_api_seconds: int = 1

    def __init__(self, logger, highlighter_config: Config = Config()):
        self.logger = logger
        self.config = highlighter_config

    def execute(self, player: Player) -> List[Link]:
        self.logger.info(f"Start {self.__class__.__name__} with input: "
                         f"{player}")
        if not isinstance(player, Player):
            msg = f"{self.__class__.__name__} " \
                  f"was passed wrong input: " \
                  f"{player.__class__.__name__}. " \
                  f"This class is intended to work " \
                  f"with input of " \
                  f"type <{Player}>"
            self.logger.error(msg)
            raise ImproperConfiguration(msg)

        links = []
        for play in self._make_list_of_plays(player_info=player):
            try:
                link = self._get_link(highlight_id=play['ei'],
                                      highlight_description=play['dsc'],
                                      game_id=player.game_id)
                links.append(link)
            except InvalidLink as err:
                self.logger.error(f'Skipping play due to error: {err},'
                                  f'Highlight: {play}')

            time.sleep(self.config.sleep_between_nba_api_seconds)

        # sort links by highlight_id (just in case)
        links.sort(key=lambda x: x.highlight_id)
        return links

    def _make_list_of_plays(self, player_info: Player) -> List[dict]:
        """get list of clips info for the video
        """
        common_kwargs = dict(game_id_nullable=player_info.game_id,
                             player_id=player_info.player_id,
                             team_id=player_info.team_id)
        try:
            plays = []
            # Contents:
            # All game:
            # points no free throws, steals, blocks, assists for the dunk
            # Clutch (last 4 minutes)
            # todo think how to add 4 quarter last minutes if was overtime
            # all free_throws, missed shots, assists - no dunks, turnovers
            # ------
            # All game moments
            all_points = self._extract_playlist(**common_kwargs)
            all_points_no_free_throws = [play for play in all_points
                                         if "Free" not in play["dsc"]]
            time.sleep(.6)

            steals = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.stl,
                **common_kwargs
            )
            time.sleep(.6)
            blocks = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.blk,
                **common_kwargs
            )
            time.sleep(.6)
            all_assists = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.ast,
                **common_kwargs
            )
            dunk_assists = [play for play in all_assists
                            if "Dunk" in play["dsc"]]
            time.sleep(.6)

            # Clutch moments
            clutch_free_throws = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.fta,
                clutch_time_nullable=ClutchTime.last_4_minutes,
                **common_kwargs
            )
            time.sleep(.6)
            clutch_assists = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.ast,
                clutch_time_nullable=ClutchTime.last_4_minutes,
                **common_kwargs
            )
            clutch_assists_no_dunks = [play for play in clutch_assists
                                       if "Dunk" not in play["dsc"]]
            time.sleep(.6)

            clutch_all_shots = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.fga,
                clutch_time_nullable=ClutchTime.last_4_minutes,
                **common_kwargs
            )
            clutch_missed_shots = [play for play in clutch_all_shots
                                   if "MISS" in play["dsc"]]
            time.sleep(.6)

            clutch_turnovers = self._extract_playlist(
                context_measure_detailed=ContextMeasureDetailed.tov,
                clutch_time_nullable=ClutchTime.last_4_minutes,
                **common_kwargs
            )
            time.sleep(.6)

            plays = all_points_no_free_throws + dunk_assists + \
                    blocks + steals + \
                    clutch_free_throws + \
                    clutch_assists_no_dunks + \
                    clutch_missed_shots + \
                    clutch_turnovers

            self.logger.debug(plays)
            return sorted(plays, key=lambda play: play["ei"])
        except Exception as err:
            self.logger.critical(f"Error in VideoDetails highlighter: {err}")
            raise Abort(f"Failed to get video details, error: {err}")

    @staticmethod
    def _extract_playlist(**kwargs):
        """Make request to the VideoDetails endpoint and extract 'playlist'
        part of the answer
        """
        return VideoDetails(**kwargs).get_dict()["resultSets"]["playlist"]

    def _get_link(self, highlight_id: int, highlight_description: str,
                  game_id: str) -> Link:
        """get link and check it is valid from nba api
        """
        try:
            video_data = VideoEventsAsset(
                game_id=game_id,
                game_event_id=highlight_id
            ).get_dict()
            links = video_data['resultSets']['Meta']['videoUrls']
            self.logger.debug(links)
            # we choose best video asset quality
            url = links[0]['lurl']
            if url is None or not url.endswith('.mp4'):
                raise InvalidLink(f"Invalid url for download: {url}")
            return Link(highlight_id=highlight_id, url=url,
                        description=highlight_description)
        except (InvalidLink, IndexError, AttributeError) as err:
            self.logger.error(f"Problem with body of "
                              f"VideoEventAsset endpoint: {err}, "
                              f"Context:game_id={game_id}, "
                              f"highlight_id={highlight_id}")
            raise
        except Exception as err:  # todo try to narrow the exception
            self.logger.error(f"Problem with connection to "
                              f"VideoEventAsset endpoint: {err},"
                              f"Context:game_id={game_id}, "
                              f"highlight_id={highlight_id}")
            raise
