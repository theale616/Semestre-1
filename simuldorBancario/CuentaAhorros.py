class CuentaAhorros_:
    
    saldoAhorros= 0
    tasa_interes= 0.006 
    
    
    

    def retirarvalor(self, valor):
    
        retiro= self.saldoAhorros - valor
        return retiro
        
    def depositarvalor(self, valor):
        deposito = self.saldoAhorros + valor
        return deposito

    def calcular_SaldoConInteres(self, meses):
        calculoTotal = self.saldoAhorros + (self.tasa_interes* meses)
        self.saldoAhorros = calculoTotal
        return calculoTotal
    