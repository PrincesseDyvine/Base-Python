from re import S, T

#a une limite: ne peut pas calculer 1000!
def factoriel(n):
     if(n<2):
          return 1
     else:
          return n*factorielle(n-1)
#pas de limite
def factorielle(n):
     if(n<2):
          return 1
     else:
          p=1
          for i in range(1,n):
               p=p*(n-i)
          q=n*p
          return q

#CALCUL LA RACINE N-IEME D'UN NOMBRE K
def racineNieme(n,k):
     if(n==0):
          return 1
     elif(n==1):
          return k
     else:
          return k**(1/n)

#CALCUL LA COMBINAISON DE k dans n
def combinaison(n,k):
     x=factorielle(n)
     y=factorielle(k)
     p=n-k
     z=factorielle(p)
     q=y*z
     t=x/q
     return t

#CALCUL DE LA SOMME (a+b)^n
def somme(a,b,n):
     t=n+1
     s=0
     for i in range(0,t):
          c=combinaison(n,i)
          x=a**i
          r=n-i
          y=b**r
          z=x*y*c
          s=s+z
     return s

#CALCUL DE LA VALEUR ABSOLUE DE N
def valeurAbsolue(n):
     if n>=0:
          return n
     else:
          return -n


#AFFICHE LES TABLE DE MULTIPLICATION DE N
def tableMutiplication(n):
     print("TABLE DE MULTIPLICATION DE ",n)
     for i in range(0,14):
          y=n*i
          print(n," x ",i," = ",y)
          print("______________________")

#CALCUL APPROXIMATIVE DE expo(x)
def exponentielle(x):
     t=1001
     s=0
     for i in range(0,t):
          a=factorielle(i)
          b=x**i
          c=b/a
          s=s+c
     return s






