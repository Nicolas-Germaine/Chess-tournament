from tinydb import TinyDB
db = TinyDB('db.json')

class Player:
    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

class Data_base():

    player1 = Player(first_name=input("Tapez le prénom >> "),
                 last_name=input("Tapez le nom de famille >> "),
                 date_of_birth=input("Tapez la date de naissance (ex 12/02/1987) >> "),
                 gender=input("Sexe ? (H/F) >> "),
                 ranking=input("Son rang ? >> "))

    serialized_player1 = {
            'first_name': player1.first_name,
            'last_name': player1.last_name,
            'date_of_birth': player1.date_of_birth,
            'gender': player1.gender,
            'ranking': player1.ranking
            }
    db.insert(serialized_player1)
    print(serialized_player1)

"""class PlayerView:
    def insert(self):
        nb = 0

        while nb < 2:
            db.insert({
                "first_name":
                    input("Tapez le prénom >> "),
                "last_name":
                    input("Tapez le nom de famille >> "),
                "date_of_birth":
                    input("Tapez la date de naissance (ex 12/02/1987) >> "),
                "gender":
                    input("Sexe ? (H/F) >> "),
                "ranking":
                    input("Son rang ? >> ")})
            nb += 1

        return insert()"""
