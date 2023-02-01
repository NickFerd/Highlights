"""Script to make video highlights for particular player"""
import datetime

from loguru import logger
from nba_api.stats.static import players

from highlights.config import BasicFlowConfig, LogConfig
from highlights.domain.common import Player, Game, Team, Stats
from highlights.domain.deciders.player_adapter import PlayerAdapter
from highlights.domain.flow_managers.basic_flow import BasicFlow
from highlights.exceptions import Abort


def create_highlights(_player: Player, _logger):
    """Script for creating video highlights for a certain player.
    Intended to be called manually
    """
    config = BasicFlowConfig()

    flow = BasicFlow(config=config, logger=logger)

    try:
        flow.run(player=_player)
    except Abort:
        logger.error(f"Failed flow with input: {_player}")
    except Exception as err:
        logger.critical(f"Unexpected error happened: {err}")


if __name__ == '__main__':
    log_config = LogConfig()
    logger.add(log_config.filename,
               level=log_config.level,
               rotation=log_config.rotation)

    player = PlayerAdapter().make_player(game_id='0022200768',
                                         full_name="Nikola Jokic")
    create_highlights(_player=player, _logger=logger)
