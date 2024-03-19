# Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos.

sueldos = int(input("Ingrese la cantidad de sueldoss: "))
lista = []
promedioSueldo = 0
sumaSueldos = 0

for i in range(sueldos):
    sueldo = float(input("Ingrese un sueldo: "))
    lista.append(sueldos)
    
    sumaSueldos += sueldo
    
promedioSueldo = sumaSueldos / len(lista)
print("El promedio de sueldo de los ", sueldos, " operarios es: ", promedioSueldo)