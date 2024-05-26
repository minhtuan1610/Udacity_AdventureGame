import random
import time


def print_sleep(message, waitTime):
    print(message)
    time.sleep(waitTime)


def introduction():
    print_sleep(
        "You find yourself standing in an open field, filled with grass and yellow wildflowers.",
        2,
    )
    print_sleep("")
