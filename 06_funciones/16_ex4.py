# cristofer fuentes
# regalenme una rodillla nueva
# 28-04-2025


#acceder un valor a un diccionario 
#sin que se rompa el programa si la clave no existe

def buscar_cantante():
    cantante= {
        "nombre": "luis",
        "pais" : "puero rico"
    }

    try:
        clave = input( "¿ Que quieres saber ? (nombre o pais)")
        print("Resultado:", cantante [clave])
    except KeyError:
        print("Esta clave no existe")
buscar_cantante()