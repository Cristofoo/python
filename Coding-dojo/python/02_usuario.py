class usuario:
    def __init__(self,nombre, edad, gmail, contraseña):
        self.nombre = nombre
        self.edad = edad
        self.gmail = gmail
        self.contraseña = contraseña
    
    def micontraseña(self):
        return self.contraseña
    
    def micumple(self):
        self.edad += 1
        return self.edad # si quiero volver algun numero que no se me olvide el return

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
gmail = input("¿Cuál es tu correo? ")
contraseña = input("Escribe una contraseña segura: ")

usuario_x = usuario(nombre, edad, gmail, contraseña)

print("mi contraseña", usuario_x.micontraseña())