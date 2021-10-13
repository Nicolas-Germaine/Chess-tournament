from ..controllers.controllers import MakePairPlayer
from tinydb import TinyDB

db = TinyDB("./Chess-tournament/db.json")
tournament_table = db.table('tournament_table')
player_table = db.table('player_table')

class Tournament:

    def list_of_tournament(self):

        tournament = []
        contents = [item['name'] for item in db.table('tournament_table').all()]
        print(f"Liste des tournois dispo >>> {contents}")
        choice = input("Entrez 1 pour le premier tournoi, 2 pour le second... >>> ")
        tournament.append(choice)

        if tournament == ['1']:
            contents = [item['prenom'] for item in db.table('player_table').all()]
            print(f'Les players sont >>> {contents}')
        else:
            print('Oops...')
            return MakePairPlayer(contents)





