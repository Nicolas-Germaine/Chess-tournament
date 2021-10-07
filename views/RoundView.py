from tinydb import TinyDB
from ..views.PlayerView import PlayerView

# tentative de recup d'infos à partir de TinyDB pour faire le premier round


class Infos:

    def init(self, players):
        self.players = players
        self.view = Pairing()

    def first_round(self):
        middle = len(self.players) // 2
        groups = self.players[:middle], self.players[middle:]
        matches = list(zip(groups[0], groups[1]))
        print(matches)

        ### appel de la view pour enregistrer les resultats et Print les resultats en console
        return self.view.views_pairing(matches)


class MakePairPlayer:

    def __init__(self, players):

        self.players = players
        print("Dans la vue de start")

    def firts_round(self):
        middle = len(self.players)//2
        groups = self.players[:middle], self.players[:middle]
        matches = list(zip(groups[0], groups[1]))
        print(matches)