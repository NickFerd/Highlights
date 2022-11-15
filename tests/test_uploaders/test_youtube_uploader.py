"""Test for youtube basic uploader
"""
from dataclasses import dataclass
from pathlib import Path

from highlights.domain.common import VideoMetaInfo
from highlights.domain.uploaders.youtube_uploader import Uploader
from tests.conftest import only_manual
from loguru import logger


@dataclass
class FakeConfig:
    PRODUCTION = False
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    CLIENT_SECRETS_FILE = 'client_secret_708589580477-7b621070akh81uhtc2maoqa6v28aki0t.apps.googleusercontent.com.json'
    CRED_FILE = 'token_youtube_v3.pickle'


@only_manual
def test_youtube_uploader():
    """Functional test of uploader
    Real upload.
    """
    meta = VideoMetaInfo(title='NBA Highlights',
                         description='#nba #highlights #nbadviser \n'
                                     'latest nba games highlights')
    uploader = Uploader(logger=logger, uploader_config=FakeConfig())
    uploader.execute(video_path=Path("0022200003_1631094_final.mp4"),
                     meta_info=meta)
