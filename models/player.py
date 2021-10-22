
class NewPlayers:
    """add players for tournament"""

    def __init__(self, first_name, last_name, date_of_birth, gender, tournament, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.tournament = tournament
        self.ranking = ranking
        self.point = 0
        """liste contenant les playeurs qui se rencontre, si ils ne se sont pas rencontrer ils peuvent faire le match"""
        self.fight = set()



    def __lt__(self, autre):
        """
        Trie par point ensuite par classement
        """

        if type(autre) is not type(self):
            raise TypeError

        return (-self.point, self.ranking) < (-autre.point, autre.ranking)


    def __str__(self):
        """Used in print"""
        return f"{self.first_name}"

    __repr__ = __str__


