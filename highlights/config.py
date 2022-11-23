"""Project configurations models
"""

from pydantic import BaseSettings, BaseModel

from highlights.domain.highlighters.video_details_highlighter import \
    VideoDetailsHighlighter
from highlights.domain.mergers.basic_merger import BasicMerger
from highlights.domain.uploaders.youtube_uploader import Uploader

DEFAULT_DESCRIPTION = "#nba #nbahighlights\n" \
                      "Most impressive performances of the game day - " \
                      "NBAdviser Highlights"


class LogConfig(BaseModel):
    """variables for configuring logging"""
    filename: str = '/var/log/highlights/log.txt'
    rotation: str = '1 week'
    level: str = 'INFO'


class BasicFlowConfig(BaseSettings):
    """Configuration for BasicFlow workflow"""
    highlighter: VideoDetailsHighlighter.Config = \
        VideoDetailsHighlighter.Config()
    merger: BasicMerger.Config = BasicMerger.Config()
    uploader: Uploader.Config = Uploader.Config()
    min_value_stats = 6  # from what value include in title (stats related)
    max_number_videos = 4  # number of videos to make
    video_description = DEFAULT_DESCRIPTION

    class Config:
        env_nested_delimiter = '__'
