lista1=[]
lista2=[1,2,3,4,5]
lista3=[6.3,7.4,8.2,9.3,10.9]
lista4=["Mario", "Pedro", "Dario"]
lista5=[1,2,3,4,5, "veronica"]
print(type(lista1))

print(lista2[3])
print(len(lista2))
print(lista2)
lista2[2]=7
print(lista2)

lista1.append(10)
lista1.append(1)
lista1.append(11)
print(lista1)
# pop elimina el ultimo elemento de la lista
lista1.pop()
print(lista1)

print(lista2)
# sort ordena la lista
lista2.sort()
print(lista2)