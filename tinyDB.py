from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('db.json')
fruits = db.table('8 players')

fruits.insert({'first_name': input("Tapez le prénom >>")})
fruits.insert({'last_name': input("Tapez le nom de famille >> ")})
fruits.insert({'date_of_birth': input("Tapez la date de naissance (ex 12/02/1987) >> ")})
fruits.insert({'gender': input("Sexe ? (H/F) >> ")})
fruits.insert({'ranking': input("Son rang ? >> ")})


pprint(fruits.all())

"""from tinydb import TinyDB, Query, where
from pprint import pprint

db = TinyDB('db.json')

class PlayerView:
    """Player game view."""

    def information_player(self):
        """User view information for player creation."""
        list_player = db.table('8 players')
        nb = 0

        while nb < 4:
            list_player.insert({'first_name': input("Tapez le prénom >> ")})
            list_player.insert({'last_name': input("Tapez le nom de famille >> ")})
            list_player.insert({'date_of_birth': input("Tapez la date de naissance (ex 12/02/1987) >> ")})
            list_player.insert({'gender': input("Sexe ? (H/F) >> ")})
            list_player.insert({'ranking': input("Son rang ? >> ")})
            nb += 1

        return list_player"""
