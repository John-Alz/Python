# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo
# y a este resultado se lo multiplica por el tercero.

numUno = int(input("Ingresa el #1: "))
numDos = int(input("Ingresa el #2: "))
numTres = int(input("Ingresa el #3: "))
suma = 0
multiplicacion = 0

if numUno == numDos and numUno == numTres and numDos == numTres:
    suma = numUno + numDos
    multiplicacion = suma * numTres
    print("Los numeros son iguales")
else:
    print("Los numero no son iguales")

print("La suma es: ", suma)
print("La multiplicacion es: ", multiplicacion)