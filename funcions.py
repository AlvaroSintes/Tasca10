def canvi(l,m,n):
    print("1){}{} \n {}".format(l, m,n))
    l='Adéu,'
    m='Alvaro'
    n='Que vagi bé'
    print("2) {}{} \n {}".format(l, m,n))
#Programa principal
a="Hola,"
b="Ramis."
c="Com estàs?"
print("El valor de la variable abans de canviar és: {}{}\n {}".format(a,b,c))
canvi(a,b,c)
print("El valor de la variable després de canviar és: {}{}\n {}".format(a,b,c))


"""
def canvi(l):
    x = int(input("Introdueixi la posició a modificar: "))
    l[x]=input("Introdueixi el valor a inserir: ")
#Programa principal
a=[3, 4, 5, 6, 7, 8, 'a', (1,2),[3,4],10]
# La llista 
print("El valor de la llista abans de canviar és: {}".format(a))
#Ens mostrara la llista
canvi(a)
#Canvia un valor de la llista
print("El valor de la llista després de canviar és: {}".format(a))
#Ens mostrara la llista modificada
def intercanvi(a,b):
    return b,a
x='a'
y='b'
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y = intercanvi(x,y)
print("Després de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))

def major(x,y):
    if x>y:
        return x
    else:
        return y
x= int(input("Introdueixi el primer numero: "))
y= int(input("Introdueixi el segon numero: "))
z= major(x,y)
print("El major de {} i {} és {}".format(x, y, z))
"""