"""Fixtures specific for deciders tests
"""

import pytest

from highlights.domain.common import Player, Game, Stats


@pytest.fixture
def ref_top_scorers_decider():
    """reference data for test of TopScorersDecider"""
    return [
        Player(player_id=203081, team_id=1610612757, name='Damian Lillard',
               game=Game(game_id='0022200027',
                         home_team='Portland Trail Blazers',
                         away_team='Phoenix Suns',
                         date='2022-10-21T22:00:00-04:00'),
               stats=Stats(points=35, assists=2, rebounds=3, other=None)),
        Player(player_id=202685, team_id=1610612740,
               name='Jonas Valanciunas',
               game=Game(game_id='0022200017',
                         home_team='Charlotte Hornets',
                         away_team='New Orleans Pelicans',
                         date='2022-10-21T19:00:00Z'),
               stats=Stats(points=30, assists=4, rebounds=17, other=None)),
        Player(player_id=1630169, team_id=1610612754,
               name='Tyrese Haliburton',
               game=Game(game_id='0022200018', home_team='Indiana Pacers',
                         away_team='San Antonio Spurs',
                         date='2022-10-21T19:00:00Z'),
               stats=Stats(points=27, assists=12, rebounds=3, other=None)),
        Player(player_id=201939, team_id=1610612744, name='Stephen Curry',
               game=Game(game_id='0022200026',
                         home_team='Golden State Warriors',
                         away_team='Denver Nuggets',
                         date='2022-10-21T22:00:00-04:00'),
               stats=Stats(points=23, assists=4, rebounds=5, other=None)),
        Player(player_id=1626164, team_id=1610612756, name='Devin Booker',
               game=Game(game_id='0022200027',
                         home_team='Portland Trail Blazers',
                         away_team='Phoenix Suns',
                         date='2022-10-21T22:00:00-04:00'),
               stats=Stats(points=23, assists=3, rebounds=5, other=None)),
        Player(player_id=1626179, team_id=1610612766, name='Terry Rozier',
               game=Game(game_id='0022200017',
                         home_team='Charlotte Hornets',
                         away_team='New Orleans Pelicans',
                         date='2022-10-21T19:00:00Z'),
               stats=Stats(points=23, assists=11, rebounds=8, other=None)),
        Player(player_id=1627751, team_id=1610612759, name='Jakob Poeltl',
               game=Game(game_id='0022200018', home_team='Indiana Pacers',
                         away_team='San Antonio Spurs',
                         date='2022-10-21T19:00:00Z'),
               stats=Stats(points=21, assists=5, rebounds=8, other=None)),
        Player(player_id=203999, team_id=1610612743, name='Nikola Jokic',
               game=Game(game_id='0022200026',
                         home_team='Golden State Warriors',
                         away_team='Denver Nuggets',
                         date='2022-10-21T22:00:00-04:00'),
               stats=Stats(points=19, assists=7, rebounds=10, other=None))
    ]
