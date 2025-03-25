# Cristofer fuentes
#programador de left for dead 2
#24-03-2025
pistas = ("puerta roja", 221, "londres", 3.14, "watson", 7,"moriarty")

print(pistas[0])

#2

print(pistas[6])

#3

print (len(pistas))

#4
if 'londres' in pistas:
    print(" encontrada")
else:
    print("no encontrada")

#5
print(pistas[0])
print(pistas[1])
print(pistas[2])

'''o de esta manera'''

primeras = pistas[:3]
print(primeras)

#6

# Tupla original
pistas = ("puerta roja", 221, "londres", 3.14, "watson", 7,"moriarty")

# Pistas adicionales
pistas_adicionales = ("dedos", "sangre")

# Crear una nueva tupla combinando ambas
nueva_tupla = pistas + pistas_adicionales

print(nueva_tupla)

#7
pistas = ("puerta roja", 221, "londres", 3.14, "watson", 7, "moriarty")


try:
    posicion_watson = pistas.index("watson")
    print(f" la posición: {posicion_watson}")
except ValueError:
    print(" no se encuentra en la tupla.")

#8

contar = pistas.count(7)
print(contar)


