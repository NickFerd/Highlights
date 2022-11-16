"""Tests for common data structures and functions
"""
import datetime

import pytest
from highlights.domain.common import Player, Game, Team, Stats


def _players():
    """List of players"""
    return [
        Player(player_id=203081, team_id=1610612757, name='Damian Lillard',
               game=Game(game_id='0022200027',
                         home_team=Team(team_id=1610612757,
                                        full_name='Portland Trail Blazers',
                                        tricode='POR'),
                         away_team=Team(team_id=1610612756,
                                        full_name='Phoenix Suns',
                                        tricode='PHX'),
                         date=datetime.date(2022, 10, 21),
                         status=2),
               stats=Stats(points=35, assists=5, rebounds=5, other=None)),
        Player(player_id=202685, team_id=1610612740,
               name='Jonas Valanciunas',
               game=Game(game_id='0022200017',
                         home_team=Team(team_id=1610612766,
                                        full_name='Charlotte Hornets',
                                        tricode='CHA'),
                         away_team=Team(team_id=1610612740,
                                        full_name='New Orleans Pelicans',
                                        tricode='NOP'),
                         date=datetime.date(2022, 10, 21),
                         status=3),
               stats=Stats(points=30, assists=1, rebounds=17, other=None)),
        Player(player_id=1630169, team_id=1610612754,
               name='Tyrese Haliburton',
               game=Game(game_id='0022200018',
                         home_team=Team(team_id=1610612754,
                                        full_name='Indiana Pacers',
                                        tricode='IND'),
                         away_team=Team(team_id=1610612759,
                                        full_name='San Antonio Spurs',
                                        tricode='SAS'),
                         date=datetime.date(2022, 10, 21),
                         status=3),
               stats=Stats(points=27, assists=12, rebounds=5, other=None)),
        Player(player_id=201939, team_id=1610612744, name='Stephen Curry',
               game=Game(game_id='0022200026',
                         home_team=Team(team_id=1610612744,
                                        full_name='Golden State Warriors',
                                        tricode='GSW'),
                         away_team=Team(team_id=1610612743,
                                        full_name='Denver Nuggets',
                                        tricode='DEN'),
                         date=datetime.date(2022, 10, 21),
                         status=2),
               stats=Stats(points=23, assists=6, rebounds=6, other=None))]


def _stats():
    """List of stats representations, used in pair with _players() function"""
    return [
        '35 pts',
        '30 pts 17 rebs',
        '27 pts 12 asts',
        '23 pts 6 asts 6 rebs'
    ]


@pytest.mark.parametrize('player, stats_repr',
                         list(zip(_players(), _stats())))
def test_player_get_stats(player, stats_repr):
    """unit test for function get_stats of player object"""
    assert player.get_stats(min_include=6) == stats_repr


def test_player_game_date(_player):
    """test for proper date conversion
    """
    assert _player.game_date == "Oct 21"
