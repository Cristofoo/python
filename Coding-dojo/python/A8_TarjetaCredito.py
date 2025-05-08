class TarjetaCredito:
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite
        self.saldo_pagar = 0

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite:
            self.saldo_pagar += monto
            print(f"Compra aprobada por ${monto} en tarjeta {self.numero}. Nuevo saldo a pagar: ${self.saldo_pagar}")
        else:
            print(f"Compra rechazada en tarjeta {self.numero}. Límite excedido.")

    def pagar(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        print(f"Pago de ${monto} realizado en tarjeta {self.numero}. Saldo restante: ${self.saldo_pagar}")



class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = {}  

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas[tarjeta.numero] = tarjeta
        print(f"Tarjeta {tarjeta.numero} agregada a {self.nombre}.")

    def hacer_compra(self, numero_tarjeta, monto):
        if numero_tarjeta in self.tarjetas:
            self.tarjetas[numero_tarjeta].compra(monto)
        else:
            print(f"Tarjeta {numero_tarjeta} no encontrada para {self.nombre}.")
        return self

    def pagar_tarjeta(self, numero_tarjeta, monto):
        if numero_tarjeta in self.tarjetas:
            self.tarjetas[numero_tarjeta].pagar(monto)
        else:
            print(f"Tarjeta {numero_tarjeta} no encontrada para {self.nombre}.")
        return self

    def mostrar_saldo_usuario(self):
        print(f"Saldo total de {self.nombre}:")
        for numero, tarjeta in self.tarjetas.items():
            print(f" - Tarjeta {numero}: ${tarjeta.saldo_pagar} a pagar")
        return self



if __name__ == "__main__":
    # Crear tarjetas
    tarjeta1 = TarjetaCredito("1111-2222", 1000)
    tarjeta2 = TarjetaCredito("3333-4444", 500)

    # Crear usuario y asignar tarjetas
    usuario = Usuario("Lucía")
    usuario.agregar_tarjeta(tarjeta1)
    usuario.agregar_tarjeta(tarjeta2)

    # Simular operaciones
    usuario.hacer_compra("1111-2222", 250)
    usuario.hacer_compra("3333-4444", 600)  # Excede el límite
    usuario.pagar_tarjeta("3333-4444", 100)
    usuario.mostrar_saldo_usuario()
