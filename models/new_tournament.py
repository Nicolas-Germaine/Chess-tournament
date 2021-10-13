"""Game time"""

TIME = ("Blitz", "Bullet", "Speed")


class Tournament:
    """Information for a new tournament"""

    def __init__(self, name, place, date, comments, number_of_turns=4, tours=0, time=0):
        """Init information of tournament"""
        self.name = name
        self.place = place
        self.date = date
        self.comments = comments
        self.number_of_turns = number_of_turns
        self.tours = tours
        self.players = []
        self.time = time
