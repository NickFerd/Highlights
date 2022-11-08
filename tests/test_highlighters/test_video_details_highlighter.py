"""Tests of VideoDetailsHighlighter
"""
from dataclasses import dataclass
from unittest.mock import patch

from highlights.domain.common import Player, Game, Stats
from highlights.domain.highlighters.video_details_highlighter \
    import VideoDetailsHighlighter

from loguru import logger


@dataclass
class FakeConfig:
    SLEEP_BETWEEN_NBA_API_SECONDS: int = 0


# patch external dependencies
@patch('highlights.domain.highlighters.video_details_highlighter.VideoDetails')
@patch(
    'highlights.domain.highlighters.video_details_highlighter.VideoEventsAsset'
)
def test_video_details_highlighter(mock_nba_videoeventsasset,
                                   mock_nba_videodetails,
                                   video_details_response,
                                   video_events_assets_response,
                                   links_ref):
    """test business logic of highlighter
    """
    # replace real calls to external api
    api_video_details = mock_nba_videodetails.return_value
    api_video_details.get_dict.return_value = video_details_response

    api_video_events_assets = mock_nba_videoeventsasset.return_value
    api_video_events_assets.get_dict.return_value = video_events_assets_response

    # we need to pass valid PLayer type object
    # contents does not matter as we mock calls to api
    player = Player(player_id=203081,
                    team_id=1610612757,
                    name='Damian Lillard',
                    game=Game(game_id='0022200027',
                              home_team='Portland Trail Blazers',
                              away_team='Phoenix Suns',
                              date='2022-10-21T22:00:00-04:00'),
                    stats=Stats(points=35, assists=2, rebounds=3,
                                other=None))

    highlighter = VideoDetailsHighlighter(logger=logger,
                                          highlighter_config=FakeConfig())
    res = highlighter.execute(player=player)

    assert res == links_ref
