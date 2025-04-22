#Cristofer Fuentes
#me duele la rodilla
#31-03-2025

altura = int(input("Introduce tu altura en cm: "))
creditos = int(input("Introduce tus créditos: "))

if altura >= 137 and creditos >= 10:
    print("¡Disfruta el viaje!")
elif creditos >= 10:
    print("No eres lo suficientemente alto para viajar.")
elif altura >= 137:
    print("No tienes suficientes créditos.")
else:
    print("No cumples ninguno de los requisitos.")
