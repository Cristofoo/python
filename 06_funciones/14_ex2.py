# cristofer fuentes
# regalenme una rodillla nueva
# 28-04-2025

#division segura
#dividir entre 2 numeros y evitar o alterar siel usuario quiere dividir entre 0

def division_segura():
    try:
        num1 = int(input("ingresa un numero:  "))
        num2 = int(input("ingresa otro numero:  "))
        resultado = num1 / num2
        print("este es tu resultado", resultado)
    except ZeroDivisionError:
        print("Lo sentimos pero no se puede realizar esta division. Intentalo de nuevo")
    except ValueError:
        print(" Error. solo debes ingresar numeros")

division_segura() 