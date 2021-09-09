from ..models.utils import Menu
from ..views.HomeMenuView import HomeMenuView
from ..views.NewTournamentView import NewTournamentView
from ..views.PlayerView import PlayerView
from tinydb import TinyDB


class ApplicationController:
    """Main controller."""

    def __init__(self):
        """..."""
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()

class HomeMenuController:
    """List of menu"""
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        # Contruction menu
        self.menu.add("auto", "Nouveau tournoi", NewTournamentController())
        self.menu.add("auto", "Charger un tournoi", OldTournamentController())
        self.menu.add("auto", "Ajouter des joueurs", NewPlayersController())
        self.menu.add("auto", "Charger une liste de joueurs", OldPlayersController())
        self.menu.add("q", "Quitter", EndScreenController())

        # Demander à la vue d'afficher le menu et collecte de réponse utilisateur
        user_choice = self.view.get_user_choice()

        # Retourner le controller associer au choix de l'utilisateur au controlleur principal
        return user_choice.handler

class NewTournamentController:
    """aaaa"""
    def __init__(self):
        """self.info = NewPlayers()"""
        self.view = NewTournamentView()

    def __call__(self):
        user_input = self.view.information_tournament()
        print(user_input)
        db = TinyDB("Chess-tournament/db.json")
        tournament_table = db.table('tournament_table')
        serialized_player1 = {
            'name': user_input[0],
            'lieu': user_input[1],
            'date': user_input[2],
            }
        tournament_table.insert(serialized_player1)
        print("Tournoi crée")
        
        return HomeMenuController

class OldTournamentController:
    """bbbb"""

    def __call__(self):
        print("Dans le controller de Charger un tournoi")
        print()

class NewPlayersController:
    """ccc"""
    def __init__(self):
        """self.info = NewPlayers()"""
        self.view = PlayerView()

    def __call__(self):
        print(">>>>> Vous allez devoir ajouter les informations pour 8 joueurs. <<<<<")
        print()
        user_input = self.view.information_player()
        print(user_input)
        db = TinyDB('Chess-tournament/db.json')
        player_table = db.table('player_table')
        
        serialized_player1 = {
            'prenom': user_input[0],
            'nom de famille': user_input[1],
            'date de naissance': user_input[2],
            'sexe': user_input[3],
            'rang': user_input[4]
            }
        player_table.insert(serialized_player1)

        serialized_player2 = {
            'prenom': user_input[5],
            'nom de famille': user_input[6],
            'date de naissance': user_input[7],
            'sexe': user_input[8],
            'rang': user_input[9]
            }
        player_table.insert(serialized_player2)

        serialized_player3 = {
            'prenom': user_input[10],
            'nom de famille': user_input[11],
            'date de naissance': user_input[12],
            'sexe': user_input[13],
            'rang': user_input[14]
            }
        player_table.insert(serialized_player3)

        serialized_player4 = {
            'prenom': user_input[15],
            'nom de famille': user_input[16],
            'date de naissance': user_input[17],
            'sexe': user_input[18],
            'rang': user_input[19]
            }
        player_table.insert(serialized_player4)

        serialized_player5 = {
            'prenom': user_input[20],
            'nom de famille': user_input[21],
            'date de naissance': user_input[22],
            'sexe': user_input[23],
            'rang': user_input[24]
            }
        player_table.insert(serialized_player5)

        serialized_player6 = {
            'prenom': user_input[25],
            'nom de famille': user_input[26],
            'date de naissance': user_input[27],
            'sexe': user_input[28],
            'rang': user_input[29]
            }
        player_table.insert(serialized_player6)

        serialized_player7 = {
            'prenom': user_input[30],
            'nom de famille': user_input[31],
            'date de naissance': user_input[32],
            'sexe': user_input[33],
            'rang': user_input[34]
            }
        player_table.insert(serialized_player7)

        serialized_player8 = {
            'prenom': user_input[35],
            'nom de famille': user_input[36],
            'date de naissance': user_input[37],
            'sexe': user_input[38],
            'rang': user_input[39]
            }
        player_table.insert(serialized_player8)
        print()
        print(">>>>> 8 joueurs ajouter. <<<<<")
        return HomeMenuController


class OldPlayersController:
    """ddd"""

    def __call__(self):
        print("Dans le controller de Charger une liste de joueurs")
        print()

class EndScreenController:
    """eee"""

    def __call__(self):
        print("Au revoir !")
        print()


if __name__ == "__main__":
    app = ApplicationController()
    app.start()
