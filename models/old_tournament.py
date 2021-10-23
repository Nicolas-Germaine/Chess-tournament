#from ..controllers.controllers import MakePairPlayer
from tinydb import TinyDB,Query,where

db = TinyDB("./Chess-tournament/db.json")
tournament_table = db.table('tournament_table')
player_table = db.table('player_table')

class Tournament:

    def list_of_tournament(self):

        contents = [item['name'] for item in db.table('tournament_table').all()]
        print(f"Liste des tournois dispo >>> {contents}")
        choice = input("Entrez le Nom du tournoi... >>> ")
        # tournament.append(choice)

        # if tournament == ['1']:
        #     contents = [item['prenom'] for item in db.table('player_table').all()]
        #     print(f'Les players sont >>> {contents}')
        # else:
        #     print('Oops...')
        table_tournament = db.table('tournament_table')
        tournament = table_tournament.search(Query().name == choice)
        # print(tournament[0]['players'])
        print(f"les joueurs sont {tournament[0]['players']} ")
        for item in tournament[0]['players']:
            print(item.first_name)






