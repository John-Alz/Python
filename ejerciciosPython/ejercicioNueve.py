# Si un empleado recibe un ingreso mensual, pero el empleador le dice que el primer mes le incrementa 
# 30%, el segundo mes 40% y tercer mes 35%. Se debe capturar por teclado el ingreso del empleado y 
# el mes, postreramente se debe mostrar el valor neto del ingreso mensual del empleado.

nombreDelEmpleado = str(input("Ingrese el nombre del empleado: "))
ingresoMensual = float(input("Ingrese la catidad de dinero que recibe mensualmente: "))
mes = int(input("Ingrese el número del mes (1 para enero, 2 para febrero, 2 para marzo.): "))

aumentoMesUno = ingresoMensual * 0.30
aumentoMesTres = ingresoMensual * 0.35

if mes == 1:
    salarioNeto = ingresoMensual + aumentoMesUno
elif mes == 2:
    salarioNeto = ingresoMensual * 1.40
elif mes == 3:
    salarioNeto = ingresoMensual + aumentoMesTres
    
print("El salario neto del empleado para el mes de " + str(mes) + " es: $" + str(salarioNeto))