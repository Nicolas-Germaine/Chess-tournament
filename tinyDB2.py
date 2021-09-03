from tinydb import TinyDB

class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


db = TinyDB('db.json')
player_table = db.table('player')

def insert():
    player1 = Player(first_name=input("Tapez le prénom >> "), last_name=input("Tapez le nom de famille >> "))
    player2 = Player(first_name='Axel', last_name='Germaine')


    serialized_player1 = {
        'first_name': player1.first_name,
        'last_name': player1.last_name
        }


    serialized_player2 = {
        'first_name': player2.first_name,
        'last_name': player2.last_name
    }

    first_name = serialized_player1['first_name']
    last_name = serialized_player1['last_name']
    player_1 = Player(first_name=first_name, last_name=last_name)

    first_name = serialized_player2['first_name']
    last_name = serialized_player2['last_name']
    player_2 = Player(first_name=first_name, last_name=last_name)


    print(serialized_player1)
    print(serialized_player2)


"""serialized_player1.insert = player_table.all()
serialized_player2.insert = player_table.all()"""
