# cristofer fuentes
# tengo muchas caspaaaaaaaaaaaaaaaaaaaaaaaaa
# 21-04-2025


def obtener_articulo(numero):
    if numero == 1:
        return "🍔 Hamburguesa con queso"
    elif numero == 2:
        return "🍟 Papas fritas"
    elif numero == 3:
        return "🥤 Refresco"
    elif numero == 4:
        return "🍦 Helado"
    elif numero == 5:
        return "🍪 Galleta"
    else:
        return "Número no válido. Intenta con un número del 1 al 5."

def bienvenida():
    print("Bienvenido al Auto-Servicio 🚗🍔")
    print("Menú:")
    print("1. 🍔 Hamburguesa con queso")
    print("2. 🍟 Papas fritas")
    print("3. 🥤 Refresco")
    print("4. 🍦 Helado")
    print("5. 🍪 Galleta")


bienvenida()
opcion = int(input("Escribe el número del artículo que quieres pedir: "))
resultado = obtener_articulo(opcion)
print(f"Has seleccionado: {resultado}")
