# Regles du jeu

#-le jeu comporte deux jouers:vous et l'ennemi
#- Vous commencez tous les deux avec 50 points de vie
#- Votre passage dispose de 3 potions qui vous permettent de recuperer des points de vie
#- L'ennemi ne dispose d'aucune potion
#- Chaque potion vous permet de recuperer un nombre aleatoire de points de vie
#- Votre attaque inflige a l'ennemi des degats aléatoires compris entre 5 et 10 points de vie
#- L'attaque de l'ennemie vous inflige des degats aleatoire compris entre 5 et 15 points de vie
#- Lorsque vous utilisez une potion vous passez le prochain tour

# DEROULE DE LA PARTIE

# Lorsque vous lancez le script, vous devez demander a l'utilisateur s'il souhaite attaque ou utiliser une potion:
# si l'utilisateur choisi la premiere option ,vous infligez des points de degats a l'ennemi.
# ces points seront compris entre 5 et 10 et determinés aleatoirement par le programme
# si l'utilisateur choisi la deuxieme option, vous prenez la potion

import  random

ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False  # consiste a savoir si je vous passez le tour ou pas

while True :  # la boucle est infini
     # jeu du joueur
     if SKIP_TURN :
          print("Vous passez votre tour...")
          SKIP_TURN = False
     else : 
          user_choice = ""
          while user_choice not in ["1", "2" ] :
               user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
          if user_choice == "1": # attaque
               your_attack = random.randint(5,10) 
               ENEMY_HEALTH -= your_attack # soustaire a mon ennemi les points que je l'ai infligé
               print(f"Vous avez infligé {your_attack} points de degats a l'ennemi ")
          elif user_choice =="2": # potion 
               if NUMBER_OF_POTIONS > 0 : # verifier s'il nous reste des potions
                    potion_health = random.randint(15, 50)
                    PLAYER_HEALTH += potion_health
                    NUMBER_OF_POTIONS -= 1 # on decremente le nombre de potion
                    SKIP_TURN = True # passer le tout si on a utiliser une potion
                    print(f"Vous recuperer {potion_health} point de vie ({NUMBER_OF_POTIONS} restantes)")
               else : # si on a plus de potion...
                    print ("Vous n'avez plus de potions...")
                    continue

     if ENEMY_HEALTH <= 0: # verifier si l'ennemi n'est pas mort
        print("Tu as gagné")
        break

     # attack de l'ennemi
     enemy_attack = random.randint(5, 15)
     PLAYER_HEALTH -= enemy_attack
     print(f"L'ennemi vous a afligé {enemy_attack} points de degats")

     if PLAYER_HEALTH <= 0:  #verifier si le joueur est mort
          print("Tu as perdu")
          break
     # stats
     print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
     print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi.")
     print("-" * 50) # indiquer des separateurs entre les differents tirs de jeu

print("Fin du jeu")





