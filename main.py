"""Run."""

from models.player import Player
from controllers.controllers import Controller
from views.player import View


def main():
    view = View()
    game = Controller(view)
    game.run()


if __name__ == "__main__":
    main()