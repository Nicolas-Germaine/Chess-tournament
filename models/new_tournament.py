"""from  player import Player"""

"""Game time"""

TIME = ("Blitz", "Bullet", "Speed")


class Tournament:
    """Information for a new tournament"""

    def __init__(self, name, place, date, players=None):
        """Init information of tournament"""
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.rounds = 4
        self._entries = {}
        self._entries = name, place, date

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]

    def __repr__(self):
        return f"Tournament({self.name}, {self.place}, {self.date})"

    def __str__(self):
        return str(self.name, self.place, self.date)


if __name__ == "__main__":
    menu = Tournament
    menu.add("Nicolas", "paris", "12/02/1987")
    menu.add("Axel", "toulouse", "21/08/09")
    menu.add("Leslie", "paris", "je sais pas")
    print(menu._entries)


"""fonction make pair players"""
