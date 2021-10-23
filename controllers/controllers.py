from ..models.utils import Menu
from ..views.HomeMenuView import HomeMenuView
from ..views.NewTournamentView import NewTournamentView
from ..views.PlayerView import PlayerView
from ..views.PairingView import Infos
from ..models.old_tournament import Tournament
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
        db = TinyDB("./Chess-tournament/db.json")
        tournament_table = db.table('tournament_table')
        serialized_player1 = {
            'name': user_input[0],
            'lieu': user_input[1],
            'date': user_input[2],
            'players': [],
        }
        tournament_table.insert(serialized_player1)
        print("Tournoi crée")

        return HomeMenuController


class OldTournamentController:
    """bbbb"""

    def __call__(self):
        old_players_tournament = Tournament.list_of_tournament(list)
        #MakePairPlayer(old_players_tournament)


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
        db = TinyDB('./Chess-tournament/db.json')
        player_table = db.table('player_table')

        serialized_player1 = {
            'prenom': user_input[0].first_name,
            'nom de famille': user_input[0].last_name,
            'date de naissance': user_input[0].date_of_birth,
            'sexe': user_input[0].gender,
            'rang': user_input[0].ranking,

        }
        player_table.insert(serialized_player1)

        serialized_player2 = {
            'prenom': user_input[1].first_name,
            'nom de famille': user_input[1].last_name,
            'date de naissance': user_input[1].date_of_birth,
            'sexe': user_input[1].gender,
            'rang': user_input[1].ranking,

        }
        player_table.insert(serialized_player2)

        serialized_player3 = {
            'prenom': user_input[2].first_name,
            'nom de famille': user_input[2].last_name,
            'date de naissance': user_input[2].date_of_birth,
            'sexe': user_input[2].gender,
            'rang': user_input[2].ranking,

        }
        player_table.insert(serialized_player3)

        serialized_player4 = {
            'prenom': user_input[3].first_name,
            'nom de famille': user_input[3].last_name,
            'date de naissance': user_input[3].date_of_birth,
            'sexe': user_input[3].gender,
            'rang': user_input[3].ranking,

        }
        player_table.insert(serialized_player4)
        """
        serialized_player5 = {
            'prenom': user_input[4].first_name,
            'nom de famille': user_input[4].last_name,
            'date de naissance': user_input[4].date_of_birth,
            'sexe': user_input[4].gender,
            'rang': user_input[4].ranking,
        }
        player_table.insert(serialized_player5)

        serialized_player6 = {
            'prenom': user_input[5].first_name,
            'nom de famille': user_input[5].last_name,
            'date de naissance': user_input[5].date_of_birth,
            'sexe': user_input[5].gender,
            'rang': user_input[5].ranking,
        }
        player_table.insert(serialized_player6)

        serialized_player7 = {
            'prenom': user_input[6].first_name,
            'nom de famille': user_input[6].last_name,
            'date de naissance': user_input[6].date_of_birth,
            'sexe': user_input[6].gender,
            'rang': user_input[6].ranking,
        }
        player_table.insert(serialized_player7)

        serialized_player8 = {
            'prenom': user_input[7].first_name,
            'nom de famille': user_input[7].last_name,
            'date de naissance': user_input[7].date_of_birth,
            'sexe': user_input[7].gender,
            'rang': user_input[7].ranking,
        }
        player_table.insert(serialized_player8)"""
        print()
        print(">>>>> 8 joueurs ajouter. <<<<<")
        print()
        #return MakePairPlayer(user_input)


class OldPlayersController:
    """ddd"""

    def __call__(self):
        print("Dans le controller de Charger une liste de joueurs")
        print()


class MakePairPlayer:

    def __init__(self, players):

        self.players = players
        self.view = Infos()

    def first_round(self):

        middle = len(self.players) // 2
        groups = self.players[:middle], self.players[middle:]
        matches = list(zip(groups[0], groups[1]))
        print(matches)

        ### appel de la view pour enregistrer les resultats et Print les resultats en console
        return self.view.views_pairing(matches)
        ### Trier les joueurs par nombre de point et par classement
        ### Return les joueur

    def other_round(self, playeround):
        """
        Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite.
        Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        """
        # print("first rounddddddd", playeround)
        groups = playeround[::2], playeround[1::2]
        matches = list(zip(groups[0], groups[1]))

        availables = sorted(playeround)
        # print("le testtt unique===", availables)

        for item in range(len(matches)):
            (player_1, player_2) = matches[item]
            availables.remove(player_1)

            if player_2 in player_1.fight:
                possibles = [p for p in availables if p not in player_1.fight]

                if not possibles:
                    availables.remove(player_2)
                    # print("not possiblesnot possiblesnot possibles")
                else:
                    # print("possibles", possibles)
                    figther = next(iter(sorted(possibles)))
                    # print("figther===>", figther)
                    matches[item] = (player_1, figther)

                    availables.remove(figther)
                    # print("Matches possible ===", matches)
                    groups2 = availables[::2], availables[1::2]

                    matches2 = list(zip(groups2[0], groups2[1]))
                    # print("Matches Matches 22===", matches2)
                    matches[item + 1:] = matches2
                    # print("possible Matches 22===", matches)
        print("matches====>", matches)
        return self.view.views_pairing(matches)

    def __call__(self):
        print("self.MakePairPlayer")
        # Round 1
        print("==================FIRST ROUND ======================")
        round1 = self.first_round()
        # Round 2
        print("==================2E ROUND ======================")
        round2 = self.other_round(round1)
        # Round 3
        print("==================3E ROUND ======================")
        round3 = self.other_round(round2)
        # Round 4
        print("==================4E ROUND ======================")
        round4 = self.other_round(round3)


class EndScreenController:
    """eee"""

    def __call__(self):
        print("Au revoir !")
        print()


if __name__ == "__main__":
    app = ApplicationController()
    app.start()
