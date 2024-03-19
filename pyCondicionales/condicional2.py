#  Leer 2 números; si son iguales que los multiplique,
#  si el primero es mayor que el segundo que los reste y si no que los sume.

numeroUno = int(input("Diigte el #1: "))
numeroDos = int(input("Diigte el #2: "))

if numeroUno == numeroDos:
    resultado = numeroUno * numeroDos
elif numeroUno > numeroDos:
    resultado = numeroUno - numeroDos
else:
    resultado = numeroUno + numeroDos


print("El resultado es: " + str(resultado))
