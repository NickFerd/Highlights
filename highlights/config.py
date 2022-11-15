"""Project configurations models
"""

from pydantic import BaseSettings, BaseModel

from highlights.domain.highlighters.video_details_highlighter import \
    VideoDetailsHighlighter
from highlights.domain.mergers.basic_merger import BasicMerger
from highlights.domain.uploaders.youtube_uploader import Uploader


class LogConfig(BaseModel):
    """variables for configuring logging"""
    filename: str = '/var/log/highlights/log.txt'
    rotation: str = '1 week'
    level: str = 'INFO'


class BasicFlowConfig(BaseSettings):
    """Configuration for BasicFlow workflow"""
    log: LogConfig = LogConfig()
    highlighter: VideoDetailsHighlighter.Config = \
        VideoDetailsHighlighter.Config()
    merger: BasicMerger.Config = BasicMerger.Config()
    uploader: Uploader.Config = Uploader.Config()

    class Config:
        env_nested_delimiter = '__'
