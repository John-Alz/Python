# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10,
# imprimir en pantalla la leyenda "Todos los números son menores a diez".

numUno = int(input("Ingresa el #1: "))
numDos = int(input("Ingresa el #2: "))
numTres = int(input("Ingresa el #3: "))

if numUno < 10 and numDos < 10 and numTres < 10:
    print("Todos los números son menores a diez")
else:
    print("No todos los numeros son menores a 10")