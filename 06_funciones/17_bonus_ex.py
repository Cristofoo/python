# cristofer fuentes
# regalenme una rodillla nueva
# 28-04-2025


#repetir hasta que o hagan bien 
#podemos usar un bucle junto con try

def pedir_numero_repetido():
    while True:
        try: 
            numero = int(input("Escribe un numero entero:"))
            print(" ¡ Gracias tu numero es: ", numero)
            break
        except ValueError:
            print("eso no es un numero valido")
pedir_numero_repetido()