# Si un aprendiz desea saber cuál será su calificación final en programación de software. Dicha 
# calificación se compone de cuatro notas.
nombreAlumno = str(input("Ingrese su nombre: "))
notaUno = float(input("Ingrese la nota #1: "))
notaDos = float(input("Ingrese la nota #2: "))
notaTres = float(input("Ingrese la nota #3: "))
notaCuatro = float(input("Ingrese la nota #4: "))

sumatoriaNotas = notaUno + notaDos + notaTres + notaCuatro
calificacionFinal = sumatoriaNotas / 4

print("La calificacion final del alumno " + str(nombreAlumno) + " es: " + str(calificacionFinal))