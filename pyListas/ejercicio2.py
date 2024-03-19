# ejercicio 2
# Definir una lista por asignación que almacene los nombres de los 
# primeros cuatro meses de año. Mostrar el primer y último elemento de la lista solamente.
numeroDeMeses = int(input("Digite el numero de meses: "))
contador = 0
lista = []

while contador < numeroDeMeses:
    mes = input("Digite el mes que dese: ")
    lista.append(mes)
    
    contador += 1
    
print(lista)
print("Primer elemento de la lista: ", lista[0])
print("Ultimo elemento de la lista: ", lista[-1])