# -De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.

nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))
aniosDeAntiguedad = float(input("Ingrese los anios de antiguedad: "))
aumento = 0
sueldoAPagar = 0

if sueldo < 500 and aniosDeAntiguedad >= 10:
    aumento = sueldo * 0.20
elif sueldo < 500 or aniosDeAntiguedad < 10:
    aumento = sueldo * 0.05
else:
    print("Error")
    
sueldoAPagar = sueldo + aumento;

print("El operario ", nombre, " recibira: $" + str(sueldoAPagar))