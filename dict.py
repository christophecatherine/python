'''

#Dict explication
dict = {}
dict= { 'Nom': "Tom", "Age": 18, "Villes": ["Paris","Lyon","Marseille"]}
print('*** show type ***')
print(type(dict))
print('*** add elt in my dict ***')
dict['pays']= "France"
dict.update({1:"hello",2:"world"})
print('*** show dict after add elt ***')
print(dict)
dict.pop(1)
print('*** after pop ***')
print(dict)
elt=dict.get("Nom")
print(elt)


print('*** parcours dict ***')
for el in dict:
print(dict[el])

'''