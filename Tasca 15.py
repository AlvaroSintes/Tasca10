def longitud(a):
    long = 0
    for i in a:
        long += 1
    return long

# Ús de la funció
x = "Cal Dimoni"
print("La longitud de la cadena donada és: ", longitud(x))

y = [3, 4, 5, "a", "hola"]
print("La longitud de la llista donada és: ", longitud(y))

z = (3, 5, 7, 9, 10)
print("La longitud de la tupla donada és: ", longitud(z))

w = {3, 5, 7, 9, 10}
print("La longitud del conjunt donat és: ", longitud(w))