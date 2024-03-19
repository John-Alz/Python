# Hacer un programa que me capture por teclado un valor en pesos colombianos y me los convierta a 
# dólares y euros.

pesosColombianos = int(input("Ingrese la cantidad de pesos colombianos que desea convertir a dolares o a euros: "))
conversionDolares = round(pesosColombianos / 3961, 2)
conversionEuros = round(pesosColombianos / 4298, 2)
print("La cantidad de " + str(pesosColombianos) + " COP, equivale a " + str(conversionDolares) + "$")
print("La cantidad de " + str(pesosColombianos) + " COP, equivale a " + str(conversionEuros) + "€")