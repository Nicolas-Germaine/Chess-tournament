"""Base view."""


class View:
    """Player game view."""

    def menu(self):
        """prompt for main menu"""
        new_tournament = input("Nouveau tournoi ? : ")
        load_tournament = input("Charger un tournoi ? : ")
        add_players = input("Ajouter des joueurs ? : ")
        load_players =("Charger une liste de joeurs ? : ")

    def information_player(self):
        """Prompt for a name."""
        first_name = input("Tapez le prénom : ")
        last_name = input("Tapez le nom de famille : ")
        date_of_birth = input("Tapez la date de naissance (ex 12/02/1987) : ")
        gender = input("Sexe ? (H/F) : ")
        ranking = input("Son rang ? : ")
