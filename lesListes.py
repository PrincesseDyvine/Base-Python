# une lsite peut etre vide, contenir plusieurs types de variables,on peut ajouter ou retirer les elements d'une liste
# attention le mot "list" est mot reservé a python qui permet notamment de convertir des elements en liste
# Ajouter et retirer les elements d'une liste
#append,pour ajouter des element et elle ajoute une seule valeur a la fois si on veut ajouter plusieurs valeurs on utilse "extend" en utilisant comme liste
#remove, pour enlever un element dans la liste et elle enleve juste la premiere occurrence de la liste
# pour recuperer un element dans une liste on va utiliser des indices qui correspondent a la position EXP: liste[0]
# on peut egalement utiliser des indices negatifs soit -1 le dernier element de la liste
# les slices ,permet de recuper jsute quelques elements de la liste
liste=["utilisateur_01","utilisateur_02","utilisateur_03","utilisateur_04","utilisateur_05","utilisateur_06"]
print(liste[0:1]) # il va juste recuperer le premier utilisateur si on veut recuperer les deuxieme on doit mettre [0:2]

liste=["utilisateur_01","utilisateur_02","utilisateur_03","utilisateur_04","utilisateur_05","utilisateur_06"]
print(liste[:]) # On peut egalement ne rien mettre et ça va juste recuperer la totalité de utilisateurs en commençant par le premier 

liste=["utilisateur_01","utilisateur_02","utilisateur_03","utilisateur_04","utilisateur_05","utilisateur_06"]
print(liste[::2]) # on peut egalement utiliser cette methode pour specifier le pat (1sur 2), 

liste=["utilisateur_01","utilisateur_02","utilisateur_03","utilisateur_04","utilisateur_05","utilisateur_06"]
print(liste[::-1]), #on peut egalement mettre un nombre negatif au pat ce qui va permettre de renverser la liste
#----------------------------------------------------------------------------------------------------------------------
# D'autres choses a faire avec les listes
# index ,pour connaitre l'emplacement ou encore la position d'un element dans la liste
employes=["Carlos", "Max","Martine","Patrick","Alex"]
resultat=employes.index("Max")
print(resultat)
#--------------------------------------------------------
# "count" compter le nombre d'occurence dans la liste
employes=["Carlos", "Max","Martine","Patrick","Alex","Max"]
resultat=employes.count("Max")
print(resultat) # et la nous aurons comme resultat 2 car nous avons deux "Max" dans la liste
#-----------------------------------------------------------------------------------------------
# "sort" , qui permet de trier la liste
employes=["Carlos", "Max","Martine","Patrick","Alex"]
employes.sort()
print(employes) # elle va trier par ordre alphabetique, il faut faire attention a la syntaxe,on trie directement 
# on peut le faire egalement avec la methode sorted mais elle retourne le resultat dans une liste sans impacter la liste d'origine
#-------------------------------------------------------------------------------------------------------------------
# reverse, elle va inverser l'ordre de la liste
employes=["Carlos", "Max","Martine","Patrick","Alex"]
employes.reverse()
print(employes) #['Alex', 'Patrick', 'Martine', 'Max', 'Carlos'], elle va juste inverser la liste
#----------------------------------------------------------------------------------------------------
#Elements pur enlever des elements dans une liste
# 4h39min 40 SECONDES

