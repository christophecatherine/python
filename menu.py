'''
menu = ("banane","mangue","ananas","papaye","fraise","orange","kiwi","figue")
#print(menu[0])
for i in menu:
    print("index:",menu.index(i),"valeur:",i)
    print("######### Passez votre commande #########")
choix=int(input("Entrez le numrero de votre commande:"))

#check if choix est associé a un index valide
if choix >=0 and choix < len(menu):
    print("vous avez saisi:",choix, " et la commande correspondante est :",menu[choix])
else:
    print("Désolé aucune commande correspondante a ce numero:",choix)

'''



