def remplirUneListe(Liste):
     taille_liste=int(input("donner le nombre des employés :"))
     for i in range(0,taille_liste):
          print("EMPLOYE NUMERO :",i)
          x = int(input("donner son salaire :"))
          Liste.append(x)

def calculSommeListe(Liste):
     taille=len(Liste)
     somme=0
     for i in range(0,taille):
          xi=Liste[i]
          somme=somme+xi
     return somme

def calculSalaireMoyen(Liste):
     qq=0
     taille=len(Liste)
     somm = 0
     for i in range(0,taille):
          somm=somm+Liste[i]
     sal_moy=somm/taille
     return sal_moy

def calculVariance(Liste):
     sal_moy=calculSalaireMoyen(Liste)
     taille=len(Liste)
     for i in range(0,taille):
          p=Liste[i]
          q=(p-sal_moy)**2
     variances=(q/taille)
     return variances

def calculEcartType(Liste):
     o=calculVariance(Liste)
     op=o**(1/2)
     return op

def calculSalaireMedian(Liste):
     minimum=min(Liste)
     maximum=max(Liste)
     salaire_median=(minimum+maximum)/2
     return salaire_median

def ListeEmployeeAvecSalaireSuperieureAuSalaireMoyen(Liste):
     Liste_Employee_Sup_Moy = []
     salaire_moy=calculSalaireMoyen(Liste)
     taille=len(Liste)
     for i in range(0,taille):
          s=Liste[i]
          if(s>salaire_moy):
               Liste_Employee_Sup_Moy.append(i)
     return Liste_Employee_Sup_Moy

##################EXECUTION################
Employee = []
remplirUneListe(Employee)
v=calculVariance(Employee)
e=calculEcartType(Employee)
s=calculSalaireMoyen(Employee)
som=calculSommeListe(Employee)
m=calculSalaireMedian(Employee)
print("---------------------------------------------------------------------")
l=ListeEmployeeAvecSalaireSuperieureAuSalaireMoyen(Employee)
pourcentage=((len(l))/(len(Employee)))*100

print("VOICI NOTRE LISTE :", Employee)
print("SALAIRE MAX :",max(Employee))
print("SALAIRE MIN :", min(Employee))
print("SALAIRE MOYEN: ",s)
print("SALAIRE MEDIAN: ", m)
print("MASSE SALARIALE: ",som)
print("VARIANCE DES SALAIRE: ",v)
print("ECART TYPE DES SALAIRE: ",e)
print("EMPLOYEE AVEC SALAIRE SUP AU SALAIRE MOY :",l," Soit : ",pourcentage,"%")