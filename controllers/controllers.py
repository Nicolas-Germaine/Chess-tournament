from ..models.utils import Menu
from ..views.HomeMenuView import HomeMenuView
from ..views.PlayerView import PlayerView
from ..models.player import NewPlayers


class ApplicationController:
    """Main controller."""

    def __init__(self,):
        """List of players and a view."""
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

    def __call__(self):
        print("Dans le controller de Nouveau tournoi")
        print()

class OldTournamentController:
    """bbbb"""

    def __call__(self):
        print("Dans le controller de Charger un tournoi")
        print()

class NewPlayersController:
    """ccc"""
    def __init__(self):
        self.info = NewPlayers()
        self.view = PlayerView(self.info)

    def __call__(self):
        # 1. Construction d'une liste de joueur
        self.info.add("auto", "premier joueur", PlayerView())
        self.info.add("auto", "second joueur", PlayerView())
        self.info.add("auto", "troisieme joueur", PlayerView())

        # 2. Demander à la vue les inputs et de les collecter
        user_input = self.view.information_player()

        # 3. Pas tout compris
        return user_input

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
