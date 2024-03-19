# Efectué un programa que digiten n números y diga cuantos pares y cuantos son
# impares y el total de números que escribieron Y LA SUMA DE PARES E IMPARES

num = int(input("La cantidad de numeros que desee: "))
numbers = range(1, (num))
sum = 0

for number in numbers:
    if number % 2 == 0:
        print(number, " Es par")
    else:
        print(number, " Es impar")
    sum += number

print("LA suma de los numeros es: ", sum)

print("El total de numeros escritos fue: ", num)