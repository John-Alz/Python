numero = float(input('Ingresa un número. 0 para terminar: '))
acumula=0
while(numero != 0):
    if (numero == 0):
        break
    else:
     acumula = acumula+numero

numero = float(input('Ingresa un número. 0 para terminar: '))
    

print (" la suma de los numeros es ", acumula)
print('Fin del programa.')

control = "no"
acumula=0
while(control != "si"):
     numero = float(input('Ingresa un número. '))
     acumula = acumula+numero
     control = str(input('desea salir escriba si. '))


print (" la suma de los numeros es ", acumula)
print('Fin del programa.')