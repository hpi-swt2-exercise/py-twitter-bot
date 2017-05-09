"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone
from requests import get

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
    # Some more ideas: https://www.programmableweb.com/category/humor/api
    data = get('https://api.chucknorris.io/jokes/random').json()
    joke = data['value']
    return joke[0:139]


