################
# Fede Trujillo - @FNT138
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import re
def cadena_separada(separador, texto_a_separar):
    """ la funcion pasa el string recibido en 'texto_a_separar'
        a una lista en la primer vuelta del lazo, en la segunda
        elimina separadores y devuelve una tupla con los dos textos"""
    
    for i in range(2):
        expresion_regular = '|'.join(map(re.escape, separador))
        texto_separado = re.split(expresion_regular, texto_a_separar)
    return texto_separado


def desempaquetado(texto):
    """ La funcion desempaqueta la tupla recibida en el argumento
    'texto'
    """
    txt1 = texto[0]
    txt2 = texto[-1]
    return txt1, txt2
    
 
def reemplazar(cadena, dic):
    """
    Funcion para reemplazar convertir a minusculas y eliminar
    caracteres especiales
    (comas, acentos, espacios entre palabras y el salto de linea \n")
    de una cadena dada
     """
    cadena = cadena.lower()
    for k,v in dic.items():        
        cadena=cadena.replace(k, v)
    
    cadena = str.rstrip(cadena)
    cadena = str.strip(cadena)
    return cadena

def anagramas(txt1, txt2):
    """La funcion extrae los caracteres de la palabra utilizando sorted()
        y los compara para verificar si es un anagrama
    """
#     Una palabra es anagrama de otra si contiene las mismas letras aunque puedan
#     estar en diferente orden.    
#     retorna True si las palabras son anagramas  
   
    txt1 = sorted(txt1)
    txt2 = sorted(txt2)
    
    if txt1 == txt2:
        return True
    else:
        return False
 
 
 
 
 
def prueba():    
    dic={"à":"a", "è":"e", "ì":"i", "ò":"o", "ù":"u",
             "á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", 
             "ä":"a", "ë":"e", "ï":"i", "ö":"o", "ü":"u",
             ",":" ", ".":"", " ":""}
    separador = " - ","–" #establece los separadores del texto
    
    # abre y cierra el archivo en "lineas"
    with open("anagramas.txt", encoding="utf-8") as lineas: 
        for linea in lineas:
            text = (linea) #guarda el valor de linea
            #llama a la funcion que transforma a tuple la cadena
            separar = cadena_separada(separador, text)
            #llama a la funcion que desempaqueta la tupla
            texto_desempaquetar = desempaquetado(separar)
            #llama a la funcion que transforma los textos
            texto_reemplazar_1 = reemplazar(texto_desempaquetar[0], dic)            
            texto_reemplazar_2 = reemplazar(texto_desempaquetar[-1], dic)
            #llama a la funcion que verifica si es un anagrama
            anagrama = anagramas(texto_reemplazar_1, texto_reemplazar_2)
            #Imprime por consola el resultado 
            print(f"  ' {texto_desempaquetar} ' es ' {anagrama} '")    
    

if __name__ == "__main__":
    prueba()