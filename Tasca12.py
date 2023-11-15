def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de números enters
          2. Calculadora de números reals
          3. Canvis de base
          4. Sortir
          """)
    a = int(input("Elegeixi una opcio: "))
    return a
def calculadora_enters():
    op = 1
    while op>0:
        print("""
              Menú enters
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = int(input("Elixeixi una opció: "))
        match op:
            case 1: #Sumar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueixi el segon número: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adéu, ja tornaras a la calculadora inicial \n\n")
                op=-1


def calculadora_reals():
    op = 1
    while op>0:
        print("""
              Menú reals
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = float(input("Elixeixi una opció: "))
        match op:
            case 1: #Sumar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueixi el segon número: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adéu, ja tornaras a la calculadora inicial \n\n")
                op=-1


# Funcions de canvis de base 
# De decimal a binari, octal i hexadecimal
def dectobin(numero):
    # Prec: Numero sigui un enter
    # Post: Escriu el valor de l'enter en binari
    return bin(numero)
def dectooct(numero):
    # Prec: Numero sigui un enter
    # Post: Escriu el valor de l'enter en octal
    return oct(numero)
def dectohex(numero):
    # Prec: Numero sigui un enter
    # Post: Escriu el valor de l'enter en hexadecimal
    return hex(numero)
    # De binari a octal, decimal, hexadecimal
def bintooct(numero):
    # Prec: Numero sigui una cadena de caracters
    # Post: Escriu en numero en octal
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    # Prec: Numero sigui una cadena de caracters
    # Post: Escriu en numero en decimal
    a=int(numero,2)
    return a
def bintohex(numero):
    # Prec: Numero sigui una cadena de caracters
    # Post: Escriu en numero en hexadecimal
    a=int(numero,2)
    return dectohex(a)
    # De octal a binari, decimal i hexadecimal
def octtobin(numero):
    # Prec: Numero sigui una cadena de caracters i en octal
    # Post: Escriu en numero en hexadecimal o millor dit, el retorna
    a = int(numero,8)
    return dectobin(a)
def octtodec(numero):
    # Prec: Numero sigui una cadena de caracters i en octal
    # Post: Escriu en numero en hexadecimal o millor dit, el retorna
    a = int(numero,8)
    return a
def octtohex(numero):
    # Prec: Numero sigui una cadena de caracters i en octal 
    # Post: Escriu en numero en hexadecimal o millor dit, el retorna
    a=int(numero,8)
    return dectohex(a)

def canvis_base():
    op = 1
    while op>0:
        print("""
            Menú canvis de base 
            1. Donat un binari ho passem a tota la resta
            2. Donat un octal el passem a tota la resta
            3. Donat un decimal ho passem a tota la resta
            4. Donat un hexadecimal ho passem a tota la resta
            5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: #Binari to
                b = input("Introdueixi el numero binari: ")
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El nuemro binari {} es: \n oct -> {} \n dec -> {} \n hex ->{}".format(b,o,d,h))
            case 2: # Octal to
                o = input("Introdueixi el numero octal: ")
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El nuemro octal {} es: \n bin -> {} \n dec -> {} \n hex ->{}".format(o,b,d,h))
            case 3: # Decimal to
                d = input("Introdueixi el numero decimal: ")
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
                print("El nuemro decimal {} es: \n bin -> {} \n oct -> {} \n hex ->{}".format(d,b,o,h))
            case 4: # Hexadecimal to
                h = input("Introdueixi el numero hexadecimal: ")
                b = hextobin(h)
                o = hextooct(h)
                d = hextodec(h)
                print("El nuemro hexadecimal {} es: \n bin -> {} \n oct -> {} \n dec ->{}".format(h,b,o,d))
            case 5: # Sortir
                print("Adeu, tornaras a la calculadora inicial \n\n")
                op=-1
#programa principal
a = 1
while a>0 :
    a = menu_principal()
    match a :
        case 1:
            calculadora_enters()
        case 2: 
            calculadora_reals()
        case 3:
            canvis_base()
        case 4:
            a = -1
        case other:
            print("Opció no vàlida ") 
