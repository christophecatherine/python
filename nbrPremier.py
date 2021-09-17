'''
print("####### Nombre premier dans un intervalle ########")
#TP nombre premier dans un intervalle donné
val_min = int(input("entrez valeur min:"))
val_max = int(input("entrez valeur max: "))
print("les nombres premiers trouvés dans notre intervalle [", val_min, ",", val_max, "] sont:")
for num in range(val_min,val_max): #parcours les nombres de mon intervalle
if num >1:# verifie si num est sup a 1 car tous nombre premiers est sup a 1 si oui


for i in range(2,(num//2)+1): # moitie du nombre augmente de un potentiel diviseur du nombre
# je recherche de poetentiels diviseurs
if (num % i)== 0: # si le reste de la division est 0 alors je sors, je passeau nombre suivant
#jusqu'a epuisement de monintervalle
break
else:
print(num)

'''
