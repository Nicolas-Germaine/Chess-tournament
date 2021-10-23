#from ..controllers.controllers import MakePairPlayer
<<<<<<< HEAD
from tinydb import TinyDB,Query,where

=======
from ..models.player import NewPlayers
from tinydb import TinyDB, where
>>>>>>> 4b31f7d5a16606ded7b28db4dc726380f8c2bdaa
db = TinyDB("./Chess-tournament/db.json")
tournament_table = db.table('tournament_table')
player_table = db.table('player_table')

class Tournament:

    def list_of_tournament(self):

        contents = [item['name'] for item in db.table('tournament_table').all()]
        print(f"Liste des tournois dispo >>> {contents}")
        choice = str(input("Rentrez le nom du tournoi >>> "))
        table_tournament = db.table('tournament_table')
        name = tournament_table.search(where('name') == choice)
        #print("============", type(list(name[0]['players'].split(" "))))
        ##########################################################################
        for i in list(name[0]['players'].split(" ")):
            req_players = player_table.search(where('prenom') == str(i))
            print("===========", i)
            try:
                new_player = NewPlayers(req_players[0]['prenom'],
                                        req_players[0]['nom de famille'],
                                        req_players[0]['date de naissance'],
                                        req_players[0]['sexe'],
                                        req_players[0]['rang'])
                print(new_player)
            except:
                pass

        return name[0]['players']



# Crud = Create / Read / Update / Delete
# ex -> python tinyDB create


