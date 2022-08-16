# DES MODULES, un fichier python qui conyient des fonctions qu'on peut utiliser
# random et os, afin de generer des nombres aleatoires
from ast import Import
import random
r= random.randint(0,2) # generer aleatoirement un nombre en entrant deux arguments
print(r)

# fonction "uniform", elle retourne les nombres decimaux
r=random.uniform(0,1)
print(r)
#
# fonction randrange, celle ci marche juste avec un seul argument,et on peut specifier un pat(par exemple un pas de 10)
r=random.randrange(999)
print(r)
#EXEMPLE 2
r=random.randrange(0,101,10)
print(r)

# Le module "OS", on l'utilise pour creer et supprimer des dossiers
# exemple
import os 
chemin ="C:/Users/princ/Desktop"
dossier = os.path.join(chemin,"dossier ")
print(dossier)
os.makedirs(dossier) # avec makedirs on ne peut pas creer deux fois le meme dossier
# EXEMPLE 2 
chemin ="C:/Users/princ/Desktop"
dossier = os.path.join(chemin,"dossier ")
if not os.path.exists(dossier): # on ajoute une structure conditionnelle afin que si le dossier n'esxiste pas il met false et on peut le creer , pour ne pas avoir d'erreur
     os.makedirs(dossier) 
print(dossier)
#----------------------------------------------------
# La fonction "removedirs", suppprimer un dossier
chemin ="C:/Users/princ/Desktop"
dossier = os.path.join(chemin,"dossier ")
os.removedirs(dossier)  # si le dossier n'existe pas et on essaye de le supprimer python va indiquer une erreur
# EXEMPLE 2 , pour ne pas avoir d'erreur lorsque le dossier n'esxiste pas
chemin ="C:/Users/princ/Desktop"
dossier = os.path.join(chemin,"dossier ")
if os.path.exists(dossier): # exist,nous permet de voi si un dossier exist
     os.removedirs(dossier)
#-----------------------------------------------------------------------------------
#QUELQUES FONCTIONS
# La fonction "dir", qui permet d'afficher toute les fonction squ'on peut utilser à l'interieur du module
# EXEMPLE
import random 
print(dir(random))
#------------------------------------
# La fonction "help", on n'est pas obligé d'utiliser le print,il va juste afficher l'aide de la fonction voulue(les parametres que prend cette fonction)
#EXEMPLE
help(random.randint)
#-----------------------------------------
#La fonction pprint, elle va nous permettre d'afficher les resultats de la fonction dir d'une meilleure façon
#EXEMPLE
import random
from pprint import pprint
pprint(dir(random))
#------------------------------------------------------------
# LES OBJECTS "CALLABLE" (appelable), elle va nous permettre de savoir si on peur appeler un object
# EXEMPLE
import pprint
callable(pprint)
print(callable(pprint)) # FALSE
# EXEMPLE 2
from pprint import pprint
print(callable(pprint)) # TRUE
# EXEMPLE 3
import os 
from pprint import pprint
print(callable(os.name)) # pour verifier si "os.nam" est appelable: False
#----------
print(os.name)
