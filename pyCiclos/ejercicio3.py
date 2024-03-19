# Programa 3 notas sacar promedio y si promedio >=35 paso sino perdió para n alumnos (ejemplo 3)
# decir cuántos pasaron y cuantos perdieron, y el total de alumnos.
# A y el promedio del curso el promedio de los que pasaron y promedio de los que perdieron.

alumnoUno = float(input("Ingrese la nota del alumno #1: "))
# alumnoDos = float(input("Ingrese la nota del alumno #2: "))
# alumnoTres = float(input("Ingrese la nota del alumno #3: "))
# alumnoCuatro = float(input("Ingrese la nota del alumno #4: "))
# alumnoCinco = float(input("Ingrese la nota del alumno #5: "))
# alumnoSeies = float(input("Ingrese la nota del alumno #6: "))

indice = 0

for nota in range(1, ):
    indice += 1
    alumnoUno = float(input("Ingrese la nota del alumno #" + str(indice) + ": "))
    print(alumnoUno)
    if alumnoUno >= 3.5:
        print("Aprobo")
    else:
        print("No aprobo")
