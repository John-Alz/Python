# agregar por teclado y almacenar en una lista las alturas de 5 personas
# (valores float)
# Obtener el promedio de las mismas. Contar cuántas personas son más altas
# que el promedio y cuántas más bajas.

alturas = int(input("Ingrese la cantidad de alturas: "))
lista = []
promedioAlturas = 0
masAltasPromedio = 0
masBajasPromedio = 0

for i in range(alturas):
    altura = float(input("Ingrese la altura: "))
    lista.append(altura)

promedioAlturas = sum(lista) / len(lista)

print("Promedio alturas: ", promedioAlturas)

for element in lista:
    if element > promedioAlturas:
        masAltasPromedio += 1
    else:
        masBajasPromedio += 1

print("La cantidad de personas mas altas que el promedio es: ", masAltasPromedio)
print("La cantidad de personas mas bajas que el promedio es: ", masBajasPromedio)