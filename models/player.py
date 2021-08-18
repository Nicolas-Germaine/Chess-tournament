"""Player."""

from typing import List


class Player:
    """Players info."""

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name()        # Prénom
        self.last_name = last_name()          # Nom de famille
        self.date_of_birth = date_of_birth()  # Date de naissance
        self.gender = gender()                # Sexe
        self.ranking = ranking()              # Classement
