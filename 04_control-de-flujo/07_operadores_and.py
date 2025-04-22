#Cristofer Fuentes
#me duele la rodilla
#31-03-2025

edad = int(input("Edad: "))
tiene_carnet = input("¿Tienes carnet? (sí/no): ").lower() == "sí"

if edad >= 18 and tiene_carnet:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")
