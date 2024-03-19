# Pida datos para grabar dos matrices, sume el 3 elemento de cada matriz y
# muéstrelo
rows = int(input("Cauntas filas quieres?: "))
columns = int(input("Cauntas columnas quieres?: "))

matrix = []
suma = 0

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Escribe el valor de la fila {row_position}: ")))
    matrix.append(row)

for row in matrix:
    print(row)
    
suma = matrix[0][2] + matrix[1][2]
print("La suma del 3er elemento de cada matrix es: ", suma)