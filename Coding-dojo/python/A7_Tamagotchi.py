# --- Clase Tamagotchi ---
class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} jugó y ahora tiene {self.felicidad} de felicidad y {self.salud} de salud.")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} comió y ahora tiene {self.felicidad} de felicidad y {self.salud} de salud.")

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} fue curado y ahora tiene {self.salud} de salud y {self.felicidad} de felicidad.")


# --- Clase Persona ---
class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} está jugando con {self.tamagotchi.nombre}")
        self.tamagotchi.jugar()

    def darle_comida(self):
        print(f"{self.nombre} le da comida a {self.tamagotchi.nombre}")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} cura a {self.tamagotchi.nombre}")
        self.tamagotchi.curar()


# --- Código principal ---
if __name__ == "__main__":
    # Crear instancia de Tamagotchi
    tama = Tamagotchi(nombre="Tamy", color="Rojo")

    # Crear instancia de Persona con Tamagotchi
    persona = Persona(nombre="Carlos", apellido="Pérez", tamagotchi=tama)

    # Interacciones
    persona.darle_comida()
    persona.curarlo()
    persona.jugar_con_tamagotchi()
