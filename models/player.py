
class NewPlayers:
    """add players for tournament"""

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self._ranking = ranking
        self._point = 0
        """liste contenant les playeurs qui se rencontre, si ils ne se sont pas rencontrer ils peuvent faire le match"""
        self.fight = set()

    def __lt__(self, autre):
        """
        Trie par point ensuite par classement
        """

        if type(autre) is not type(self):
            raise TypeError

        return (-self._point, self._ranking) < (-autre._point, autre._ranking)

    @property
    def ranking(self):
        return self._ranking

    def __str__(self):
        """Used in print"""
        return f"{self.first_name} {self._point: >10} {self._ranking: >4}"

    __repr__ = __str__


