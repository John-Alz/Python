# ejercicio 4
# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.

elementos = int(input("Ingrese la longitud de sus lista: "))
lista = []
contadorMayoresCien = 0

for i in range(elementos):
    num = int(input("Digite el numero deseado: "))
    lista.append(num)
    if num > 100:
        contadorMayoresCien += 1
        print("Es mayor a 100")
    else: 
        print("ERROR")

print("Lista: ", lista)
print("La cantidad de numeros mayores a cien es: ", contadorMayoresCien)