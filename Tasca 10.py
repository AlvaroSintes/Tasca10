#Definició de la funció
def major(a): # Defineix la funció
    if x>18: # Verifica si la edat es major que 18.
        print("És major d'edat") # Imprimeix un missatge si la condició anterior és veritable, indicant que la persona és més gran.
    elif x<18: # Si la condició anterior no és vertadera, verifiqueu si l'edat és menor que 18.
        print("És menor d'edat") # Imprimeix un missatge si la segona condició és veritable, indicant que la persona és menor.
    else:  # Si cap de les condicions anteriors és vertadera, vol dir que l'edat és igual a 18.
        print("Té 18 anys") # Imprimeix un missatge indicant que la persona té 18 anys.Imprimeix un missatge indicant que la persona té 18 anys. 

#Programa principal
x = int(input("Introdueixi la seva edat: ")) # Demana a l'usuari que introdueixi la seva edat, converteix l'entrada a un sencer
major(x) # Truca a la funció 'major' amb l'edat ingressada com a argument, executa la funció per determinar i mostrar si ets mallor d'edat o no
