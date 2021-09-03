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