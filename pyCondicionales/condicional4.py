
# En una tienda de descuento se efectúa una promoción en la cual 
# se hace un descuento sobre el valor de la compra total según 
# el color de la bolita que el cliente saque al pagar en caja. 
# Si la bolita es de color blanco no se le hará descuento alguno, 
# si es verde se le hará un 10% de descuento, si es amarilla un 25%, 
# si es azul un 50% y si es roja un 100%. 
# Determinar la cantidad final que el cliente deberá pagar 
# por su compra. 
# se sabe que solo hay bolitas de los colores mencionados.

nombre = input("Ingrese su nombre: ")
valorDeCompra = float(input("Ingreses el valor de su compra: "))
bolitaDeColor = input("Escriba el color de bolita para acceder a un descuento (Blanco, verde, amarilla, azul y roja): ")
descuento = 0

if bolitaDeColor == ' ':
    print('Debes escribir el color de una bolita')
elif bolitaDeColor == 'blanco':
    print('No tendras descuento.')
elif bolitaDeColor == 'verde':
    descuento = valorDeCompra * 0.10
elif bolitaDeColor == 'amarillo':
    descuento = valorDeCompra * 0.25
elif bolitaDeColor == 'azul':
    descuento = valorDeCompra * 0.50
elif bolitaDeColor == 'roja':
    descuento = valorDeCompra * 1
else:
    print('Error')

cantidadApagar = valorDeCompra - descuento
print('El cliente ', nombre, ' pagara por su compra un valor de: ', cantidadApagar)