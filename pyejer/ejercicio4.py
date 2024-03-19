import math
 
print(math.ceil(1.001))    # returns 2
print(math.floor(1.001))   # returns 1
print(math.factorial(10))  # returns 3628800
print(math.gcd(10,125))    # returns 5
 
print(math.trunc(1.001))   # returns 1
print(math.trunc(1.999))   # returns 1

# raiz cuadrada
num = 9
resu = math.sqrt(num)
print(resu)

print("-------------------------------")

numeroPi = math.pi
print("El numero PI es: ", numeroPi)

print("-------------------------------")

numeroUno = 3
numeroDos = 2
potencia = math.pow(3, 2)
print("La potencia cuadrada de ", numeroUno, " es: ", potencia)

print("-------------------------------")

numero = 4
valorAbsoluto = math.fabs(numero)
print("El valor absoluto de ", numero, " es: ", valorAbsoluto)