class TarjetaCredito:
    
    tarjetas_creadas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.tarjetas_creadas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self  

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self  

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self  

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self  

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("Información de todas las tarjetas:")
        for i, tarjeta in enumerate(cls.tarjetas_creadas, 1):
            print(f"Tarjeta {i}: Saldo a Pagar = ${tarjeta.saldo_pagar:.2f}, "
                  f"Límite = ${tarjeta.limite_credito}, Interés = {tarjeta.intereses * 100}%")


tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=1500, intereses=0.03)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.05)


tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()


tarjeta2.compra(300).compra(200).compra(250).pago(100).pago(50).cobrar_interes().mostrar_info_tarjeta()


tarjeta3.compra(100).compra(150).compra(100).compra(100).compra(100).mostrar_info_tarjeta()

# BONUS: mostrar todas las tarjetas creadas
TarjetaCredito.mostrar_todas_las_tarjetas()
