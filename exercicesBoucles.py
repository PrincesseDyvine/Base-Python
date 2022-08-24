#EXERCICES,on doit juste recuperer les nombres pairs(avec la comprehension de liste)
nombres=[1 ,21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

# ---------------------------------------------------------
#EXEMPLE, on veut verifier si i est plus grand ou egal a 0
nombres=range(-10,10)
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres)

#------------------------------------------------------------
# EXEMPLE 3, on veut modifier la liste
nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]
print(nombres_doubles)

#
#EXEMPLE 4,
nombres = range(10)
nombres_inverses = [ i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses)

#
#EXEMPLE 5, afficher dix utilisateurs
for i in range(10): # ou (1,11)
     print(f"Utilisateur {i+1}")

#
#EXEMPLE, afficher un mot a l'envers
mot = "python"
for l in reversed(mot):
     print(l)

#
#EXEMPLE, sortir d'une boucle while
continuer = "o"
while continuer =="o":
     print("On continue!")
     continuer = input("Voulez vous continuer ? o/n ")




