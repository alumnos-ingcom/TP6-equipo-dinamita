################
# Fede Trujillo - @FNT138
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def reemplazar(cadena, dic):
    """
    Funcion para reemplazar caracteres con acentos ' (´)' ' (`) ' de una cadena dada
     """
    cadena = cadena.lower()
    for k,v in dic.items():        
        cadena=cadena.replace(k, v)
    
    cadena = str.rstrip(cadena)
    cadena = str.strip(cadena)
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
    dic={"à":"a", "è":"e", "ì":"i", "ò":"o", "ù":"u",
             "á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", 
             "ä":"a", "ë":"e", "ï":"i", "ö":"o", "ü":"u",
             ",":" ", ".":"", " ":""}
    texto_1 = str(input("Texto_ 1: "))
    texto_2 = str(input("Texto_ 2: "))
    reemplazo_1 = reemplazar(texto_1, dic)
    reemplazo_2 = reemplazar(texto_2, dic)
    
    anagrama = anagramas(reemplazo_1, reemplazo_2)
    print(anagrama)

    
    
if __name__ == "__main__":
    prueba()