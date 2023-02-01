"""Class to use in manual script.
Provided with player's name, the class gets all needed info for creating
Player object instance of his performance from current game day if he played.
"""

from typing import Optional

from nba_api.stats.static import players
from nba_api.live.nba.endpoints import boxscore as live_boxscore

from highlights.domain.common import Game, Player, Stats
from highlights.domain.deciders.top_scorers_decider import Helper


class PlayerAdapter(Helper):
    """Class for creating Player instance
    It is responsible for searching for player in team rosters of provided
    game and fetching his stats
    """

    def make_player(self, game_id: str,
                    full_name: str = None, player_id: Optional[int] = None):
        """Entry point
        """
        # player_name and player_id mutually exclusive
        if player_id is not None and full_name is not None:
            raise RuntimeError("Parameters player_id and player_name "
                               "are mutually exclusive. "
                               "Provide only one parameter!")

        if player_id is None:
            # search by full name
            player = players.find_players_by_full_name(full_name)
            if len(player) > 1:
                raise RuntimeError(f"Found more than 1 players with provided "
                                   f"name: {player}. Provide player ID")
            player_id = player[0]["id"]

        return self._create_player_instance(game_id, player_id)

    def _create_player_instance(self, game_id: str, player_id: int):
        """fetch from api list of today's games
        """
        game_data_raw = live_boxscore.BoxScore(game_id=game_id)
        home = game_data_raw.home_team.get_dict()
        away = game_data_raw.away_team.get_dict()
        game = game_data_raw.game.get_dict()

        game_instance = self._extract_game(game)
        for team in [home, away]:
            for one_player in team["players"]:
                if one_player["personId"] == player_id:
                    stats = one_player["statistics"]
                    return Player(player_id=player_id,
                                  team_id=team["teamId"],
                                  name=one_player["name"],
                                  game=game_instance,
                                  stats=Stats(
                                      points=stats["points"],
                                      assists=stats["assists"],
                                      rebounds=stats["reboundsTotal"]
                                  ))


if __name__ == '__main__':
    player = PlayerAdapter().make_player(game_id='0022200756',
                                         full_name="Paolo Banchero")
    print(player)
