# JEU DU NOMMBRE MYSTERES?L'UTILISATEUR DOIT POUVOIR DEVINER UN NOMBRE MYSTERE ENTRE 0 ET 100 EN UN 5 ESSAIS
# A chaque essaie on doit dire si le nombre qu'il a saisi est plus gand ou plus petit que le nombre mystere
# s'il ne parvient a trouver le nombre mystere au bot de 5 essai on lui retourne "dommage" en affichant egalemnt le nombre mystere

from random import randint

number_to_find = randint(0,100)
remaining_attempts = 5 # le nombre d'essai restant

print("*** Le jeu du nombre mystère***")

# Boucle principale
while remaining_attempts > 0:
     print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}") #(pour ajouter s a essais)
# saisie de l'utilisateur
     user_choice = input("Devine le nombre : ")
     if not user_choice.isdigit():
          print("Veuillez entrer un nombre valide.")
          continue
     
     user_choice = int(user_choice)

     if number_to_find > user_choice: # plus grand
          print (f"Le nombre mystere est plus grand que {user_choice}")

     elif number_to_find < user_choice: # plus petit
          print(f"Le nombre mystere est plu petit que {user_choice}")

     else: # egal(succès)
          break
     remaining_attempts -= 1
# Gagné ou perdu 
if remaining_attempts ==0:
     print(f"Dommage ! Le nombre mystère etait {number_to_find} !")
else:
     print(f"Bravo ! Le nombre mystère etait bien {number_to_find} !")
     print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")
print("Fin du jeu.")