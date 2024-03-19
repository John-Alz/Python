# en python no existe switch se simula asi:
# calcule el índice de masa corporal (IMC) de una persona y le proporcione una clasificación basada en el IMC calculado. 
# El IMC se calcula como el peso (en kilogramos) dividido por el cuadrado de la altura (en metros). 
# La clasificación se determina según la siguiente tabla: 
# IMC menor a 18.5: Bajo peso 
# IMC entre 18.5 y 24.9: Peso normal 
# IMC entre 25 y 29.9: Sobrepeso 
# IMC mayor o igual a 30: Obesidad

menu = """
1-Calcular IMC
2-Salir
"""

print(menu)

op = int(input("Seleccione una opción: "))

if op == 1:
    nombre = input('Ingrese su nombre: ')
    peso = float(input('Ingrese su peso (en kilogramos): '))
    altura = float(input('Ingrese su altura (en metros): '))
    
    imc = peso / altura ** 2

    if imc < 18.5:
        print(str(nombre) + ' tienes bajo peso.')
    elif imc >= 18.5 and imc <= 24.9:
        print(str(nombre) + ' tienes un peso normal.')
    elif imc >= 25 and imc <= 29.9:
        print(str(nombre) + ' tienes un sobre peso.')
    elif imc >= 30:
        print(str(nombre) + ' tienes obesidad.')
    else:
        print('Error')

    print('Tu IMC es igual a: ', imc)

elif op == 2:
    print("Saliendo...")
else:
    print("Opción no válida")
