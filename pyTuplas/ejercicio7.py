# Dadas dos matrices cuadradas del mismo tamaño, debes realizar la suma de estas matrices y almacenar el resultado en una tercera matriz. 
# La suma debe realizarse elemento por elemento, es decir, la posición (i, j) de la matriz resultante debe 
# contener la suma de los elementos en la posición (i, j) de ambas matrices originales.

filas = int(input("Cuantas filas quieres que tenga la matriz?: "))
columnas = int(input("Cuantas columnas quieres que tenga la matriz?: "))

matrizUno = []

for posicion_fila in range(filas):
    filaUno = []
    for elementos in range(columnas):
        filaUno.append(int(input(f"Ingrese el elemento de la fila {posicion_fila}: ")))
    matrizUno.append(filaUno)
    
matrizDos = []

for posicion_fila in range(filas):
    filaDos = []
    for elementos in range(columnas):
        filaDos.append(int(input(f"Ingrese el elemento de la fila {posicion_fila}: ")))
    matrizDos.append(filaDos)
    

for fila in matrizUno:
    print(fila)
    
print("--------------------------------------------------------------------------------")
        
for fila in matrizDos:
    print(fila)
    

matrizSuma = []

for i in range(filas):
    filaResult = []
    for j in range(columnas):
        suma = matrizUno[i][j] + matrizDos[i][j]
        filaResult.append(suma)
    matrizSuma.append(filaResult)
    
print("--------------------------------------------------------------------------------")

for fila in matrizSuma:
    print(fila)