from typing import List

from models.player import Player

class Controller:
    """Main controller."""

    def __init__(self, view):
        """List of players and a view."""
        # models
        self.menu: List[Main Menu] = []
        self.players: List[Player] = []

        # views
        self.view = view

    def get_players(self):
        """Get some players."""
        while len(self.players) < 5:  # nombre magique
            name = self.view.information_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def run(self):
        """Run the game."""
        self.get_players()