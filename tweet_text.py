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
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (140 chars max)
    berlin_time = datetime.now(timezone('Europe/Berlin'))
    float i = random.random()
    if i < 0.1:
        text = berlin_time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    elif i < 0.2:
        text = "git gud"
    elif i < 0.3:
        text = "DROP TABLE GOOD_TEXTS;"
    elif i < 0.4:
        text = "x"
    elif i < 0.5:
        text = "Das elektrische Feld beschreibt einen Raumzustand um eine Punktladung Q"
    elif i < 0.6:
        text = "The mitochondria is the powerhouse of the cell."
    elif i < 0.7:
        text = "*insert creative text*"
    else:
      # Some more ideas: https://www.programmableweb.com/category/humor/api
      data = get('https://api.chucknorris.io/jokes/random').json()
      joke = data['value']
      text = joke[0:139]
    return text
