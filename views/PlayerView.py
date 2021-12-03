import datetime
from ..models.player import NewPlayers
from tinydb import TinyDB, Query,where
import json

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

        while nb < 4:

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
            info = NewPlayers(first_name, last_name, date_of_birth, gender, int(ranking))
            new_player.append(info)
            nb += 1
        new_player = sorted(new_player)
        self.list_of_tournament(new_player)

        return new_player

    def list_of_tournament(self, new_player):
        
        list_tournament = []
        # new_player = self.information_player()
        new_player = new_player
        list_players = [x.first_name for x in new_player]
        print("new_player====", new_player)
        contents = [item['name'] for item in db.table('tournament_table').all()]
        print(f"Liste des tournois dispo >>> {contents}")
        contents.append(list_tournament)

        choice = str(input("Rentrez le nom du tournoi >>> "))

        table_tournament = db.table('tournament_table')
        # table_tournament.update({'players': new_player},Query().name==choice)
        resultat = table_tournament.update_multiple([({'players': list_players}, where("name") == choice)])
        print(resultat)

