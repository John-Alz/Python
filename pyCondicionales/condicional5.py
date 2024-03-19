anio = int(input('Ingrese el anio: '))
    
if anio % 4 == 0 and anio % 100 != 0:
    print('El anio ' + str(anio) + ' es anio viciesto')
else:
    print('El anio '+ str(anio) + ' no es viciesto')