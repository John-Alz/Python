# Efectué un programa que digiten n números y diga cuantos pares y cuantos son
# impares y el total de números que escribieron Y LA SUMA DE PARES E IMPARES


num = int(input("La cantidad de numeros que desee: "))
contador = 0 
i = 0 
sumaPar = 0
sumaImpar = 0

while contador < num:
    i += 1
    numeros = int(input("Ingrese el numero #" + str(i) + ": "))
    
    if numeros % 2 == 0:
        sumaPar  += numeros
        print(numeros, " Es par")
    else:
        sumaImpar += numeros
        print(numeros, " Es impar")
    
    contador+=1

print("La suma de los numeros pares es: ", sumaPar)
print("La suma de los numeros impares es: ", sumaImpar)

print("El total de numeros escritos fue: ", num)