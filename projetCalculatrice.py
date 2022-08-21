# PROJET/ LA CALCULATRICE
# l utilisateur doit pouvoir entrer deux nombre et on doit ensuite afficher l'addition de ses deux nombres

a = b =""
while not(a.isdigit()and b.isdigit()): # tant que a et b ne sont pas des nombres on boucle
     a =input("Entrez un premier nombre : ")
     b =input("Entrez un deuxieme nombre : ")
     if not (a.isdigit() and b.isdigit()) : 
          print("Veuillez entrer deux nombres valides")
print(f"Le resultat de l'addition de {a} avec {b} est egal à {int(a) + int(b)}")
# il y'a plusieur manieres de faire