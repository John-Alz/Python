# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma

lista = [5,60,70,2,4]
sumaElementos = 0

for elemento in lista:
    sumaElementos += elemento

print("La suma de todos los elementos de la lista son: ", sumaElementos)