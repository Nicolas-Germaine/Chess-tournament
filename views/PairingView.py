
class Infos:

    def views_pairing(self, matches):
        
        list_joueurs = []
        for item in range(len(matches)):
            (player_1, player_2) = matches[item]
            print(f"*=**=*=*=*=*=*=*=*={player_1} VS {player_2}*=**=*=*=*=*=*=*=*=")
            print("======================")
            numb = input(f"Entre 1 si le joueur {player_1} est vainquer ou 0 si c'est un match nul ou 2 pour le joueur {player_2}  ")
            if int(numb)==1:
                player_1._point +=1
                player_1.fight.add(int(player_2.first_name))
                # player_2.fight.add(int(player_1.first_name))
                print("Le vainqueur est ",player_1)
            elif int(numb)==2:
                player_2._point +=1
                player_2.fight.add(int(player_1.first_name))
                # player_1.fight.add(int(player_2.first_name))
                print("Le vainqueur est ",player_2)
            elif int(numb)==0:
                player_1._point +=0.5
                player_2._point +=0.5
                player_1.fight.add(player_2.first_name)
                print("Match Nul")
            list_joueurs.append(player_1)
            list_joueurs.append(player_2)
            
        return sorted(list_joueurs)