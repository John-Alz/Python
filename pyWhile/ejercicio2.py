# Efectué un programa que imprima una tabla de multiplicar y otro programa que imprima las tablas del uno al 10

mult = int(input("Ingrese un numero: "))
multiplicacion = 0
contador = 0

while contador < 11:
    multiplicacion = mult * contador
    print(mult, " X ", contador, " = ", multiplicacion)
    contador += 1
