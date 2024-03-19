tamanio = 1

tupla = ()

for i in range(tamanio):
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    lista = list(tupla)
    lista.append(dia)
    lista.append(mes)
    lista.append(anio)
    tupla = tuple(lista)

print("Tupla de fecha ingresada:", tupla)