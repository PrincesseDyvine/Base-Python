# Manipulation des chaines de caractères 2H29
# upper : modifier une chaine de caractere pour la mettre en majuscule
from email.policy import strict


a="bonjour"
print(a.upper())
#--------------------------------------------------
# lower: pour mettre en miniscul
b="BONSOIR"
print(b.lower())
#----------------------------------------------------
# capitolize:permet de mettre une majuscule au debut d'une chaine de caractere
c="bonjour tout le monde"
print(c.capitalize()) # ne pas confondre avec title() qui met les majuscules a chaque premiere lettre d'un mot
#----------------------------------------------------------------------------------------------------------------
# remplacer et modifier des parties des chaines de caractere
# replace: permet de remplacer un ou plusieurs caractere par un autre
a="bonjour"
print(a.replace("jour","soir")) # il a remplecé jour par soir
f="bonjour bonjour"
print(f.replace("jour","soir")) # il va remplacer ou tous les mots ou il ya jour
# on peut aussi l'utiliser pour enlever l'espace entre les chaines de caracteres
#----------------------------------------------------------------------------------
#strip:
a=" bonjour "
print(a.strip()) # par defaut si on ne lui passe rien elle va juste enlever les espaces
# celle-ci fonctionne unique sur le debut et la fin de la chaine de caracter et pas au milieu
a=" bonjour "
print(a.strip(" ujor")) # on va donc rester avec "bon"
# il faut savoir qu'il prend egalement en compte les espaces, et l'ordre n'a pas d'importance
# pour specifier qu'on veut par exemple affecter les partie droite (rstrip) ou (lstrip) pour la gauche
#-------------------------------------------------------------------------------------------------------
# SEPARER ET JOINDRE
# split: pour separer
n="1, 2, 3, 4, 5"
print(n.split(", ")) # ça separe en fonction de ce qu'on entre par exemple dans notre cas il va separer en fonction de la virgule et renvoie sur forme de liste
n="1, 2, 3, 4, 5"
print(n.join(", "))
#-------------------------------------------------------------------------------------------------------------------
#zfill: permet de determiner le nombre de caracter qu'on veut afficher elle n'est utuliser que sur les chaines de caractere
a="9"
print(a.zfill(4)) # ca nous renvoie a "0009" POUR AVOIR 4 caracteres
i=[20]
for i in range(20) :
    print(str(i).zfill(2)) # cela va npus afficher le meme nmbre de caractere pour avoir une meiulleure vue(01,02,03...)
#----------------------------------------------------------------------------------------------------------------
#is: permet de verifier si une chaine de caractere verifie une condition
a=" bonjour "
print(a.islower()) # si la condition est verifié il va renvoir un boleen soit TRUE ou FALSE
a=" Bonjour "
print(a.islower()) # false
a=" Bonjour "
print(a.istitle()) # cela verifie si la chaine rempli les condition d'un titre c'est dire toute les premeiers lettre d'un mos sont en majuscule
a="50 "
print(a.isdigit()) #pour savoir si la chaine de caractere contient uniquement des chiffres #TRUE
a=" cl "
print(a.istitle()) # FALSE car on a autre chose qu'un chiffre
#---------------------------------------------------------------------------------------------
# COMPTER LE NOMBRE D OCCURENCE
#count: elle compte les carcters present et non le mots
a=" bonjour le jour"
print(a.count("jour")) # elle renvoi 2 car on a deux fois jour dans la chaine , pour changer cela il faut juste ajouter un espace au debut pour bien specifier
a=" bonjour le jour"
print(a.count(" jour")) # et la ca nous renvoie 1 acause de l'espace
#--------------------------------------------------------------------------------
# TROUVER UNE CHAINE OU SUITE DE CARACTERE
#FIND: il va trouver a partir de combien de lettre un le caractere demandé apparait
a="bonjour le jour"
print(a.find("jour")) # ca nous renvoi 3 car b=0,o=1,n=2 et (j=3) ou le mot jour commence
a="bonjour le jour"
print(a.index("jour")) # index renvoie le meme resultat
# sauf qu'avec fIND s'il ne trouve pas le caractere demandé il va inscrire -1 et INDEX va signaler une erreur
a="bonjour le jour"
print(a.rfind("jour"))
# pour la fonction FIND on peut utiliser rfind uniquement pour demander de commencer vers la droite
#--------------------------------------------------------------------------------------------------
# CHERCHER AU DEBUT ET A LA FIN
#endswith
a="image.png"
print(a.endswith(".png")) # ca retour # TRUE car la chaine de caractere se termine bien par cette element au cas contraire il metttre faux
#startswith
a="image.png"
print(a.startswith("image")) # TRUE
# OPERATEURS MATHEMATIQUES
# + - * /
print(5+3)
print(3-2)
print(4*5)
print(6/2)
# on peut egalement additionner des chaines de carcteres
print("Hello"+ "World")
print("Python" * 3)
# on ne peut pas soustraire ni diviser une chaine de carcters
# % permet de recuperer le reste d'une division
print(10 % 2) # 0
# // donner la reponse en nombre entier peut importe si la reponse est un nmbre decimal
print(10//3) # 3
# ** permet de faire des puissance
print(2**4)
#------------------------------------------------------------
# LES OPERATEURS D ASSIGNATION
# =
i=2
i=i+1
print(i)
# OPERATEURS DE COMPARAISON
#== egal a 
# != different de
# il ya une differnce entre is et ==
# is verifie l adresse en memoire
a=[1,2,3]
b=[1,2,3]
a==b # TRUE uniquement entre -5 et 256
a is b # FALSE
# METTRE EN FORME(concatenation) UNE CHAINE DE CARACTERE POUR INSERER DES VARIABLES
# la methode fstring
prenom= "Paul"
print(f"Bonjour {prenom} !") # Bonjour Paul !
# plus besoin de convertir en chaine de caracteres pour faire des operartions
age=22
prenom="Princesse"
phrase= "Je m'appele {} et J'ai {} ans ".format(prenom,age)
print(phrase) # Je m'appele Princesse et J'ai 22 ans 
#-----------------------------------------------------------------------------
protocole="http://"
nom_du_site="youtube"
extension=".com"
url="{}www.{}.{}".format(protocole,nom_du_site, extension)
print(url)
# L'avantage de rformat par rapport a fstring est qu'on peut definir une variable et l'utiliser plutard ce qui n'est pas le cas de fstring
