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

    def information_player(self):

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

# Création d'une classe pour tinyDB, je n'arrive pas à écrire ds le fichier.json même si le code semble ok
"""
class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


db = TinyDB('db.json')
player_table = db.table('player')

player1 = Player(first_name=input("Tapez le prénom >> "), last_name=input("Tapez le nom de famille >> "))
player2 = Player(first_name='Axel', last_name='Germaine')

serialized_player1 = {
    'first_name': player1.first_name,
    'last_name': player1.last_name
}

serialized_player2 = {
    'first_name': player2.first_name,
    'last_name': player2.last_name
}

first_name = serialized_player1['first_name']
last_name = serialized_player1['last_name']
player_1 = Player(first_name=first_name, last_name=last_name)

first_name = serialized_player2['first_name']
last_name = serialized_player2['last_name']
player_2 = Player(first_name=first_name, last_name=last_name)


print(serialized_player1)
print(serialized_player2)
"""
