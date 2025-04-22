#Cristofer Fuentes
#me duele la rodilla
#31-03-2025

llueve = input("¿Está lloviendo? (sí/no): ").lower() == "sí"
hay_sombra = input("¿Hay sombra? (sí/no): ").lower() == "sí"

if llueve or hay_sombra:
    print("Lleva paraguas o sombrero.")
else:
    print("Buen día para salir sin protección.")
