# En Mega Plaza de Madrid se hace un 25% de descuento a los clientes cuya compra supere los $ 
# 70000 ¿Cuál será la cantidad que pagara una persona por su compra?

nommbreDelCliente = str(input("Ingrese el nombre del cliente: "))
valorDeCompra = int(input("Ingrese el valor de su compra: "))
descuentoCompra = valorDeCompra * 0.25

if valorDeCompra > 70000:
    valorFinalDeCompra = valorDeCompra - descuentoCompra
    print("el cliente " + str(nommbreDelCliente) + " pagara por su compra el total de: $" + str(valorFinalDeCompra))
else:
    print("el cliente " + str(nommbreDelCliente) + " no tiene descuento en su compra")