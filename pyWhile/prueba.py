from random import randint

def main():
    n = int(input("INgrese la cantidad de elementos de la lista: "))
    
    lista = [x+1 for x in range(n)]
    
    print(lista)

if __name__ == "__main__":
    main()