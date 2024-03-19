# Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades 
# si este se le asigna como un porcentaje de su salario mensual que depende de su 
# antigüedad en la empresa de acuerdo con la sig. tabla:
# Tiempo Utilidad
# Menos de 1 año 5 % del salario
# 1 año o más y menos de 2 años 7% del salario
# 2 años o más y menos de 5 años 10% del salario
# 5 años o más y menos de 10 años 15% del salario
# 10 años o más 20% del salario


nombre = input("Ingrese su nombre: ")
valorSalarioMensual = float(input("Ingreses el valor de su salario mensual: $"))
aniosDeAntiguedad = float(input('Ingrese los anios de antiguedad en la empresa: '))
utilidad = 0

if aniosDeAntiguedad < 1:
    utilidad = valorSalarioMensual * 0.05
elif aniosDeAntiguedad >= 1 and aniosDeAntiguedad < 2:
    utilidad = valorSalarioMensual * 0.07
elif aniosDeAntiguedad >= 2 and aniosDeAntiguedad < 5:
    utilidad = valorSalarioMensual * 0.10
elif aniosDeAntiguedad >= 5 and aniosDeAntiguedad < 10:
    utilidad = valorSalarioMensual * 0.15
elif aniosDeAntiguedad >= 10:
    utilidad = valorSalarioMensual * 0.20
else:
    print('Error')
    
print('El empleado ', nombre, ' tendra una utilidad de: $', utilidad)