from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('db.json')
list_player = db.table('8 players')
nb = 0

while nb < 2:
    list_player.insert({'first_name': input("Tapez le prénom >> ")})
    list_player.insert({'last_name': input("Tapez le nom de famille >> ")})
    list_player.insert({'date_of_birth': input("Tapez la date de naissance (ex 12/02/1987) >> ")})
    list_player.insert({'gender': input("Sexe ? (H/F) >> ")})
    list_player.insert({'ranking': input("Son rang ? >> ")})
    nb += 1


pprint(list_player.all())
