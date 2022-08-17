#une methode est une fonction qui appartient a un object
#EXEMPLE
# sorted(liste) et liste.sort() , nous permet toute les deux de trier une liste
# la fonction sorted n'agit pas directement sur la liste, elle va nous renvoyer une nouvelle version de la liste sans modifier la liste d'origine
# et si on veut que ce changement s'applique a notre liste d'origine il va falloir ecraser la premiere liste exp(liste=sorted(liste))
# par contre avec la methode liste.sort qui agit directement sur la liste d'origine vu qu'elle est directemnt affecter a un element
# sorted est une fonction

# LES OBJETS MUABLES ET IMMUABLES
# muables = listes,dictionnaires,sets
# immuables = chaines de caracteres ,nombres

# Quelques fonctions supplémentaires
# la fonction "len", qui nous retourne la longueur d'un element
# dans une chaine de caractère elle va nous retourner le nombre de lettre et dans une liste elle nous retournera le nombre d'element contenu dans la liste
len("python") # 6
len([1,2,3])  # 3

#Fonction "round", nous permet d'arrondir un nombre decimal vers le nombre entier le plus proche
round(2.2) # 2 
round(2.7) # 3
#Fonction "min", recupere la valeur minimum 
min([1,2,3]) # 1
#Fonction "max", recupere la valeur maximale
max([1,2,3]) # 3

# Fonction "sum", qui nous permet de recuperer la somme des elements dans une liste? on l'utilise qu'avec une structure de données qui contient jsute des nobres
sum([10,10,10]) #30

# Fonction "range", qui permet de facilement creer une liste de nombre allant de 0 au nombre indiqué de facon aleatoire
a=range(2,5)
#5H04MIN


