class perro:
    def __init__(self, nombre, raza, edad):
        self.name= nombre 
        self.age= edad
        self.race= raza
        #no es necesario que tengan distinto nombre porque se puede ocupar el mismo
#esto es un metodo
    def cumple(self):
        self.age += 1 
    
    def getname(self):
        return self.name  #vuelve al nombre 
    




miperro= perro("roko", 5 , "mestizo")
# print(miperro.name)
print("el nombre de mi perro es",miperro.getname())

miperro = perro("blanca", 14, "mestizo")
print (miperro.name)