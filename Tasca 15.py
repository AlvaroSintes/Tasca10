def longitud(a): # Defineix la funció anomenada longitud que pren un argument 'a'.
    long = 0  # Inicialitza una variable 'long' a 0 per comptabilitzar la longitud de la seqüència.
    for i in a: # Itera sobre els elements de la seqüència 'a'.
        long += 1 # Incrementa el valor de 'long' per cada element a la seqüència, comptant així la longitud.
    return long  # Retorna el valor de 'long' com a resultat de la funció.

# Ús de la funció
x = "Cal Dimoni" # Assigna la cadena "Cal Dimoni" a la variable 'x'.
print("La longitud de la cadena donada és: ", longitud(x)) # Crida a la funció 'longitud(x)' per obtenir la longitud de la cadena i la imprimeix.

y = [3, 4, 5, "a", "hola"] # Asigna la llista en la variable 'y'.
print("La longitud de la llista donada és: ", longitud(y)) # Crida a la funció 'longitud(y)' per obtenir la longitud de la llista i la imprimeix.

z = (3, 5, 7, 9, 10) # Asigna la tuple a la variable 'z'.
print("La longitud de la tupla donada és: ", longitud(z)) # Crida a la funció 'longitud(z)' per obtenir la longitud de la tupla i la imprimeix.

w = {3, 5, 7, 9, 10} # Asigna el conjunt a la variable 'w'.
print("La longitud del conjunt donat és: ", longitud(w)) # Crida a la funció 'longitud(w)' per obtenir la longitud del conjunt i la imprimeix.