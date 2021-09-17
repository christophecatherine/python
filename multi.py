'''
n = 5
n = int(input("taper la valeur de n : "))
print("Voici la table de",n)
for i in range(1,11):
    print(i,"x",n,"=",i*n)

'''

'''
#TP multiplication
print("####### votre table multiplication ########")

my_num = int(input("Saisir un nombre: "))
print("Table de multiplication de: ", my_num)
for i in range(1,11):
c = i*my_num

print(i,"x",my_num,"=",c)

'''
#exemple de break:
'''
print("####### votre table multiplication cas BREAK ########")
my_num = int(input("Saisir un nombre: "))
print("Table de multiplication de: ", my_num)
for i in range(1,11):
if(i==5):
break
c = i*my_num

print(i,"x",my_num,"=",c)
'''

#exemple Continue
'''
print("####### votre table multiplication cas Continue ########")
my_num = int(input("Saisir un nombre: "))
print("Table de multiplication de: ", my_num)
for i in range(1,11):
if(i==5):
continue
c = i*my_num

print(i,"x",my_num,"=",c)

'''
'''

#exemple avec un pas
#exemple Continue
print("####### votre table multiplication avec le pas definit ########")
my_num = int(input("Saisir un nombre: "))
print("Table de multiplication de: ", my_num)
for i in range(1,11,2):
if(i==5):
continue #remplacer break un autre rendu
c = i*my_num

print(i,"x",my_num,"=",c)

'''

