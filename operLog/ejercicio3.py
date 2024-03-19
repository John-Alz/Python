# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10,
# imprimir en pantalla la leyenda "Alguno de los números es menor a diez"

numUno = int(input("Ingresa el #1: "))
numDos = int(input("Ingresa el #2: "))
numTres = int(input("Ingresa el #3: "))

if numUno < 10 or numDos < 10 or numTres < 10:
    print("Alguno de los números es menor a diez")
else:
    print("Todos los numeros son mayores a 10")