# Cristofer fuentes
#programador de left for dead 2
#24-03-2025

# Ordenar alfabéticamente los elementos de tipo cadena en la tupla
pistas = ("Puerta Roja", 221, "Londres", 3.14, "Watson", 7, "Moriarty")
cadenas = [elemento for elemento in pistas if isinstance(elemento, str)]
print("Pistas ordenadas alfabéticamente:", sorted(cadenas))
