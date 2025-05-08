# cristofer fuentes
# regalenme una rodillla nueva
# 28-04-2025


#conversion segura a un numero
# pedir un numero al usuario y evitar errores si se escribe letras

def pedir_numero ():
    try:
        numero = int(input("escribe un nunmero entero"))
        print("gracias tu numero es:", numero)
    except ValueError: 
        print("eso no es un numero valido. intenta otra vez")

pedir_numero()