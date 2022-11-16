"""Unit tests for deciders
"""
import datetime
from unittest.mock import patch, MagicMock

from highlights.domain.deciders.top_scorers_decider import TopScorersDecider


def test_top_scorers_deciders(live_scoreboard_games, ref_top_scorers_decider):
    """test business logic of decider
    """
    with patch.object(TopScorersDecider, '_get_raw_data',
                      return_value=live_scoreboard_games):
        decider = TopScorersDecider(logger=MagicMock())
        res = decider.execute()
        assert res == ref_top_scorers_decider


def test_extract_time_top_scorers_decider():
    """test function that converts dates
    """
    input_game_code = '20221021/SASIND'
    ref = datetime.date(2022, 10, 21)

    decider = TopScorersDecider(logger=MagicMock())
    assert decider._extract_game_date(game_code=input_game_code) == ref
