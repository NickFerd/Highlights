"""Script to make video highlights for particular player"""
import datetime

from loguru import logger
from nba_api.stats.static import players

from highlights.config import BasicFlowConfig
from highlights.domain.common import Player, Game, Team, Stats
from highlights.domain.flow_managers.basic_flow import BasicFlow
from highlights.exceptions import Abort


@logger.catch
def create_highlights(player: Player):
    """Script for creating video highlights for a certain player.
    Intended to be called manually
    """
    config = BasicFlowConfig()

    logger.add(config.log.filename,
               level=config.log.level,
               rotation=config.log.rotation)

    flow = BasicFlow(config=config, logger=logger)

    try:
        flow.run(player=player)
    except Abort:
        logger.error(f"Failed flow with input: {player}")
    except Exception as err:
        logger.critical(f"Unexpected error happened: {err}")


if __name__ == '__main__':
    _player = players.find_players_by_full_name('klay thompson')
    player = Player(player_id=_player[0]['id'],
                    team_id=1610612744,
                    name='Klay Thompson',
                    game=Game(game_id='0022200245',
                              home_team=Team(team_id=1610612745,
                                             full_name='Houston Rockets',
                                             tricode='HOU'),
                              away_team=Team(team_id=1610612744,
                                             full_name='Golden State Warriors',
                                             tricode='GSW'),
                              date=datetime.date(2022, 11, 20), status=3),
                    stats=Stats(points=41, assists=3, rebounds=4, other=None))
    create_highlights(player=player)
