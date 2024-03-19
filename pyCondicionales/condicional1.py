# 1.) se lee un nota según el siguiente cuadro asignarle el mensaje correspondiente
# Si es menor o igual a 3.4 es bajo
# Si es menor o igual a 4.0 es básico
# Si es menor o igual a 4.6 es alto
# Si es menor o igual a 5.0 es superior

nota = float(input("Digite su nota: "))

if nota <= 3.4:
    print("Es bajo")
elif nota <= 4.0:
    print("Es basico")
elif nota <= 4.6:
    print("Es alto")
elif nota <= 5.0:
    print("Es superior")
else:
    print("Error")