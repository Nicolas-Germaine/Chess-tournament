

from tinydb import TinyDB, Query, table
db = TinyDB('db.json')


"""def insert_tournament():
    tournament_table = db.table('tournament_table')
    tournament_table.insert({'name': 'Super tournoi', 'place': 'Toulouse', 'date': '21/12/2009'})
"""

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

#insert_tournament()
#insert_players1()
#insert_players2()

User = Query()
table_player = db.table('players')
table_tournament = db.table('tournament_table')
player_prenom = db.table('prenom')

print(player_prenom)
"""item = db.table('players')"""

"""def search():
    player1 = table_player.search(User.rang == 1)
    player2 = table_player.search(User.rang == 2)
    print(player1)
    print(player2)
    print(player1[0])"""

#print(db.tables())
"""print(db.table('players'[1]))"""

#print(table_player.all())
#print(table_player.search(User.rang == 2))
#print(table_tournament.all())

#item = table_player
"""for k in item:
    print(k)"""

#print(item)

#search()
