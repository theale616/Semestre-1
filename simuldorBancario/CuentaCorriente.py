

class CuentaCorriente_:

    
    saldoCorriente= 0

    

        

    def depositarValor(self, valor):
        # Aqui va el codigo del metodo
        Deposito= self.saldoCorriente + valor
        return Deposito




    def retirarValor(self, valor):
        # Aqui va el codigo del metodo
        descuento= valor*0.01
        retiro= self.saldoCorriente - (valor+descuento)
        return retiro
    
    def SalditoCorriente(self):
        # Aqui va el codigo del metodo
        return self.saldoCorriente  