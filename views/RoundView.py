from tinydb.database import TinyDB
import PlayerView

# tentative de recup d'infos à partir de TinyDB pour faire le premier round

class Infos:

    def __init__(self):

        self.view = PlayerView()
        self.db = TinyDB("./db.json")

    def __call__(self):
        print("self.PlayerView")
        user_info = self.db('player_table')

        return MakePairPlayer(user_info)

class MakePairPlayer:

    def __init__(self, players):

        self.players = players

    def firts_round(self):
        middle = len(self.players)//2
        groups = self.players[:middle], self.players[:middle]
        matches = list(zip(groups[0], groups[1]))
        print(matches) 