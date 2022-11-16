"""Test for youtube basic uploader
"""
from unittest.mock import MagicMock

import pytest
from loguru import logger

from highlights.domain.common import VideoMetaInfo
from highlights.domain.uploaders.youtube_uploader import Uploader
from highlights.exceptions import NotAutomated
from tests.conftest import only_manual


@only_manual
def test_youtube_uploader():
    """Functional test of uploader
    Real upload.
    """
    meta = VideoMetaInfo(title='NBA Highlights',
                         description='#nba #highlights #nbadviser \n'
                                     'latest nba games highlights')
    config = Uploader.Config(
        production=False,
        cred_file="token_youtube_v3.pickle",
        client_secrets_file="client_secret_708589580477"
                            "-7b621070akh81uhtc2maoqa6v28aki0t.apps.googleusercontent.com.json"
    )
    uploader = Uploader(logger=logger, uploader_config=config)
    uploader.execute(video_path="0022200003_1631094_final.mp4",
                     meta_info=meta)


def test_obtain_credentials_prod_raises():
    """test that obtain_credentials function raises error
    """
    config = Uploader.Config(production=True, cred_file="fake.pickle")
    uploader = Uploader(logger=MagicMock(), uploader_config=config)

    with pytest.raises(NotAutomated):
        uploader._obtain_credentials()
