class NewTournamentView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print()
        print(">>>>> Vous allez devoir ajouter les informations pour un nouveau tournoi. <<<<<")
        print()

    def get_user_choice(self):
        while True:
            # afficher le menu à l'utilisateur
            self._display_menu()
            # demander à l'utilisateur de rentrer les infos
            print()
            name = input("Nom du tournoi >> ")
            place = input("Lieu >>")
            date = input("date >>")
            information = input("Il va y avoir 4 rounds, et il vous faut 8 joueurs."
                          "Voulez vous ")
            print()
            # valider le choix utilisateur
            if name in self.menu:
                # retourner le choix de l'utilisateur
                return self.menu[name]
            if place in self.menu:
                return self.menu[place]
            if date in self.menu:
                return self.menu[date]
            if information in self.menu:
                return self.menu[information]


print(NewTournamentView._display_menu(self=None))