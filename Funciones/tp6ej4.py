################
# Fede Trujillo - @FNT138
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej8 import cifrado_cesar


def cifrar(texto, cifrado, rotacion):
    lista = ""
    with open(texto, encoding="utf-8") as arch:
        with open(cifrado, "x") as cifr:
            for linea in arch:
                lista = lista + (linea)
            re = reemplazar(lista)
            cifrar = cifrado_cesar(re, rotacion)
            cifr = cifr.write(cifrar)
        return"FIN"
                
def reemplazar(cadena):
    cadena = str(cadena)
    cadena = str.rstrip(cadena)
    return cadena                
                
            
        
def prueba():
    txt = str(input("Nombre del archivo a cifrar: "))
    ext = str(input("Extension del archivo: "))
    rotacion = int(input("Ingrese la rotacion del cifrado: "))
    archivo = txt+ext
    ext = ".cesar"
    cifrado = txt+ext
    funcion = cifrar(archivo, cifrado, rotacion)
    print(funcion)
    
if __name__ == "__main__":
    prueba()
