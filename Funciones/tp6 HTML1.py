################
# Fede Trujillo - @FNT138
# Walter Ojeda - @walter_ojeda
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hacer_etiqueta(contenido, etiqueta):
    html = '<%s>%s</%s>\n' % (etiqueta, contenido, etiqueta)
    return html

def hacer_comentario(contenido):
    coment = '<!--%s-->\n' % (contenido)
    return coment

def programa(contenido):
    programa_html = "<html>\n<body>\n%s</body>\n</html>" % (contenido)
    return programa_html

def archivo(nombre, programa):
    with open(nombre, "x") as arch:
        arch.write(programa)
    return 'archivo creado'
    
def prueba():
    html_programa = ''
    html= ''
    opciones = input("Ingrese 'H' si quiere hacer una etiqueta, o 'C' si quiere hacer un comentario: ")
    
    if opciones == 'H' or opciones == 'h':
        etiqueta = input("Ingrese tipo de etiqueta: ")
        contenido = input("Ingrese contenido de etiqueta: ")
        html = hacer_etiqueta(contenido, etiqueta)
        respuesta = input("Desea continuar? S/N: ")
        
        while respuesta == 'S' or respuesta == 's':
            etiqueta = input("Ingrese tipo de etiqueta: ")
            contenido = input("Ingrese contenido de etiqueta: ")
            html= html + hacer_etiqueta(contenido, etiqueta) 
            print(f"{html}")
            respuesta = input("desea continuar? S/N: ")
           
        opciones = input("Desea crear un archivo? S/N: ")
        if opciones == 's' or opciones == 'S':
            html_programa = programa(html)
            print(f"{html_programa}")
            txt = input("Ingrese nombre del programa: ")
            ext = '.html'
            pag = txt + ext
            program = archivo(pag, html_programa)
            print(f"{program}, todo listo papu")
        else:
            print("Muchas gracias por usar el programa :)")
        
    elif opciones == 'C' or opciones == 'c':
        contenido = input("Ingrese contenido de comentario: ")
        comentario = hacer_comentario(contenido)
        print(f"{comentario}")
    else:
        print("Opcion no valida, intente de nuevo :) ")

if __name__ == "__main__":
    prueba()