#Cristofer Fuentes
#me quiero ir de aqui
#07-04-2025

adivinanza = 6 

intento = 0

while adivinanza != 6 and intento >0:
    adivinanza = int(input("Adivina el numero"))
    intento +=1
if adivinanza != 6:
    print("te quedaste sin intentos")
else: 
    print ("adivinaste")