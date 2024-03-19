usuarios = [[],[]]

tamanio = int(input("Ingrese la canatidad de personas a las cuales les pedira informacion: "))

for i in  range(tamanio):
    nombre = input("Ingrese el nombre: ")
    id = int(input("Ingrese el numero de identificacion: "))
    
    usuarios[0].append(nombre)
    usuarios[1].append(id)
    

for i in range(tamanio):
    print("Nombre ", usuarios[0][i])
    print("id ", usuarios[1][i])
    
for row in usuarios:
    print(row)