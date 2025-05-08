# cristofer fuentes
# regalenme una rodillla nueva
# 28-04-2025


#mostrar un elemento de una lista por su posicion, si manejando si la
# posicion no existe

def mostrar_elemento():
    frutas = ["manzana", "banana", "naranja", "palta"]
    try:
        indice = int(input("elije una posicion ( 0 a 3 ): "))
        print("tu fruta elegida: ", frutas [indice])
    except IndexError:
        print("esta posicion no existe en la lista. Intentalo de nuevo")
    except ValueError:
        print("De ves ingresar un numero del 0 a 3 ")

mostrar_elemento()