"""Script to make video highlights for particular player"""
import datetime

from loguru import logger
from nba_api.stats.static import players

from highlights.config import BasicFlowConfig, LogConfig
from highlights.domain.common import Player, Game, Team, Stats
from highlights.domain.flow_managers.basic_flow import BasicFlow
from highlights.exceptions import Abort


def create_highlights(_player: Player, _logger):
    """Script for creating video highlights for a certain player.
    Intended to be called manually
    """
    config = BasicFlowConfig()

    flow = BasicFlow(config=config, logger=logger)

    try:
        flow.run(player=player)
    except Abort:
        logger.error(f"Failed flow with input: {player}")
    except Exception as err:
        logger.critical(f"Unexpected error happened: {err}")


if __name__ == '__main__':
    # _player = players.find_players_by_full_name('klay thompson')
    player = Player(player_id=1628368,
                    team_id=1610612758,
                    name=
                    "De'Aaron Fox",
                    game=Game(game_id=
                              '0022200257',
                              home_team=Team(team_id=1610612763,
                                             full_name=
                                             'Memphis Grizzlies',
                                             tricode=
                                             'MEM'
                                             ),
                              away_team=Team(team_id=1610612758,
                                             full_name=
                                             'Sacramento Kings',
                                             tricode=
                                             'SAC'
                                             ),
                              date=datetime.date(2022,
                                                 11,
                                                 22),
                              status=3),
                    stats=Stats(points=32,
                                assists=6,
                                rebounds=8,
                                other=None))
    log_config = LogConfig()
    logger.add(log_config.filename,
               level=log_config.level,
               rotation=log_config.rotation)
    create_highlights(_player=player, _logger=logger)
