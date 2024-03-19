# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
# empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que
# permita almacenar los sueldos de los empleados agrupados en dos listas.

# Imprimir las dos listas de sueldos.

jornadaManiana = int(input("Ingrese los turnos de la maniana: "))
turnosManiana = []


for i in range(jornadaManiana):
    sueldoJm = float(input("Ingrese el sueldo de la jornada maniana: "))
    turnosManiana.append(sueldoJm)
    
print(turnosManiana)

jornadaTarde = int(input("Ingrese los turnos de la maniana: "))
turnosTarde = []


for i in range(jornadaTarde):
    sueldoJt = float(input("Ingrese el sueldo de la jornada tarde: "))
    turnosTarde.append(sueldoJt)
    
print(turnosTarde)