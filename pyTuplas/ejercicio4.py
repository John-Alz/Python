# Cargué dos matrices, efectué la suma de estas en una tercera (ej. La
# posición 1,1 de un matriz sumarla con la posición 1,1 de la otra y dejarla en
# la posición 1,1 de resultado)

rows = int(input("Cuantas filas quieres para tu matriz?: "))
columns = int(input("Cuantas columnas quieres para tu matriz?: "))

matriz = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Ingrese el valor de la fila {row_position}: ")))
    matriz.append(row)

matrizTwo = []

for row_position_two in range(rows):
    rowTwo = []
    for elementTwo in range(columns):
        rowTwo.append(int(input(f"Ingrese el valor de la fila {row_position_two}: ")))
    matrizTwo.append(rowTwo)
    
print("------------------------------------------------------------------------------")

for row in matriz:
     print(row)

print("------------------------------------------------------------------------------")

for row in matrizTwo:
     print(row)
     

matriz_sum = []
for i in range(rows):
    result = []
    for j in range(columns):
        suma = matriz[i][j] + matrizTwo[i][j]
        result.append(suma)
    matriz_sum.append(result)

print("------------------------------------------------------------------------------")

for row in matriz_sum:
     print(row)