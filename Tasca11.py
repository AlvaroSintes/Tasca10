def menu_principal():
    print("""
        Menú principal:
          1. Calculadora enters
          2. Calculadora reals
          3. Sortir
          """)
    x = int(input("Elegeixi una opcio"))
    if x>0 and x<4:
        return x
    else:
        return 0
    
    #programa principal
    a = menu_principal()
    print(a)