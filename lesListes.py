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
# La methode pop, il supprime par rapport a l'index et nom par rapport au nom de l'element
# EXEMPLE, on va retirer le dernier element de notre liste
employes=["Carlos", "Max","Martine","Patrick","Alex"]
employes.pop(-1)
print(employes)
# EXEMPLE 2 , au cas ou on veut recuperer un element supprimer
employes=["Carlos", "Max","Martine","Patrick","Alex"]
element=employes.pop(-1)
print(employes)
print(element)
# Methode clear , qui va enlever tout les element de la liste
employes=["Carlos", "Max","Martine","Patrick","Alex"]
employes.clear()
print(employes)

# La methode "join" , qui permet de joindre ensemble differents elements d'une liste, elle s'utilise unique ment sur une chaine de caractères
# EXEMPLE
liste= ["python", "est", "un", "langage", "incroyable"]
resultat = " ".join(liste) 
print(resultat)
# EXEMPLE 2
liste= ["python", "est", "un", "langage", "incroyable"]
resultat = " - ".join(liste) # on peu egalement definir la ponctuation avec laquelle on veut separer nos chaines de caracteres 
print(resultat)

# Creer une liste a partir d'une chaine de caractere
# EXEMPLE
courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses= courses.split() # par defaut la methode split separe par la virgule
print(courses)
# exemple 2
courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses= courses.split(", ") # on ajout une virgule et une espace afin d'avoir juste les virgules qui separe chaque chaine de caracters
print(courses)

# Les operateurs d'appartenance , nous permet de verifier si un element appartient ou non a une structure de données
#EEMPLE, on verifie si la chaine de carateres Paul est presente dans la liste
utilisateurs=["Paul", "Pierre", "Marie"]
"Paul" in utilisateurs # il retourne un boleen
#EXEMPLE 2
utilisateurs=["Paul", "Pierre", "Marie"]
if "Paul" in utilisateurs:
     utilisateurs.remove("Paul")
     print(utilisateurs)

# Les listes imbriquées,c'est a dire les listes a l'interieur des listes
#EXEMPLE, on doit recuperer l'element "java"
liste=["python",["java","C++", ["C"]], ["ruby"]]
print(liste[1] [0]) #on extrait premieremnt le bloc ou "java " se trouve avant de le recuperer directement dans sa liste
# EXEMPLE 2
liste=["python",["java","C++", ["C"]], ["ruby"]]
print(liste[0] [0]) # en faisant cela ca donne le premierre lettre du premmeir element de la liste

# pour recuperer un element dans la liste on le faite toujours avec ddes crochets
#avec remove il faut specifeir l'element qu'on veut supprimer
# avec pop par contre on supprime un element avec l'indice de cet element dans la liste


