def gran(a, b): # Defineix la funció anomenada gran que pren dos paràmetres, 'a' i 'b'.
    if a > b:  # Verifica si 'a' és més gran que 'b'.
        return a  # Retorna a si la condició anterior és veritable.
    else:   # Si la condició anterior és falsa, vol dir que 'b' és més gran o igual a 'a'.
        return b # Retorna 'b' en aquest cas.

# Ús de la funció
x = input("Introdueixi el primer número a comparar: ") # Demana a l'usuari que introdueixi el primer número i emmagatzema l'entrada a la variable 'x'.
y = input("Introdueixi el segon número a comparar: ") # Demana a l'usuari que introdueixi el segon número i emmagatzema l'entrada a la variable 'y'.Demana a l'usuari que introdueixi el segon número i emmagatzema l'entrada a la variable 'y'.
c = gran(x, y) # Truca a la funció 'gran' amb els números ingressats com a arguments i emmagatzema el resultat a la variable 'c'.
print("El més gran és: ", c) # Imprimeix el missatge indicant quin dels dos números ingressats és més gran, utilitzant el valor retornat per la funció 'gran'.



   


