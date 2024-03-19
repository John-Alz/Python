tupla = ("juan", "pedro", "manuel", "Jose", "John")
print("tupla original: ", tupla)
print("longitud de tupla original: ", len(tupla))
lista = list(tupla)
print("lista original: ", lista)
lista.append("Smith")
print("liat modificada: ", lista)
tupla = tuple(lista)

print("tupla modificada: ", tupla)
print("longitud de tupla modificada: ", len(tupla))
print(type(tupla))

for i in range(len(tupla)):
    print(tupla[i])
    print(i)