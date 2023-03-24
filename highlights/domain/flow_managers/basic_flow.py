"""Basic Flow class
"""
import os

from highlights.config import BasicFlowConfig
from highlights.domain.common import Player, VideoMetaInfo
from highlights.domain.highlighters.video_details_highlighter import \
    VideoDetailsHighlighter
from highlights.domain.mergers.basic_merger import BasicMerger
from highlights.domain.uploaders.youtube_uploader import Uploader


class BasicFlow:
    """Manages overall program flow

    Simple synchronous implementation, no saving result of work into DB
    !Static usage of pre-defined components (highlighter, merger, uploader)!"""

    def __init__(self, logger, config: BasicFlowConfig):
        self.logger = logger
        self.config = config

    def run(self, player, **kwargs):
        """Main entry point into flow
        """
        self.logger.info(f"Start {self.__class__.__name__}")
        # initialization of components (static)
        highlighter = VideoDetailsHighlighter(
            logger=self.logger, highlighter_config=self.config.highlighter
        )
        merger = BasicMerger(
            logger=self.logger, merger_config=self.config.merger
        )
        uploader = Uploader(logger=self.logger,
                            uploader_config=self.config.uploader)

        # run flow
        links = highlighter.execute(player=player)
        path_to_video = merger.execute(links=links)
        uploader.execute(video_path=path_to_video,
                         meta_info=self._create_meta_info(player=player))
        # delete created video if no exception occurred
        os.remove(path_to_video)

    def _create_meta_info(self, player: Player):
        """Create object with meta data of video
        """
        return VideoMetaInfo(title=self._create_title(player=player),
                             description=self.config.video_description)

    def _create_title(self, player: Player):
        """Create title of the video
        """
        return f"{player.name} Highlights (" \
               f"{player.get_stats(min_include=self.config.min_value_stats)}" \
               f") | {player.game_date} | {player.teams_playing_tricodes}"
