id(500)
# True sert a singulariser un element, on lappele singletone(pour les chiffres ils se situent entre -5 et 256)
# Pour nommer une varaible il ne faut pas commencer par un chiffre,contenir un tiret(-),pas d'espace 
#et autre caracteres qui ne sont pas numerique,ne pas utilisé un mot reservé par python exp(True)
#-------------------------------------------------------------------------
# Python est un langage dynamique et foretement typé. pourquoi?
#Pas besoin de dire a py quel est le type de la variable(dynamique)
# on peut changer le type d'une variable a tout moment(typé)
#---------------------------------------------------------------------------

a="5"
a=int(a) # conversion dur type chaine de caractere en entier
print(a) 

b="10"
b=int(b)
print(a+b)
#-----------------------------------------------------------------
# afficher le type d'une varaible
a="10"
print(type(a)) # le resultat va donner le type de variable de a (class 'str')

nombre= input("Entrez un nombre:")
print(nombre)
print(type(nombre))
#------------------------------------------------------------------

# exercice (conctenation de plusieurs variables differentes)
d= "j'ai une classe de " + str(30)  + " élèves"
e="10 " + "+ " + "5" + " est egal à " + str(15)
f=10+int("5")
g="l'addition de 10 + 5 est egal à " + str(10+5)
print(d)
print(e)
print(f)
print(g)
#--------------------------------------------------------------------
# on utilise 'input' afin que l'utilisateur puisse saisir de lui meme
h=input("Entrez un nombre :")
print(h)
#--------------------------------------------------------------
# Manipulation des chaines de caractères 2H29





