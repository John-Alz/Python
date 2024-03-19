# obtine numeros random
#import random as r
import random 
#
randomNum = random.randint(0,20)
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un numero al azar de 0 a 20: "))

if numero == randomNum:
    print("🎁🎁✨✨¡Ganaste la rifa!✨✨🎁🎁")
else:
    print("¡No adivinaste el numero!😥, sigue intentanto 😄")

print("El numero ganador es:", randomNum)
print("Tu numero es: ", numero)