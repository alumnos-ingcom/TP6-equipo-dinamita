def reemplazar(cadena, dic):
    """
    Funcion para reemplazar caracteres con acentos ' (´)' ' (`) ' de una cadena dada
     """
    for k,v in dic.items():
        cadena=cadena.replace(k, v)
    return cadena    


def anagramas(txt1, txt2):
    """
    Una palabra es anagrama de otra si contiene las mismas letras aunque puedan
    estar en diferente orden.
    
    retorna True si las palabras son anagramas  
    """
    txt1 = txt1.lower()
    txt2 = txt2.lower()
    
    return sorted(txt1) == sorted(txt2)    


def prueba():
    dic={"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u",
             "Á":"A", "É":"E", "Í":"i", "Ó":"O", "Ú":"U",
             "à":"a", "è":"e", "ì":"i", "ò":"o", "ù":"u",
             "À":"A", "È":"E", "Ì":"i", "Ò":"O", "Ù":"U"}
    texto_1 = str(input("Texto_ 1: "))
    texto_2 = str(input("Texto_ 2: "))
    reemplazo_1 = reemplazar(texto_1, dic)
    reemplazo_2 = reemplazar(texto_2, dic)
    
    anagrama = anagramas(reemplazo_1, reemplazo_2)
    print(anagrama)

    
    
if __name__ == "__main__":
    prueba()