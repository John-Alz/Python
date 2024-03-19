# Efectué un programa que imprima una tabla de multiplicar y otro programa que imprima las tablas del uno al 10

mult = int(input("Ingrese un numero: "))
tablas = range(1, 11)
multiplicacion = 0
for tabla in tablas:
    multiplicacion = mult * tabla
    print(mult, " X ", tabla, " = ", multiplicacion)