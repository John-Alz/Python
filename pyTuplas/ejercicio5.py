
rows = int(input('Cuantas filas tendra tu matriz: '))
columns = int(input('Cuantas columnas tendra tu matriz: '))

matriz = []
i = 0

suma = 0
promedio = 0

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Ingrese el valor de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)
    for elements in row:
        suma += elements
        i += 1

promedio = suma / i

print(f"La suma de los elementos de la matriz es: {suma}")
print(f"El promedio de los elementos de la matiz es: {promedio}")