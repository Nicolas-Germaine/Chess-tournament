"""Game time"""

TIME = ("Blitz", "Bullet", "Speed")


class Tournament:
    """Information for a new tournament"""

    def __init__(self, name, place, date):
        """Init information of tournament"""
        self.name = name
        self.place = place
        self.date = date
