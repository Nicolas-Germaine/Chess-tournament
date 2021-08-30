"""Player."""


class Player:
    """Players info."""

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        self.first_name = first_name        # Prénom
        self.last_name = last_name          # Nom de famille
        self.date_of_birth = date_of_birth  # Date de naissance
        self.gender = gender                # Sexe
        self.ranking = ranking              # Classement

"""player = Player(first_name='Bob', last_name='Dupont', date_of_birth= '12/02/1987',
                gender='M', ranking='1')
print(player.first_name, player.last_name, player.date_of_birth, player.gender,
      player.ranking)

serialized_player = {
    'first_name': player.first_name,
    'last_name': player.last_name,
    'date_of_birth': player.date_of_birth,
    'gender': player.gender,
    'ranking': player.ranking
}

first_name = serialized_player['first_name']
last_name = serialized_player['last_name']
date_of_birth = serialized_player['date_of_birth']
gender = serialized_player['gender']
ranking = serialized_player['ranking']"""

"""db = TinyDB('db.json')
player_table = db.table('player')
player_table.truncate()  # clear the table first
player_table.insert_multiple(serialized_player)"""

