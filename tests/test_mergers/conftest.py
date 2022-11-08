"""Fixtures for mergers tests
"""

import pytest

from highlights.domain.common import Link


@pytest.fixture
def links_input():
    return [
        Link(highlight_id=254,
             url="https://videos.nba.com/nba/pbp/media/2022/10/19/0022200014"
                 "/55/d3180cb6-a894-07d7-e975-89406f942194_1280x720.mp4",
             description="Leonard 16' Fadeaway Jumper (2 PTS)"),
        Link(highlight_id=259,
             url="https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009"
                 "/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4",
             description="Leonard 15' Fadeaway Jumper (4 PTS)"),
    ]
