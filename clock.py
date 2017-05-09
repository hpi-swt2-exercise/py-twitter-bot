"""Regularly tweet"""

# Allow running functions periodically
# http://apscheduler.readthedocs.io/en/3.3.1/
from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_bot import setup, tweet, INTERVAL_MINUTES
import sys

account = setup()

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=INTERVAL_MINUTES)
def regular_tweet():
    tweet(account)

try:
    print('Info: {name} running.'.format(name=sys.argv[0]))
    print('Info: Will tweet every {min} minutes and reply to tweets. Stop with Ctrl+c'.format(min=INTERVAL_MINUTES))
    scheduler.start()
# a KeyboardInterrupt exception is generated when the user presses Ctrl+c
except KeyboardInterrupt:
    print('\nInfo: Shutting down. Bye!')