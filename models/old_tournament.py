#from ..controllers.controllers import MakePairPlayer
from tinydb import TinyDB

db = TinyDB("./Chess-tournament/db.json")
tournament_table = db.table('tournament_table')

class Tournament:

    def list_of_tournament(self):

        # liste = [(tournament_table.search(all))]
        contents = [item['name'] for item in db.table('tournament_table').all()]
        print(contents)
        input = (">>> ")
        choice = []



