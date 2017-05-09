"""Helper functions"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

def parse_tweet_time_stamp(tweet):
    """Parse twitter time stamp into a Python datetime object"""
    # The API returns times in the format "created_at": "Mon Sep 03 13:24:14 +0000 2012"
    # https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline
    return datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')

def tweet_minutes_ago(tweet):
    """Return how many minutes ago (from now) a tweet was sent"""
    tweet_time = parse_tweet_time_stamp(tweet)
    now = datetime.utcnow()
    seconds_ago = (now - tweet_time).total_seconds()
    minutes = seconds_ago / 60.0
    return minutes
