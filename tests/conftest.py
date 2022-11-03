""" Common fixtures for tests
"""

import pytest


@pytest.fixture
def live_scoreboard_games():
    return [
        {'awayTeam': {'inBonus': '0',
                      'losses': 1,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 40},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 30},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 28},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 5}],
                      'score': 103,
                      'seed': None,
                      'teamCity': 'Denver',
                      'teamId': 1610612743,
                      'teamName': 'Nuggets',
                      'teamTricode': 'DEN',
                      'timeoutsRemaining': 3,
                      'wins': 0},
         'gameClock': 'PT09M18.00S',
         'gameCode': '20221021/DENGSW',
         'gameEt': '2022-10-21T22:00:00-04:00',
         'gameId': '0022200026',
         'gameLeaders': {'awayLeaders': {'assists': 7,
                                         'jerseyNum': '15',
                                         'name': 'Nikola Jokic',
                                         'personId': 203999,
                                         'playerSlug': 'nikola-jokic',
                                         'points': 19,
                                         'position': 'C',
                                         'rebounds': 10,
                                         'teamTricode': 'DEN'},
                         'homeLeaders': {'assists': 4,
                                         'jerseyNum': '30',
                                         'name': 'Stephen Curry',
                                         'personId': 201939,
                                         'playerSlug': 'stephen-curry',
                                         'points': 23,
                                         'position': 'G',
                                         'rebounds': 5,
                                         'teamTricode': 'GSW'}},
         'gameStatus': 2,
         'gameStatusText': 'Q4 09:18',
         'gameTimeUTC': '2022-10-22T02:00:00Z',
         'homeTeam': {'inBonus': '0',
                      'losses': 0,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 34},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 18},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 36},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 5}],
                      'score': 93,
                      'seed': None,
                      'teamCity': 'Golden State',
                      'teamId': 1610612744,
                      'teamName': 'Warriors',
                      'teamTricode': 'GSW',
                      'timeoutsRemaining': 4,
                      'wins': 1},
         'ifNecessary': False,
         'pbOdds': {'odds': 0.0, 'suspended': 0, 'team': None},
         'period': 4,
         'regulationPeriods': 4,
         'seriesGameNumber': '',
         'seriesText': ''},
        {'awayTeam': {'inBonus': '0',
                      'losses': 0,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 28},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 25},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 26},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 9}],
                      'score': 88,
                      'seed': None,
                      'teamCity': 'Phoenix',
                      'teamId': 1610612756,
                      'teamName': 'Suns',
                      'teamTricode': 'PHX',
                      'timeoutsRemaining': 4,
                      'wins': 1},
         'gameClock': 'PT06M58.00S',
         'gameCode': '20221021/PHXPOR',
         'gameEt': '2022-10-21T22:00:00-04:00',
         'gameId': '0022200027',
         'gameLeaders': {'awayLeaders': {'assists': 3,
                                         'jerseyNum': '1',
                                         'name': 'Devin Booker',
                                         'personId': 1626164,
                                         'playerSlug': 'devin-booker',
                                         'points': 23,
                                         'position': 'G',
                                         'rebounds': 5,
                                         'teamTricode': 'PHX'},
                         'homeLeaders': {'assists': 2,
                                         'jerseyNum': '0',
                                         'name': 'Damian Lillard',
                                         'personId': 203081,
                                         'playerSlug': 'damian-lillard',
                                         'points': 35,
                                         'position': 'G',
                                         'rebounds': 3,
                                         'teamTricode': 'POR'}},
         'gameStatus': 2,
         'gameStatusText': 'Q4 06:58',
         'gameTimeUTC': '2022-10-22T02:00:00Z',
         'homeTeam': {'inBonus': '1',
                      'losses': 0,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 25},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 22},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 28},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 14}],
                      'score': 89,
                      'seed': None,
                      'teamCity': 'Portland',
                      'teamId': 1610612757,
                      'teamName': 'Trail Blazers',
                      'teamTricode': 'POR',
                      'timeoutsRemaining': 3,
                      'wins': 1},
         'ifNecessary': False,
         'pbOdds': {'odds': 0.0, 'suspended': 0, 'team': None},
         'period': 4,
         'regulationPeriods': 4,
         'seriesGameNumber': '',
         'seriesText': ''},
        {'awayTeam': {'inBonus': None,
                      'losses': 0,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 35},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 26},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 32},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 31}],
                      'score': 124,
                      'seed': None,
                      'teamCity': 'New Orleans',
                      'teamId': 1610612740,
                      'teamName': 'Pelicans',
                      'teamTricode': 'NOP',
                      'timeoutsRemaining': 0,
                      'wins': 2},
         'gameClock': '',
         'gameCode': '20221021/NOPCHA',
         'gameEt': '2022-10-21T19:00:00Z',
         'gameId': '0022200017',
         'gameLeaders': {'awayLeaders': {'assists': 4,
                                         'jerseyNum': '17',
                                         'name': 'Jonas Valanciunas',
                                         'personId': 202685,
                                         'playerSlug': None,
                                         'points': 30,
                                         'position': 'C',
                                         'rebounds': 17,
                                         'teamTricode': 'NOP'},
                         'homeLeaders': {'assists': 11,
                                         'jerseyNum': '3',
                                         'name': 'Terry Rozier',
                                         'personId': 1626179,
                                         'playerSlug': None,
                                         'points': 23,
                                         'position': 'G',
                                         'rebounds': 8,
                                         'teamTricode': 'CHA'}},
         'gameStatus': 3,
         'gameStatusText': 'Final',
         'gameTimeUTC': '2022-10-21T23:00:00Z',
         'homeTeam': {'inBonus': None,
                      'losses': 1,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 24},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 27},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 34},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 27}],
                      'score': 112,
                      'seed': None,
                      'teamCity': 'Charlotte',
                      'teamId': 1610612766,
                      'teamName': 'Hornets',
                      'teamTricode': 'CHA',
                      'timeoutsRemaining': 0,
                      'wins': 1},
         'ifNecessary': False,
         'pbOdds': {'odds': 0.0, 'suspended': 0, 'team': None},
         'period': 4,
         'regulationPeriods': 4,
         'seriesGameNumber': '',
         'seriesText': ''},
        {'awayTeam': {'inBonus': None,
                      'losses': 1,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 36},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 34},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 32},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 35}],
                      'score': 137,
                      'seed': None,
                      'teamCity': 'San Antonio',
                      'teamId': 1610612759,
                      'teamName': 'Spurs',
                      'teamTricode': 'SAS',
                      'timeoutsRemaining': 0,
                      'wins': 1},
         'gameClock': '',
         'gameCode': '20221021/SASIND',
         'gameEt': '2022-10-21T19:00:00Z',
         'gameId': '0022200018',
         'gameLeaders': {'awayLeaders': {'assists': 5,
                                         'jerseyNum': '25',
                                         'name': 'Jakob Poeltl',
                                         'personId': 1627751,
                                         'playerSlug': None,
                                         'points': 21,
                                         'position': 'C',
                                         'rebounds': 8,
                                         'teamTricode': 'SAS'},
                         'homeLeaders': {'assists': 12,
                                         'jerseyNum': '0',
                                         'name': 'Tyrese Haliburton',
                                         'personId': 1630169,
                                         'playerSlug': None,
                                         'points': 27,
                                         'position': 'G',
                                         'rebounds': 3,
                                         'teamTricode': 'IND'}},
         'gameStatus': 3,
         'gameStatusText': 'Final',
         'gameTimeUTC': '2022-10-21T23:00:00Z',
         'homeTeam': {'inBonus': None,
                      'losses': 2,
                      'periods': [{'period': 1, 'periodType': 'REGULAR',
                                   'score': 26},
                                  {'period': 2, 'periodType': 'REGULAR',
                                   'score': 29},
                                  {'period': 3, 'periodType': 'REGULAR',
                                   'score': 30},
                                  {'period': 4, 'periodType': 'REGULAR',
                                   'score': 49}],
                      'score': 134,
                      'seed': None,
                      'teamCity': 'Indiana',
                      'teamId': 1610612754,
                      'teamName': 'Pacers',
                      'teamTricode': 'IND',
                      'timeoutsRemaining': 0,
                      'wins': 0},
         'ifNecessary': False,
         'pbOdds': {'odds': 0.0, 'suspended': 0, 'team': None},
         'period': 4,
         'regulationPeriods': 4,
         'seriesGameNumber': '',
         'seriesText': ''}
    ]
