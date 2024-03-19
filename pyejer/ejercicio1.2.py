menuUno = """
1-Calcular utilidad
2-Salir
"""

print(menuUno)

opUno = int(input("Seleccione una opción: "))

if opUno == 1:
    nombre = input("Ingrese su nombre: ")
    valorSalarioMensual = float(input("Ingreses el valor de su salario mensual: $"))
    utilidad = 0

    menuDos = """
    1-Menos de 1 año
    2-1 año o más y menos de 2 años
    3-2 años o más y menos de 5
    4-5 años o más y menos de 10 años
    5-10 años o más
    """

    print(menuDos)

    opDos = int(input("Seleccione una opción: ")) 
    if opDos == 1:
       utilidad = valorSalarioMensual * 0.05
    elif opDos == 2:
       utilidad = valorSalarioMensual * 0.07
    elif opDos == 3:
       utilidad = valorSalarioMensual * 0.10
    elif opDos == 4:
       utilidad = valorSalarioMensual * 0.15
    elif opDos == 5:
       utilidad = valorSalarioMensual * 0.20
    else:
        print('Error')
        
    print('El empleado ', nombre, ' tendra una utilidad de: $', utilidad)

elif opUno == 2:
    print("Saliendo...")
else:
    print("Opcion no valida")