class animal: 
    def __init__(self,nombre, edad, especie, habitad):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.habitad = habitad

    def miedad(self):
        return self.edad
    


class gato(animal):
    def __init__(self,nombre, edad, especie, habitad, color ):
        super().__init__(nombre, edad, especie, habitad)
        self.color = color

    def micolor(self):
        return self.color
       

# Entrada de datos
nombre = input("¿Cómo se llama tu gato? ")  
edad = int(input("¿Cuántos años tiene tu gato? "))
especie = input("¿Qué especie es tu gato? ")
habitad = input("¿Dónde vive tu gato? ")
color = input("¿De qué color es tu gato? ")

# Crear objeto
gato_x = gato(nombre, edad, especie, habitad, color)

# Salida
print("¿Qué especie es tu gato?", gato_x.especie)
print("¿Y de qué color es?", gato_x.micolor())
