
class NewPlayers:
    def __init__(self, name, age, date, ranking):
        self.name = name
        self.age = age
        self.date = date
        self.ranking = ranking

    def info_player(self):
        return f"Le joueur s'appelle {self.name}, il a {self.age}ans, il est née le {self.date}" \
               f" et il est {self.ranking} au classement."


player1 = NewPlayers("Nicolas", 34, "12/02/1987", 1)
player2 = NewPlayers("Axel", 12, "21/08/2009", 2)
player3 = NewPlayers("Leslie", 33, "30/07/1987", 3)

"""print(player1.info_player())
print(player2.info_player())
print(player3.info_player())"""
