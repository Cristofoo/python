# Cristofer fuentes
#programador de left for dead 2
#24-03-2025

# Obtener el valor mínimo de los elementos numéricos en la tupla
pistas = ("Puerta Roja", 221, "Londres", 3.14, "Watson", 7, "Moriarty")
numeros = [elemento for elemento in pistas if isinstance(elemento, (int, float))]
print("Número mínimo:", min(numeros))
