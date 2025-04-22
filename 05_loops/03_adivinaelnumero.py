#Cristofer Fuentes
#me quiero ir de aqui
#07-04-2025



import random
numero_secreto = random.randint(1, 20)
intentos = 0

while intentos < 5:
    adivina = int(input("Adivina un número (1-20): "))
    intentos += 1
    if adivina == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break
    else:
        print("No es correcto.")
