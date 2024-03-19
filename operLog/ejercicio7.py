# Escribe un programa que solicite al usuario dos números enteros. Luego, el programa debe imprimir si ambos números son pares,
# si alguno de los números es par, 
# o si ninguno de los números es par.

numUno = int(input("Ingresa el #1: "))
numDos = int(input("Ingresa el #2: "))

if numUno % 2 == 0 and numDos % 2 == 0:
    print("Los dos numeros son pares.")
elif numUno % 2 == 0 or numDos % 2 == 0:
    print("Alguno de los numeros es par.")
else:
    print("Ningun numero es par.")