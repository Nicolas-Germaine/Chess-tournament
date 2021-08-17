import datetime
from tinydb import TinyDB, Query

db = TinyDB('db.json')
"""Base player."""


class Player:
    """Players info."""

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name()        # Prénom
        self.last_name = last_name()          # Nom de famille
        self.date_of_birth = date_of_birth()  # Date de naissance
        self.gender = gender()                # Sexe
        self.ranking = ranking()              # Classement

"""serialized_player = {
    'Prénom': Player.first_name, 
    'Nom de famille': Player.last_name,
    'Date de naissance': Player.date_of_birth,
    'Sexe': Player.gender,
    'Classement': Player.ranking
}"""



first_name = input('Prénom ? ')
last_name = input('Nom de famille ? ')
"""date_of_birth = input('Date de naissance ? ')"""
gender = input('Sexe ? (M/F) ')
ranking = input('Classement ? ')