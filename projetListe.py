# PROJET LISTE
# manipuler une une liste:
# Ajouter un element
# Retirer un Element
# Afficher la liste
# Vider la liste
# Quitter
# Votre choix: 

import sys # on va s'en servir dans le cas de l'option 5

LISTE = []

MENU = """Choississez parmis les 5 options suivantes :"
1: Ajouter un element 
2: Retirer un element
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix : """

MENU_CHOICES = ["1" , "2" , "3" , "4 " , "5"]

while True :
     user_choices = ""
     while user_choices not in MENU_CHOICES:
          user_choices = input(MENU)
          if user_choices not in MENU_CHOICES :
               print ("Veuillez choisir une option valide...")
     
     if user_choices =="1": # ajoter un element
          item = input("Entrez le nom d'un elemnt a ajouter a la liste de courses : ")
          LISTE.append(item)
          print(f"L'element {item} a bien été ajouté a la liste.")
     elif user_choices == "2": # retirer un element
          item = input("Entrez le nom d'un elemnt a retirer de la liste de courses :")
          if item in LISTE:
               LISTE.remove(item)
               print(f"L'element {item} a bien été supprimé de la liste.")
          else:
               print(f"L'element n'est pas dans la liste. ")
     elif user_choices == "3":# afficher la liste
          if LISTE:
               print ("Voici le contenue de votre liste : ")
               for i, item in enumerate(LISTE,1):
                    print(f"{i}. {item}")
          else:
               print("Votre liste ne contient aucun elemnt.")
     elif user_choices == "4": # Vider la liste
          LISTE.clear()
          print("La liste a été vidée de son contenue.")
     elif user_choices == "5": # Quitter 
          print("A bientot ! ")
          sys.exit

     print("-" * 50)