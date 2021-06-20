################
# Fede Trujillo - @FNT138
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp5ej8 import descifrado_cesar


def descifrar(texto, cifrado, rotacion):
    lista = ""
    with open(texto, encoding="utf-8") as arch:
        with open(cifrado, "x") as cifr:
            for linea in arch:
                lista = lista + (linea)
            re = reemplazar(lista)
            descifrar = descifrado_cesar(re, rotacion)
            cifr = cifr.write(descifrar)
            return"FIN"
                
def reemplazar(cadena):
    cadena = str(cadena)
    cadena = str.rstrip(cadena)
    return cadena                
                
            
        
def prueba():
    txt = str(input("Nombre del archivo a descifrar  SIN EXTENCION:  "))
    ext = ".cesar"
    rotacion = int(input("Ingrese la rotacion del cifrado: "))
    archivo = txt+ext
    ext = ".decode"
    descifrado = txt+ext
    funcion = descifrar(archivo, descifrado, rotacion)
    print(funcion)
    
if __name__ == "__main__":
    prueba()