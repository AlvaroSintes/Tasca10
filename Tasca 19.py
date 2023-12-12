def es_palindrom(palabra):
    palabra = palabra.lower() 

    return palabra == palabra[::-1]

print(es_palindrom("radar"))   
print(es_palindrom("madre"))     
print(es_palindrom("tete"))  
print(es_palindrom("rallar")) 
print(es_palindrom("tapat"))  
print(es_palindrom("simis"))   
print(es_palindrom("refer"))   

print(es_palindrom("Alvaro")) 
print(es_palindrom("hello"))  