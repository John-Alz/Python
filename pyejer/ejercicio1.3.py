menuUno = """
1-Calcular nota
2-Salir
"""
print(menuUno)

opUno = int(input("Selecciones una opcion: "))

if opUno == 1:
    nombre = input("Ingrese su nombre: ")
    
    menuDos = """
    1-Si es menor o igual a 3.4
    2-Si es menor o igual a 4.0
    3-Si es menor o igual a 4.6
    4-Si igual a 5.0
    """
    
    print(menuDos)

    opDos = int(input("Seleccione una opción: ")) 
    
    if opDos == 1:
        mensaje = "Baja."
    elif opDos == 2:
        mensaje = "Basica."
    elif opDos == 3:
        mensaje = "Alta."
    elif opDos == 4:
        mensaje = "Superior."
    else:
        print("ERROR")
        
    print('La nota del estudiante ', nombre, ' es: ', mensaje) 

elif opUno == 2:
    print("Saliendo...")
else:
    print("Opcion no valida")