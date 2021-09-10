

from tinydb import TinyDB, Query,where
db = TinyDB('db.json')


def insert_tournament():
    tournament_table = db.table('tournament_table')
    tournament_table.insert({'name': 'Super tournoi', 'place': 'Toulouse', 'date': '21/12/2009'})

def insert_players1():
    player_table = db.table('players')
    player_table.insert({
        'prenom': "Nicolas",
        'nom de famille': 'Germaine',
        'date de naissance': '12/02/1987',
        'sexe': 'H',
        'rang': 1
        })

def insert_players2():
    player_table = db.table('players')
    player_table.insert({
        'prenom': "Axel",
        'nom de famille': 'Germaine',
        'date de naissance': '21/08/2009',
        'sexe': 'H',
        'rang': 2
        })

"""insert_tournament()
insert_players1()
insert_players2()"""

#   Je voudrais print mon dico entier et pouvoir aussi print certains elements du dico
table_player = db.table('players')
print(table_player.all())
print(table_player.all()[0]) # Pour afficher le premier joueur

