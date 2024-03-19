# Un obrero necesita calcular su salario mensual , el cual se obtiene de la siguiente manera:
# Si su salario mínimo es menor o igual a $737.717 las horas extras se pagaran a $6.453 y si su 
# salario es dos salarios mínimos mayor o igual $1.475.434 las horas extras se pagaran a $12.908.
# capturar por teclado el salario, las horas extras y mostrar el salario neto a pagar al obrero

nombreDelObrero = str(input("Ingrese el nombre del obrero: "))
ingresoMensual = float(input("Ingrese la cantidad de dinero que recibe mensualmente: "))
horasExtrasTrbajadas = int(input("Ingrese la cantidad de horas extras trabajadas: "))


if ingresoMensual <= 737717:
    valorDeHorasExtras = horasExtrasTrbajadas * 6453
elif ingresoMensual >= 1475434:
    valorDeHorasExtras = horasExtrasTrbajadas * 12908
else:
    valorDeHorasExtras = 0
    
salarioNeto = ingresoMensual + valorDeHorasExtras
    
print("El salrio neto que se le pagara a obrero " + str(nombreDelObrero) + " sera de: $" + str(salarioNeto))