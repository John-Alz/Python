menuUno = """
1-Calcular nota
2-Salir
"""

print(menuUno)

opUno = int(input("Selecciones una opcion: "))

if opUno == 1:
    numeroUno = int(input("Diigte el #1: "))
    numeroDos = int(input("Diigte el #2: "))

    if numeroUno == numeroDos:
        resultado = numeroUno * numeroDos
    elif numeroUno > numeroDos:
        resultado = numeroUno - numeroDos
    else:
        resultado = numeroUno + numeroDos


print("El resultado es: " + str(resultado))