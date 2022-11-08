"""Highlighter that uses VideoDetails NBA API endpoint to get highlights ids
"""

import time
from typing import List

from nba_api.stats.endpoints.videodetails import VideoDetails
from nba_api.stats.endpoints.videoeventsasset import VideoEventsAsset

from highlights.domain.common import Player, Link
from highlights.exceptions import ImproperConfiguration, InvalidLink, Abort


class VideoDetailsHighlighter:
    """Highlighter for creating list of links for download
    using VideoDetails endpoint"""

    def __init__(self, logger, highlighter_config):
        self.logger = logger
        self.config = highlighter_config

    def execute(self, player: Player) -> List[Link]:
        self.logger.info(f"Started {self.__class__.__name__} with input: "
                         f"{player}")
        if not isinstance(player, Player):
            raise ImproperConfiguration(f"{self.__class__.__name__} "
                                        f"was passed wrong input: "
                                        f"{player.__class__.__name__}. "
                                        f"This class is intended to work "
                                        f"with input of "
                                        f"type <{Player}>")

        links = []
        for play in self._get_raw_data(player_info=player):
            link = self._get_link(highlight_id=play['ei'],
                                  highlight_description=play['dsc'],
                                  game_id=player.game_id)
            links.append(link)
            time.sleep(self.config.SLEEP_BETWEEN_NBA_API_SECONDS)

        # sort links by highlight_id (just in case)
        links.sort(key=lambda x: x.highlight_id)
        return links

    def _get_raw_data(self, player_info: Player) -> List[dict]:
        """get raw data from nba api provider - video_details endpoint
        """
        try:
            video_details_for_player = VideoDetails(
                player_id=player_info.player_id,
                team_id=player_info.team_id,
                game_id_nullable=player_info.game_id
            ).get_dict()
            return video_details_for_player['resultSets']['playlist']
        except Exception as err:  # todo narrow exceptions
            self.logger.critical(f"Error in VideoDetails highlighter:\n{err}")
            raise Abort(f"Failed to get video details, error:\n{err}")

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
            # we choose best video asset quality
            url = links[0]['lurl']
            if not url.endswith('.mp4'):
                raise InvalidLink(f"Invalid url for download: {url}")
            return Link(highlight_id=highlight_id, url=url,
                        description=highlight_description)
        except (InvalidLink, IndexError) as err:
            self.logger.error(f"Problem with body of "
                              f"VideoEventAsset endpoint:\n"
                              f"{err}\n,"
                              f"Context:game_id={game_id}, "
                              f"highlight_id={highlight_id}")
            raise
        except Exception as err:  # todo try to narrow the exception
            self.logger.error(f"Problem with connection to "
                              f"VideoEventAsset endpoint:\n"
                              f"{err}\n,"
                              f"Context:game_id={game_id}, "
                              f"highlight_id={highlight_id}")
            raise

