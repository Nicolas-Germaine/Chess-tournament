import datetime
from  player import Player

"""Game time"""

TIME = ("Blitz", "Bullet", "Speed")


class Tournament:
    """Information for a new tournament"""

    def __init__(self, name, place, date, rounds=4):
        """Init information of tournament"""
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
