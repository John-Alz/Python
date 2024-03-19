myStr = "hello world"
print (dir(myStr)) # muestra los metodos de string
print (myStr.upper()) 

print (myStr.lower())
print (myStr.swapcase())
print (myStr.capitalize())

print("-------------------------------")

# Metodos del string
longitud = len(myStr)
print("La cadena ", myStr, " tiene una longitud de: ", longitud, " caracteres.")

print("-------------------------------")

reemplazar = myStr.replace("hello", "Hi")
print("String antiguo: ", myStr)
print("String nuevo: ", reemplazar)

print("-------------------------------")

strDivido = myStr.split(" ")
print("String base: ", myStr)
print("String dividido: ", strDivido)