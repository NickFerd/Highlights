"""Unit tests for deciders
"""
from unittest.mock import patch, MagicMock

from highlights.domain.deciders.top_scorers_decider import TopScorersDecider


def test_top_scorers_deciders(live_scoreboard_games, ref_top_scorers_decider):
    """test business logic of decider
    """
    with patch.object(TopScorersDecider, '_get_raw_data',
                      return_value=live_scoreboard_games):
        decider = TopScorersDecider(logger=MagicMock(),
                                    decider_config=MagicMock())
        res = decider.execute()
        assert res == ref_top_scorers_decider
