"""Script to make video highlights for particular player"""

from loguru import logger

from highlights.config import BasicFlowConfig, LogConfig
from highlights.domain.common import Player
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


def setup(player_name: str, game_id: str):
    """Entry point
    """
    log_config = LogConfig()
    logger.add(log_config.filename,
               level=log_config.level,
               rotation=log_config.rotation)

    player = PlayerAdapter().make_player(game_id=game_id,
                                         full_name=player_name)
    create_highlights(_player=player, _logger=logger)


if __name__ == '__main__':
    _game_id = '1111111'
    _player_name = 'Butler'
    setup(player_name=_player_name, game_id=_game_id)
