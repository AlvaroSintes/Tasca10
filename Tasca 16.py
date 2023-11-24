def es_vocal(a):
    if a in l:
        return True
    else:
        return False

a = input("Introdueixi un caracter: ")

l = ('a','e','i','o','u')

if es_vocal(a):
    print("Vertader")
else:
    print("False")
