# la boucle for servent a :
# parcourir des structure de données
#Syntaxe : for element in liste:
          #print(element)
from ast import While
from curses.ascii import isdigit
from time import time


for i in [0,1,4,7,8]: # 5 iteration
     print(i) # i=0 la premiere valeur de la liste est directement affecté a i
# il va afficher tous les chiffres a l'interieur

for lettre in "Python":
     print(lettre)

# la fonction range permet de creer une liste de nombre avec la taille qu'on lui indique
for i in range(5):
     print("Bonjour")

# la boucle while, s'execute que lorsqu'une condition est vraie
i=0
while i < 5:
     print("Bonjour")
     i+=1
#dans le cas de figure ou on ne sait pas ou s'arreter on peut demander a l'utilisateur a chaque iteration s'il veut continuer ,
continuer="O"
while continuer =="O":
     print("on continue...")
     continuer= input("voulez vous continuer? o/n")
#on peut egalement avoir besoin d'une boucle infini dans le cas ou on veut repeter une opertation toute les dix minutes par exemple
import time
while True:
     print("Sauvegarde en cours...")
     time.sleep(600)

#Modifier l'execution d'une boucle avec "continue","break"
#instruction "continue" lorsqu'elle est utilisée  elle passe directement a la prochaine iteration sans utiliser le reste du code qui se trouve apres
# EXEMPLE(continue),elle n'arrete pas l'iteration mais fait juste passer a la suivante
liste=["1","4","25", " paul"," 3"," pierre"]
for element in liste:
     if element.isdigit:
          continue
     print(element)

# intruction "break"
liste=["1","4","25", " paul"," 3"," pierre"]
for element in liste:
     if element.isdigit:
          break
     print(element)
#--------------------------------------------------------------
# Les comprehension de liste, permet d'iterrer sur une liste et de filtrer les elements grace a des structures conditionelles en une ligne
# EXEMPLE, on veut jute recuperer les elements qui sont superieur a 0
liste = [-5, -4, -3, -2, -1, 0, 1, 3, 4, 5]
nombres_positifs = [i * 2 for i in liste if i > 0]
print(nombres_positifs)

#-------------------------------------------------------------
#EXERCICES,on doit juste recuperer les nombres pairs(avec la comprehension de liste)
nombre[1 ,21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)






