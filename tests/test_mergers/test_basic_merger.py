"""tests for BasicMerger"""

import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Union
from unittest.mock import patch
from uuid import UUID

from loguru import logger

from highlights.domain.mergers.basic_merger import BasicMerger
from tests.conftest import only_manual


@dataclass
class FakeConfig:
    ROOT_ASSETS_FOLDER: Union[str, Path] = ''
    DELETE_ASSETS: bool = False
    RETRY_ON_ERROR = 3


@only_manual
@patch.object(uuid, 'uuid4',
              return_value=UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8'))
def test_basic_merger(fake_uuid, tmp_path, links_input):
    """Functional test for BasicMerger
    !Perform real operations of download and merge!
    (that is quite time consuming)
    """
    config = FakeConfig(ROOT_ASSETS_FOLDER=tmp_path)
    merger = BasicMerger(logger=logger, merger_config=config)
    video_path = merger.execute(links=links_input)

    # assert created file has this path
    ref = tmp_path / Path("final") / Path(
        "6ba7b810-9dad-11d1-80b4-00c04fd430c8_final.mp4")
    assert video_path == str(ref)

    # assert there are still clips in assets folder
    assets_folder = tmp_path / Path("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    assert len(list(assets_folder.iterdir())) == len(links_input)
