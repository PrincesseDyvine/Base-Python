# STRUCTURES CONDITIONNELLES
# 1ere conditions 
#-------------------------------------------------------
# if
age= 20
if age>= 18:
     print("vous etes majeur !")
#----------------------------------------------------------

# elif , il est utilisable que s'il y'a un if au prealable
age= 15
if age>= 18:
     print("vous etes majeur !")
elif age < 18:
     print("Vous etes mineur")
#-----------------------------------------------
# else, permet d'executer un bloc de code au cas les differentes conditions ennoncé au prealable ne sont pas respectées
utilisateur = "Paul"
if utilisateur =="admin":
     print("Accès autorisé")
elif utilisateur == "root":
     print("Acces autorisé !")
else:
     print("Accès refusé...")

# autre exemple
age = 20
majeur = True if age >= 18 else False # autre maniere de structurer, mais ne marche qu'avec if et else
#-------------------------------------------------------------------------
# OPERATEURS LOGIQUES (and,or,not)
# and, il ne marche que si les deux composants sont vrais ou alors on remplace la condition qui n'est pas vrai par un or
utilisateur="admin"
mot_de_passe="admin"
if utilisateur == "admin" and mot_de_passe =="admin":
     print("Accèes autorisé") 
# il faut savoir que python verifie premierement la condition ou il y'a "and" avant les autres condition comme "or"
#True and True= True       #True OR True= True
#True and False= False     #True OR FALSE= TRUE
#False and True= Fasle     #FALSE OR True= True
#FALSE and FALSE= FALSE    #FALSE OR FALSE= FALSE

# On peut donner la priorité a "or" en ajoutant les parenthese

# NOT, il va simplement retouner l'inverse de ce qu'on lui donne
utilisateur ="root"
if not utilisateur =="admin":
     print("Accès refusé")

     