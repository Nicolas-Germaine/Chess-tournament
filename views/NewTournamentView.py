from ..models.new_tournament import Tournament
import datetime

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
        while True:
            try:
                date_day_str = input("date (ex ->   00/00/0000) >> ")
                date = datetime.datetime.strptime(date_day_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Oops!  Le format n'est pas valide.  Try again...")
        print()
        print(">>>>> Il va y avoir 4 rounds, et il vous faut charger une liste de 8 joueurs. <<<<<")
        print()
        new_tournament.extend([name, place, date_day_str])

        return new_tournament
