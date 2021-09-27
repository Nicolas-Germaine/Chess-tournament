
from tinydb import TinyDB, Query, table, where
db = TinyDB('db.json')

User = Query()
table_player = db.table('players')


class Insert:

    def insert_players1():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Nicolas",
            'nom de famille': 'Germaine',
            'date de naissance': '12/02/1987',
            'sexe': 'H',
            'rang': 1,
            'score': 0
            })

    def insert_players2():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Axel",
            'nom de famille': 'Germaine',
            'date de naissance': '21/08/2009',
            'sexe': 'H',
            'rang': 4,
            'score': 0
            })

    def insert_players3():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Laura",
            'nom de famille': 'Renaults',
            'date de naissance': '08/10/1988',
            'sexe': 'F',
            'rang': 3,
            'score': 0
            })

    def insert_players4():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Paul",
            'nom de famille': 'Jesaisplus',
            'date de naissance': '04/06/1990',
            'sexe': 'H',
            'rang': 7,
            'score': 0
            })

    def insert_players5():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Helene",
            'nom de famille': 'Laborde',
            'date de naissance': '07/02/1987',
            'sexe': 'F',
            'rang': 2,
            'score': 0
            })

    def insert_players6():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "David",
            'nom de famille': 'Pontiac',
            'date de naissance': '15/11/1991',
            'sexe': 'H',
            'rang': 8,
            'score': 0
            })

    def insert_players7():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Mathieu",
            'nom de famille': 'Cajon',
            'date de naissance': '07/05/1985',
            'sexe': 'H',
            'rang': 5,
            'score': 0
            })

    def insert_players8():
        player_table = db.table('players')
        player_table.insert({
            'prenom': "Stephanie",
            'nom de famille': 'Claure',
            'date de naissance': '18/03/1986',
            'sexe': 'F',
            'rang': 6,
            'score': 0
            })


class Ranking:
    def player1_ranking():
        result = table_player.search(User.rang == 1)
        result = [r['rang'] for r in result]
        return result

    def player2_ranking():
        result = table_player.search(User.rang == 2)
        result = [r['rang'] for r in result]
        return result
    
    def player3_ranking():
        result = table_player.search(User.rang == 3)
        result = [r['rang'] for r in result]
        return result

    def player4_ranking():
        result = table_player.search(User.rang == 4)
        result = [r['rang'] for r in result]
        return result

    def player5_ranking():
        result = table_player.search(User.rang == 5)
        result = [r['rang'] for r in result]
        return result

    def player6_ranking():
        result = table_player.search(User.rang == 6)
        result = [r['rang'] for r in result]
        return result

    def player7_ranking():
        result = table_player.search(User.rang == 7)
        result = [r['rang'] for r in result]
        return result
    
    def player8_ranking():
        result = table_player.search(User.rang == 8)
        result = [r['rang'] for r in result]
        return result


class Name:
    def player1_prenom():
        result = table_player.search(User.rang == 1)
        # result = [r['prenom'] for r in result]
        ### Pour retourner le prenom ou autre pas besoin de faire une liste comprehension c'est gourmant en term de memoire.
        ### faire le pour les autre fonction
        return result[0]['prenom']

    def player2_prenom():
        result = table_player.search(User.rang == 2)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']

    def player3_prenom():
        result = table_player.search(User.rang == 3)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']

    def player4_prenom():
        result = table_player.search(User.rang == 4)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']

    def player5_prenom():
        result = table_player.search(User.rang == 5)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']

    def player6_prenom():
        result = table_player.search(User.rang == 6)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']

    def player7_prenom():
        result = table_player.search(User.rang == 7)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']

    def player8_prenom():
        result = table_player.search(User.rang == 8)
        #result = [r['prenom'] for r in result]
        return result[0]['prenom']


def full_insert():

    Insert.insert_players1() # A commenter apres la premiere utilisation
    Insert.insert_players2() # A commenter apres la premiere utilisation
    Insert.insert_players3() # A commenter apres la premiere utilisation
    Insert.insert_players4() # A commenter apres la premiere utilisation
    Insert.insert_players5() # A commenter apres la premiere utilisation
    Insert.insert_players6() # A commenter apres la premiere utilisation
    Insert.insert_players7() # A commenter apres la premiere utilisation
    Insert.insert_players8() # A commenter apres la premiere utilisation


def start():

    print()
    print(f'Le premier match opposera {Name.player1_prenom()} qui est au rang {Ranking.player1_ranking()} à {Name.player5_prenom()} qui est au rang {Ranking.player5_ranking()} !! ')
    print(f'Le second match opposera {Name.player2_prenom()} qui est au rang {Ranking.player2_ranking()} à {Name.player6_prenom()} qui est au rang {Ranking.player6_ranking()} !! ')
    print(f'Le troisieme match opposera {Name.player3_prenom()} qui est au rang {Ranking.player3_ranking()} à {Name.player7_prenom()} qui est au rang {Ranking.player7_ranking()} !! ')
    print(f'Le quatrieme match opposera {Name.player4_prenom()} qui est au rang {Ranking.player4_ranking()} à {Name.player8_prenom()} qui est au rang {Ranking.player8_ranking()} !! ')
    print()

    Question1 = int(input('>>>>> Prêt ? (répondre 1 pour Oui, 2 pour Non.) <<<<<   '))
    if Question1 == 1:
        print("C'est parti !!!")
        print()
    else:
        print('Bye !!')
        print()


class Round1:


    
    def match1():

        resultat_match1 = []

        print(f'{Name.player1_prenom()} {Ranking.player1_ranking()} Contre {Name.player5_prenom()} {Ranking.player5_ranking()}')
        premier_match = float(input('Qui a gagner le premier match ? ( 1 pour le joueur 1, 2 pour le joueur 5 joueur, 0.5 pour une égalité. ) >>>>> '))
        if premier_match == 1:
            (print(f'{Name.player1_prenom()} WIN, il/elle gagne 1 point'))
            #### requette pour selection du player 1
            #### Affectation ou update du score
            resultat = table_player.update({'score':1},User.prenom == Name.player1_prenom())
            return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif premier_match == 2:
            (print(f'{Name.player5_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player5_prenom())
            return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
            resultat = table_player.update({'score':1},User.prenom == Name.player5_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif premier_match == 0.5:
            (print(f'égalité entre {Name.player1_prenom()} et {Name.player5_prenom()}, les deux gagnes 0.5 points.'))
            resultat1 = table_player.update({'score':0.5},User.prenom == Name.player1_prenom())
            resultat2 = table_player.update({'score':0.5},User.prenom == Name.player5_prenom())
            return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
            resultat1 = table_player.update({'score':0.5},User.prenom == Name.player1_prenom())
            resultat2 = table_player.update({'score':0.5},User.prenom == Name.player5_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        resultat_match1.extend([premier_match])
        return resultat_match1
        

    def match2():

        resultat_match2 = []

        print(f'{Name.player2_prenom()} {Ranking.player2_ranking()} Contre {Name.player6_prenom()} {Ranking.player6_ranking()}')
        second_match = float(input('Qui a gagner le second match ? ( 1 pour le joueur 2, 2 pour le joueur 6 joueur, 0.5 pour une égalité. ) >>>>> '))
        if second_match == 1:
            (print(f'{Name.player2_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player2_prenom())
            return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
            resultat = table_player.update({'score':1},User.prenom == Name.player2_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif second_match == 2:
            (print(f'{Name.player6_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player6_prenom())
            return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
            resultat = table_player.update({'score':1},User.prenom == Name.player6_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif second_match == 0.5:
            (print(f'égalité entre {Name.player2_prenom()} et {Name.player6_prenom()}, les deux gagnes 0.5 points.'))
            resultat1 = table_player.update({'score':0.5},User.prenom == Name.player2_prenom())
            resultat2 = table_player.update({'score':0.5},User.prenom == Name.player6_prenom())
            return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
            resultat1 = table_player.update({'score':0.5},User.prenom == Name.player2_prenom())
            resultat2 = table_player.update({'score':0.5},User.prenom == Name.player6_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        resultat_match2.extend([second_match])
        return resultat_match2


    def match3():

        resultat_match3 = []

        print(f'{Name.player3_prenom()} {Ranking.player3_ranking()} Contre {Name.player7_prenom()} {Ranking.player7_ranking()}')
        troisieme_match = float(input('Qui a gagner le troisieme match ? ( 1 pour le joueur 3, 2 pour le joueur 7 joueur, 0.5 pour une égalité. ) >>>>> '))
        if troisieme_match == 1:
            (print(f'{Name.player3_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player3_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif troisieme_match == 2:
            (print(f'{Name.player7_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player7_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif troisieme_match == 0.5:
            (print(f'égalité entre {Name.player3_prenom()} et {Name.player7_prenom()}, les deux gagnes 0.5 points.'))
            resultat1 = table_player.update({'score':0.5},User.prenom == Name.player3_prenom())
            resultat2 = table_player.update({'score':0.5},User.prenom == Name.player7_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        resultat_match3.extend([troisieme_match])
        return resultat_match3
    
    def match4():

        resultat_match4 = []

        print(f'{Name.player4_prenom()} {Ranking.player4_ranking()} Contre {Name.player8_prenom()} {Ranking.player8_ranking()}')
        quatrieme_match = float(input('Qui a gagner le quatrieme match ? ( 1 pour le joueur 4, 2 pour le joueur 8 joueur, 0.5 pour une égalité. ) >>>>> '))
        if quatrieme_match == 1:
            (print(f'{Name.player4_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player4_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif quatrieme_match == 2:
            (print(f'{Name.player8_prenom()} WIN, il/elle gagne 1 point'))
            resultat = table_player.update({'score':1},User.prenom == Name.player8_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        elif quatrieme_match == 0.5:
            resultat1 = table_player.update({'score':0.5},User.prenom == Name.player4_prenom())
            resultat2 = table_player.update({'score':0.5},User.prenom == Name.player8_prenom())
            # return db.update_multiple([({'score': 1}, where('score') == '0')])  # mise à jour bd
        resultat_match4.extend([quatrieme_match])
        return resultat_match4

class Round1Ranking:


    def results():


        classement = [Round1.match1(), Round1.match2(), Round1.match3(), Round1.match4()]
        print(classement)

def purchase():

    print()
    Question1 = int(input(">>>>> Voulez vous continuer ? (répondre 1 pour Oui, 2 pour Non.) <<<<<   "))
    if Question1 == 1:
        print("Second round !!!")
        print()
    else:
        print('Bye !!')
        print()

full_insert()
start()
Round1Ranking.results()
purchase()
