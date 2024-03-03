class Cliente:
    
    def cuentas_cliente(self):
        self.cuenta_corriente = CuentaCorriente()
        self.cuenta_ahorros = CuentaAhorros()
        self.cuenta_cdt= CDT()
        
        
class CuentaCorriente:
    def saldoCuentaCorriente(self):
        self.saldo = 0

    def depositarValor(self, valor):
        self.saldo += valor


    def retirarValor(self, valor):
        if valor <= self. saldo:
            self.saldo -= valor

        else:
            print("Error, El valor no se puede retirar por saldo insuficiente") 


class CuentaAhorros:
    def SaldoCuentaAhorros(self):
        self.saldo = 0

        self.tasa_interes = 0.006 # "La tasa de interes es del 0.6% mensual"

    def retirarvalor(self, valor):
        if self.saldo <= valor:
            self.saldo -= valor
        
    def depositarvalor(self, valor):
        self.saldo += valor

    def calcular_interes(self):
        interes_mensual = self.saldo*self.tasa_interes
        self.saldo += interes_mensual

        return interes_mensual
    
class CDT:
    def saldoCDT(self):

        self.valor_invertido = 0
        self.tasa_interes = 0
        self.meses_invertidos = 0

    def invertir_valor(self, valor, tasa_interes):
        self.valor_invertido = valor
        self.tasa_interes = tasa_interes
        self.meses_invertidos = 0

    def cerrarInversionCDT(self):
        intereses_generados = self.valor_invertido*self.tasa_interes*self.meses_invertidos
        self.valor_invertido += intereses_generados
        return intereses_generados
    
    def avanzar_mes(self):
        self.meses_invertidos += 1