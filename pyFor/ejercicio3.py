# Programa 3 notas sacar promedio y si promedio >=35 paso sino perdió para n alumnos (ejemplo 3)
# decir cuántos pasaron y cuantos perdieron, y el total de alumnos.
# A y el promedio del curso el promedio de los que pasaron y promedio de los que perdieron.

numeroDeAlumnos = int(input("Ingrese el numero de alumnos: "))

numeroAlumRange = range(0, numeroDeAlumnos)

indice = 0
indiceAprobo = 0
indiceNoAprobo = 0
sumaAprobados = 0
sumaNoAprobados = 0
sumaTodosAlumnos = 0
promedio = 0

for nota in numeroAlumRange:
    indice += 1
    alumno = float(input("Ingrese la nota del alumno #" + str(indice) + ": "))
    print(alumno)
    sumaTodosAlumnos += alumno
    if alumno >= 3.5:
        indiceAprobo += 1
        sumaAprobados += alumno
        print("Aprobo")
        
    else:
        indiceNoAprobo += 1
        sumaNoAprobados += alumno
        print("No aprobo")
        

print("La cantidad de alumnos totales es: " + str(numeroDeAlumnos))
print("La cantidad de alumnos que aprobaron: " + str(indiceAprobo))
print("La cantidad de alumnos que NO aprobaron: " + str(indiceNoAprobo))

if indiceAprobo > 0:
    promedio = sumaAprobados / indiceAprobo
    print("El promedio de alumnos que aprobaron fue: ", promedio)
else:
    print('Error')
    

if indiceNoAprobo > 0:
    promedio = sumaNoAprobados / indiceNoAprobo
    print("El promedio de alumnos que NO aprobaron fue: ", promedio)
else:
    print("Error")
    
if indice > 0:
    promedio = sumaTodosAlumnos / indice
    print("El promedio de todos los alumnos fue: ", promedio)
else:
    print("Error")
