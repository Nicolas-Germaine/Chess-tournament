from ..models.new_tournament import Tournament

class NewTournamentView:

    def info_menu(self):
        print()
        print(">>>>> Vous allez devoir ajouter les informations pour un nouveau tournoi. <<<<<")
        print()

    def information_tournament(self):
        """"""
        new_tournament = []

        name = input("Nom du tournoi >> ")
        place = input("Lieu >> ")
        date = input("date (ex 12/02/1987) >> ")
        print()
        print(">>>>> Il va y avoir 4 rounds, et il vous faut charger une liste de 8 joueurs. <<<<<")
        print()
        tournament = Tournament(name, place, date)
        new_tournament.append(tournament)

        return new_tournament
