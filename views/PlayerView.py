import datetime
from ..models.player import NewPlayers
from tinydb import TinyDB

"""Base view."""

db = TinyDB("./Chess-tournament/db.json")
tournament_table = db.table('tournament_table')

class PlayerView:

    def info_menu(self):
        print()
        print(">>>>> Vous allez devoir ajouter les informations pour 8 joueurs. <<<<<")
        print()

    def information_player(self):
        """"""
        new_player = []
        nb = 0

        while nb < 8:

            first_name = input("Tapez le prénom >> ")
            last_name = input("Tapez le nom de famille >> ")
            while True:
                try:
                    date_of_birth = input("Tapez la date de naissance (ex ->    00/00/0000) >> ")
                    date = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Oops!  Le format n'est pas valide.  Try again...")
            gender = input("Sexe ? (H/F) >> ")
            while True:
                try:
                    ranking = int(input("Son rang ? (ex ->  11) >> "))
                    break
                except ValueError:
                    print("Oops!  Le format n'est pas valide.  Try again...")
            info = NewPlayers(first_name,last_name,date_of_birth,gender,int(ranking))
            new_player.append(info)
            nb += 1
        new_player = sorted(new_player)

        return new_player

    def list_of_tournament(self):

        list_tournament = []
        tournament = []
        contents = [item['name'] for item in db.table('tournament_table').all()]
        #print(f"Liste des tournois dispo >>> {contents}")
        contents.append(list_tournament)

        choice = input("Entrez 1 pour lier les joueurs au premier tournoi, 2 pour le second, etc... >>> ")
        tournament.append(choice)

        if tournament == ['1']:
            contents = [item['prenom'] for item in db.table('player_table').all()]
            print(f'Les players sont >>> {contents}')
        else:
            print('Oops...')

