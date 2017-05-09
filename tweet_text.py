"""Construct messages to be sent as tweet text"""

# Allows using time related functions
import time

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "hi" in message.lower():
        return "Hi @" + user + "! " + time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    return None

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (140 chars max)
    text = time.strftime("It is %H:%M:%S on a %A (%d-%m-%Y).")
    return text
