from tinydb import TinyDB
from ..models.player import NewPlayers
db = TinyDB('db.json')

"""Base view."""

class Data_base:

    player1 = NewPlayers(first_name=input("Tapez le prénom >> "),
                 last_name=input("Tapez le nom de famille >> "),
                 date_of_birth=input("Tapez la date de naissance (ex 12/02/1987) >> "),
                 gender=input("Sexe ? (H/F) >> "),
                 ranking=input("Son rang ? >> "))

    serialized_player1 = {
            'first_name': player1.first_name,
            'last_name': player1.last_name,
            'date_of_birth': player1.date_of_birth,
            'gender': player1.gender,
            'ranking': player1.ranking
            }
    db.insert(serialized_player1)
    print(serialized_player1)

