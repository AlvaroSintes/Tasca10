x= int(input("Introdueixi el primer numero: "))
y= int(input("Introdueixi el segon numero: "))
z= int(input("Introdueixi el tercer numero: "))

if x>y>z:
    print("El numero {} és major que {} i que {}".format(x,y,z))
elif y>x>z:
    print("El numero {} és major que {} i que {}".format(y,x,z))
elif z>y>x:
    print("El numero {} és major que {} i que {}".format(z,y,x))
elif x>z>y:
    print("El numero {} és major que {} i que {}".format(x,z,y))
elif x==y<z:
    print("El numero {} és major que {}".format(z,y))
elif y==z<x:
    print("El numero {} és major que {}".format(x,y))
elif x==z<y:
    print("El numero {} és major que {}".format(y,x))
elif x==y==z:
    print("Els numeros {},{} i {} son iguals ")
elif x==y>z:
    print("El numero {}  és major que {}".format(x,z))
elif y==z>x:
    print("El numero {}  és major que {}".format(z,x))
elif x==z>y:
    print("El numero {}  és major que {}".format(x,y))