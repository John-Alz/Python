# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))

if dia == 25 and mes == 12:
    print("La fecha corresponde a navidad")
else:
    print("La fecha no corresponde a navidad")