"""Schedule module for executing scripts

Used instead of cron
"""

from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler

from highlights.config import LogConfig
from highlights.scripts.decider_basic_flow_highlights import create_highlights

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    log_config = LogConfig()
    logger.add(log_config.filename,
               level=log_config.level,
               rotation=log_config.rotation)

    # configure jobs
    scheduler.add_job(create_highlights, args=[logger],
                      trigger="cron", hour="9", minute="0", max_instances=1)

    scheduler.start()
