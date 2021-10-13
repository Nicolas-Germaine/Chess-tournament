"""Game time"""

TIME = ("Blitz", "Bullet", "Speed")


class Tournament:
    """Information for a new tournament"""

    def __init__(self, name, place, date, number_of_turns=4, tours, players, time, comments):
        """Init information of tournament"""
        self.name = name
        self.place = place
        self.date = date
        self.number_of_turns = number_of_turns
        self.tours = tours
        self.players = players
        self.time = time
        self.comments = comments
