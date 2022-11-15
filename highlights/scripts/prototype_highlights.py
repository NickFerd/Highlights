"""Script to make video highlights."""

from loguru import logger

from highlights.config import BasicFlowConfig
from highlights.domain.deciders.top_scorers_decider import TopScorersDecider
from highlights.domain.flow_managers.basic_flow import BasicFlow


@logger.catch
def create_highlights():
    """Script for creating video highlights.
    Intended to be called by cron or manually
    """
    config = BasicFlowConfig()

    logger.add(config.log.filename,
               level=config.log.level,
               rotation=config.log.rotation)

    flow = BasicFlow(config=config, logger=logger)

    # run decider component
    decider = TopScorersDecider(logger=logger)
    players = decider.execute()
    for player in players:
        flow.run(player=player)


if __name__ == '__main__':
    create_highlights()
