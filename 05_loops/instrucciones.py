#Cristofer Fuentes
#me quiero ir de aqui
#07-04-2025


contador = 0

while contador <10:
    print("contador")
    contador +=1

else:
    print("dejo de contar")

# break

contador = 0

while contador <5 :
    contador +=1

    if (contador==4):
        print("se rompio el bucle")
        break 
    print (contador) 

#continue

contador = 0 
while contador <5: 
    contador +=1
    if (contador ==3):
        continue
    print(contador)