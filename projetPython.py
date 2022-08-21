# L'utilisateur doit entrer deux nombre , ensuite je dois lui retourner une phrase et a la fin donner l'addition des deux nombres qu'il a rentrer
#from curses.ascii import isdigit


a= int(input("Entrez un premier nombre : "))
b= int(input("Entrez un deuxieme nombre : "))
print("le resultat de l'addition de "  + str(a)  +  " avec "  +  str(b)  + " est egal a "+ str(a+b))
print(f"Le resultat de l'addition de {a} avec {b} est egal a {int(a) + int(b)}") # deuxieme methode (on ajoute int si on ne l'a pas fait en declarant les variables)


