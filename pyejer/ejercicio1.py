# en python no existe switch se simula asi:
menu ="""
1-M_numero
2-M_texto
3-Msigno
4-Mnumero_usado
"""
print(menu)
op =int(input("toma un caso"))
if op == 1:
    print(545)
elif op == 2:
    print("hola mundo")
elif op == 3:
    print("?")
elif op == 4:
    print(op)
else:
    print(" tecla errada")