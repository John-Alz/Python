mat = [[]]

i = 0

r = 0
c = 0

while r>20 or r<1 or c>20 or c<1:
    f = int(input("Cantidad de filas"))
    c = int(input("Cantidad de columnas"))
    
for x in range(r):
    if (x+1) != f:
        mat.append([])
        
        for y in range(c):
            if i == 0:
                mat[x].append(i)
                i=1
            else:
                mat[x].append(i)
                i=0

for x in range(r):
    print(mat[x])
    x+=1

mat = [[]]

i = 1

r = 0
c = 0
f = int(input("Cantidad de filas"))
c = int(input("Cantidad de columnas"))
    

for i in range(r):
    mat.append([])
    for j in range(c):
        value = float(input("f {}, c {} : ".format(i+1, j+1)))
        mat[i].append(value)
print()

for f in mat:
    print("[", end=" ")
    for element in f:
        print("{:8.2f}".format(element), end = " ")
print()