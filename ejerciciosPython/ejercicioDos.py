# Calcular el nuevo salario de un empleado si obtuvo un incremento del 10 % sobre su salario actual y un 
# descuento de 3.5% por aportes obligatorios a parafiscales que corresponden al empleador en beneficio 
# de sus trabajadores.

salarioActual = float(input("Digite su salario actual: "))
aumentoSalario = salarioActual * 0.10
descuento = salarioActual * 0.035
nuevoSalario = salarioActual + aumentoSalario - descuento
print("El aumento de salario del empleado sera de " + str(aumentoSalario) + "$")
print("El descuento de aportes parafiscales del empleado sera de " + str(descuento) + "$")
print("El nuevo salario del empleado sera de " + str(nuevoSalario) + "$")