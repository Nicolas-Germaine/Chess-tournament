from tinydb import TinyDB
db = TinyDB('db.json')


def insert():

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


class PlayerView:
    insert()
