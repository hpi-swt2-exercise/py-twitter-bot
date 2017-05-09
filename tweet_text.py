"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "hi" in message.lower():
        berlin_time = datetime.now(timezone('Europe/Berlin'))
        date = berlin_time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
        return "Hi @" + user + "! " + date
    return None

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (140 chars max)
    berlin_time = datetime.now(timezone('Europe/Berlin'))
    text = berlin_time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    return text
