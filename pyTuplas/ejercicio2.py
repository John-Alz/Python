# Cargue un MATRIZ de cinco elementos, y al tercero increméntelo en 10 ,
# muestre como quedo

matriz = ()
tamaño = 5
incremento = 0

for i in range(tamaño):
    elemento = int(input("Ingrese el numero: "))
    lista = list(matriz)
    lista.append(elemento)
    matriz = tuple(lista)

incremento = matriz[2] * 10

print("La matriz es: ",matriz)
print("El numero ", matriz[2], " se incremento 10 veces: ", incremento)