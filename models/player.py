
class NewPlayers:
    """add players for tournament"""

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        """liste contenant les playeurs qui se rencontre, si ils ne se sont pas rencontrer ils peuvent faire le match"""
        self.fight = []

    def __repr__(self) -> str:
        """Used in print"""
        return f"{self.first_name} {self.last_name}"