#Cristofer Fuentes
#me quiero ir de aqui
#07-04-2025

print("banco del 4°B")

pin = int(input('ingresa tu pin:'))

while pin !=1234:
    pin = int (input('Pin incorrecto. Ingresa nuevamente'))

if pin == 1234:
    print("! Pin aceptado")
    print("Bienvenido a tu cuenta")