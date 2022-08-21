#EXERCICE
#Exercici 1, l'utilisateur doit rentrer un mot de passe et en fonction de se qu'il va rentrer on doit lui retourner une phrase
# verifier la longueur d'un mot de passe et le contenu d'un mot de passe entré par l'utilisateur
#from curses.ascii import isdigit (pas obligatoire)

mdp = input("Entrez un mot de passe (minimum 8 caractères) : ")

mdp_trop_court= "votre mot de passe est trop court."

if (len(mdp) == 0):
     print(mdp_trop_court.upper())
elif(len(mdp) < 8): 
     print(mdp_trop_court.capitalize())
elif(mdp.isdigit()):
     print("Votre mot de passe ne contient que des nombres.")
else:
     print("Inscription terminée")
