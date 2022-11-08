"""Fixtures for tests of highlighters
"""

import pytest

from highlights.domain.common import Link


@pytest.fixture
def links_ref():
    return [
        Link(highlight_id=254,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009'
                 '/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description="Leonard 16' Fadeaway Jumper (2 PTS)"),
        Link(highlight_id=259,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009'
                 '/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description="Leonard 15' Fadeaway Jumper (4 PTS)"),
        Link(highlight_id=386,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009'
                 '/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description='Leonard Free Throw 2 of 2 (5 PTS)'),
        Link(highlight_id=410,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009'
                 '/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description="Leonard 1' Reverse Layup (7 PTS) (Jackson 3 AST)"),
        Link(highlight_id=445,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009'
                 '/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description="Leonard 27' 3PT Jump Shot (10 PTS) (Wall 2 AST)"),
        Link(highlight_id=643,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009'
                 '/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description="Leonard 5' Turnaround Bank Hook Shot (12 PTS)"),
        Link(highlight_id=693,
             url='https://videos.nba.com/nba/pbp/media/2022/10/19/0022200009/783/34ebc6be-9491-9a8c-d75d-ede24d605475_1280x720.mp4',
             description="Leonard 21' Jump Shot (14 PTS) (George 4 AST)")
    ]
