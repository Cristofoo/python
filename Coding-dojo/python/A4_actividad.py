# 1. Actualizar valores en diccionarios y listas
matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Actualizar matriz
matriz[1][0] = 6

# Actualizar cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

# Actualizar ciudades
ciudades["México"][2] = "Monterrey"

# Actualizar coordenadas
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        resultado = ", ".join([f"{k} - {v}" for k, v in diccionario.items()])
        print(resultado)

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)
