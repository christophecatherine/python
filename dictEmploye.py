'''
import os
reponse = 'y' #yes
index=1
employes={} #contient la liste de nos employes

print("*** Enregistrement employé ***")
while reponse =='y':
os.system('cls') #clear ecran
print("*** saisir infos employé *** ",index)
nom = input("Nom: ")
prenom= input("Prenom: ")
age = input("Age: ")
sexe = input("Genre: ")
salaire= input(" Salaire: ")
role = input("Role: ")
#enregistrement infos dans le dictionnaire
employes.update({index:{"Nom":nom,"Prenom":prenom,"Age":age,"Sexe":sexe,"Salaire":salaire,"Role":role}})
index+=1
reponse = input("voulez vous continuez ?")

print("*** Liste des employés *** ")
for em in employes.items():
print(em)

'''