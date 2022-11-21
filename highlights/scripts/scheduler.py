"""Schedule module for executing scripts

Used instead of cron
"""

from apscheduler.schedulers.blocking import BlockingScheduler

from highlights.scripts.decider_basic_flow_highlights import create_highlights

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # configure jobs
    # scheduler.add_job(create_highlights, trigger="cron", hour="8")
    scheduler.add_job(create_highlights,
                      trigger="cron", minute="*/3", hour="17", max_instances=1)

    scheduler.start()
