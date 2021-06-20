################
# Fede Trujillo - @FNT138
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def copia(texto, texto_2):    
    with open(texto, encoding="utf-8") as arch:
        with open(texto_2, "x") as nuevo:
            for cadena in arch:
                nuevo.write(cadena)
            return "exito :D"
    
    
def prueba():
    texto = str(input("Ingrese el archiv a copiar con su extension: "))
    texto_2 = str(input("Ingrese el archivo de destino con su extension: "))
    copiadora = copia(texto, texto_2)
    print(f" Su archivo se copio con {copiadora}")

if __name__ == "__main__":
    prueba()