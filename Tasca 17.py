def llegir_llista():
    a='a'
    l= []
    while a!='.':
        a = input("Introdueixi una numero diferent a '.': ")
        if a !='.':
            l.append(int(a))
        else:
            return l

def sumar_llista(l):
    s=0
    for e in l:
        s += e
    print("La suma de tots els elements de la llista {} és {}".format(l,s))
def multiplicar_llista(l):
    m=1
    for e in l:
        m *= e 
    print("La multiplicacio de tots els elements de la llista {} és {}".format(l,m))

#Prorgrama principal
l = llegir_llista()
sumar_llista(l)
multiplicar_llista(l)
