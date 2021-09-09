import datetime

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

        while nb < 8:

            first_name = input("Tapez le prénom >> ")
            last_name = input("Tapez le nom de famille >> ")
            while True:
                try:
                    date_of_birth_str = input("Tapez la date de naissance (ex ->    00/00/0000) >> ")
                    date = datetime.datetime.strptime(date_of_birth_str, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Oops!  Le format n'est pas valide.  Try again...")
            gender = input("Sexe ? (H/F) >> ")
            while True:
                try:
                    ranking = int(input("Son rang ? (ex ->  11) >> "))
                    break
                except ValueError:
                    print("Oops!  Le format n'est pas valide.  Try again...")
            new_player.extend([first_name, last_name, date_of_birth_str, gender, ranking])
            nb += 1

        return new_player
