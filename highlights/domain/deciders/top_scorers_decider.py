"""Decider class, implements logic of choosing players to make videos about.
Main logic - return top performers from every game of the day,
sorted by points descending"""

from typing import List
from datetime import date

from nba_api.live.nba.endpoints import scoreboard as live_scoreboard

from highlights.domain.common import Game, Player, Stats, Team
from nba_api.stats.static import teams as static_teams


class TopScorersDecider:
    """Chooses top scorers from game day.
    Intended to be run in a script once a day when all games are finished.
    """

    def __init__(self, logger):
        self.logger = logger

    def execute(self) -> List[Player]:
        """Execute business logic behind decider
        """
        self.logger.info(f"Start {self.__class__.__name__}")
        raw_data = self._get_raw_data()
        leader_players = []
        for game_info in raw_data:
            game = Game(
                game_id=game_info['gameId'],
                home_team=self._extract_team(game_info['homeTeam']),
                away_team=self._extract_team(game_info['awayTeam']),
                date=self._extract_game_date(game_info['gameCode']),
                status=game_info["gameStatus"]
            )

            for leader_info in game_info['gameLeaders'].values():
                leader_players.append(self._extract_player(leader_info, game))

        # Sort by points scored, descending
        leader_players.sort(key=lambda x: x.stats.points, reverse=True)
        self.logger.debug(leader_players)
        return leader_players

    @staticmethod
    def _get_raw_data():
        """Get data for processing
        """
        return live_scoreboard.ScoreBoard().games.get_dict()

    @staticmethod
    def _extract_team(team_info: dict):
        """extract team name from raw data"""
        return Team(team_id=team_info["teamId"],
                    full_name=f"{team_info['teamCity']} "
                              f"{team_info['teamName']}",
                    tricode=team_info["teamTricode"])

    @staticmethod
    def _extract_game_date(game_code: str):
        """Convert to valid datetime date object
        Game code is a string, example: '20221021/SASIND'"""
        return date(year=int(game_code[:4]), month=int(game_code[4:6]),
                    day=int(game_code[6:8]))

    @staticmethod
    def _extract_player(player_info: dict, game_instance: Game):
        """extract info about a player"""
        team = static_teams.find_team_by_abbreviation(
            player_info['teamTricode']
        )
        return Player(
            player_id=player_info['personId'],
            team_id=team['id'],
            name=player_info['name'],
            game=game_instance,
            stats=Stats(points=player_info['points'],
                        assists=player_info['assists'],
                        rebounds=player_info['rebounds'])
        )
