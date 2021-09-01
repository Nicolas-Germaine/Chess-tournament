
class NewPlayers:
    def __init__(self):
        self._entries = {}

    def add(self, first_name, last_name, date_of_birth, gender, ranking):
        self._entries = (first_name, last_name, date_of_birth, gender, ranking)

    def info_player(self):
        return f"Le joueur s'appelle {self.first_name} {self.last_name}, il/elle est née le {self.date_of_birth}" \
               f" et il/elle est {self.ranking} au classement."


"""player1 = NewPlayers("Nicolas", "Germaine", 34, "12/02/1987", 1)
player2 = NewPlayers("Axel", "Germaine", 12, "21/08/2009", 2)
player3 = NewPlayers("Leslie", "Stouvenel", 33, "30/07/1987", 3)"""

"""print(player1.info_player())
print(player2.info_player())
print(player3.info_player())"""
