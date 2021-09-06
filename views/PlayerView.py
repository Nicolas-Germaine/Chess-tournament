"""Base view."""

class PlayerView:

    def info_menu(self):
        print()
        print(">>>>> Vous allez devoir ajouter les informations pour 8 joueurs. <<<<<")
        print()

    def information_player(self):
        """"""
        new_player = []
        nb = 0

        while nb < 2:

            first_name = input("Tapez le prénom >> ")
            last_name = input("Tapez le nom de famille >> ")
            date_of_birth = input("Tapez la date de naissance (ex 12/02/1987) >> ")
            gender = input("Sexe ? (H/F) >> ")
            ranking = input("Son rang ? >> ")
            new_player.extend([first_name, last_name, date_of_birth, gender, ranking])
            nb += 1

        return new_player
