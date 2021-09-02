"""from  ..views.NewTournamentView import NewTournamentView"""

"""Game time"""

TIME = ("Blitz", "Bullet", "Speed")


class Tournament:
    """Information for a new tournament"""

    def __init__(self, name, place, date):
        """Init information of tournament"""
        self.name = name
        self.place = place
        self.date = date

"""class Menu:
    def __init__(self):
        self._entries = {}

    def add(self, name, place, date):

        self._entries = Tournament(name, place, date)

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]

    def __repr__(self):
        return f"Tournament({self.name}, {self.place}, {self.date})"

    def __str__(self):
        return str(self.name, self.place, self.date)"""


"""fonction make pair players"""
