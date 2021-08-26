"""Run."""

from controllers.controllers import ApplicationController
from views.player import View


def main():
    view = View()
    game = ApplicationController(view)
    game.run()


if __name__ == "__main__":
    main()
