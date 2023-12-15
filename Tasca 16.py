def es_vocal(a): # Defineix la funcio 
    if a in l: # Verifica si el caracter 'a' es present a la llista 'l'
        return True # Si el caracter es una vocal imprimira 'True'
    else:  # Si el caràcter no és a la llista, vol dir que no és una vocal.
        return False # Torna 'False' en aquest cas

a = input("Introdueixi un caracter: ")

l = ('a','e','i','o','u')

if es_vocal(a):
    print("Vertader")
else:
    print("False")
