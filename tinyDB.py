from tinydb import TinyDB, Query, where

db = TinyDB('db.json')

class NewPlayers:
    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

class PlayerView:
    """Player game view."""

    def information_player(self):
        """User view information for player creation."""
        list_player = []
        nb = 0

        while nb < 4:

            first_name = input("Tapez le prénom >> ")
            last_name = input("Tapez le nom de famille >> ")
            date_of_birth = input("Tapez la date de naissance (ex 12/02/1987) >> ")
            gender = input("Sexe ? (H/F) >> ")
            ranking = input("Son rang ? >> ")
            players = NewPlayers(first_name, last_name, date_of_birth, gender, ranking)
            list_player.append(players)
            nb += 1

        return list_player


print(PlayerView.information_player(self=None))

