"""Script to make video highlights."""

from loguru import logger

from highlights.config import BasicFlowConfig, LogConfig
from highlights.domain.deciders.top_scorers_decider import TopScorersDecider
from highlights.domain.flow_managers.basic_flow import BasicFlow
from highlights.exceptions import Abort


def create_highlights(_logger):
    """Script for creating video highlights.
    Intended to be called by cron or manually
    """
    config = BasicFlowConfig()

    flow = BasicFlow(config=config, logger=logger)

    # run decider component
    decider = TopScorersDecider(logger=logger)
    players = decider.execute()
    for player in players[:config.max_number_videos]:
        try:
            flow.run(player=player)
        except Abort:
            logger.error(f"Failed flow with input: {player}")
        except Exception as err:
            logger.critical(f"Unexpected error happened: {err}")


if __name__ == '__main__':
    log_config = LogConfig()
    logger.add(log_config.filename,
               level=log_config.level,
               rotation=log_config.rotation)
    create_highlights(_logger=logger)
