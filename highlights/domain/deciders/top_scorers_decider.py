"""Decider class, implements logic of choosing players to make videos about.
Main logic - return top performers from every game of the day,
sorted by points descending"""

from typing import List

from nba_api.live.nba.endpoints import scoreboard as live_scoreboard

from highlights.domain.common import Game, Player, Stats
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
        self.logger.info("Start <TopScorersDecider>")
        raw_data = self._get_raw_data()
        leader_players = []
        for game_info in raw_data:
            game = Game(
                game_id=game_info['gameId'],
                home_team=self._extract_team_name(game_info['homeTeam']),
                away_team=self._extract_team_name(game_info['awayTeam']),
                date=game_info['gameEt']  # todo refactor field
            )

            for leader_info in game_info['gameLeaders'].values():
                leader_players.append(self._extract_player(leader_info, game))

        # Sort by points scored
        leader_players.sort(key=lambda x: x.stats.points, reverse=True)
        return leader_players

    @staticmethod
    def _get_raw_data():
        """Get data for processing
        """
        return live_scoreboard.ScoreBoard().games.get_dict()

    @staticmethod
    def _extract_team_name(team_info: dict):
        """extract team name from raw data"""
        return f"{team_info['teamCity']} {team_info['teamName']}"

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
