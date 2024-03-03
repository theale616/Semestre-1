
from CuentaAhorros import CuentaAhorros_
from CuentaCorriente import CuentaCorriente_
from CDT import CDT_

class SimuladorBancario_:

    "# Atributos"
    cedula= 0
    nombres= ""
    mesActual= 0
    tipoCliente= None

    "# Asociaciones"
    corriente= CuentaCorriente_
    Ahorro= CuentaAhorros_
    CDt = CDT_



    def __init__(self, cedula, nombres, mesActual, clienteNormal, clienteVIP, clientePlatino):
        self.cedula= cedula
        self.nombres= nombres
        self.mesActual=mesActual
        self.clienteNormal=clienteNormal
        self.clienteVIP= clienteVIP
        self.clientePlatino= clientePlatino
    
    
    
    
    "# Metodos de asociaciones"
  
    
    def CalcularSaldoTotal(self):
        return self.corriente.saldoCorriente() + self.Ahorro.saldoAhorros()

    def ConsignarCuentaCorriente(self, valor):
        self.corriente.depositarValor(valor)
        

    def PasarSaldoAhorroCorriente(self):
        self.corriente.depositarValor(self.Ahorro.calcular_SaldoConInteres())
        self.Ahorro.retirarvalor(self.Ahorro.calcular_SaldoConInteres())
       
        
        
    def DarSaldoCorriente(self):
        CuentaCorriente_.saldoCorriente= self.CalcularSaldoTotal(CuentaCorriente_.saldoCorriente)
        return CuentaCorriente_.saldoCorriente
    
    
        
    def DuplicarAhorro(self):
        self.Ahorro.depositarvalor(self.Ahorro.calcular_SaldoConInteres()+self.Ahorro.calcular_SaldoConInteres())
        
        
    def RetirarTodo(self):
        
        total = self.CalcularSaldoTotal()
        self.corriente.retirarValor(self.corriente.SalditoCorriente())
        self.Ahorro.retirarvalor(self.Ahorro.calcular_SaldoConInteres())
        return total

    "# metodos"


    def CambiarTipoCliente(self, nuevoTipoCliente):
         

         if nuevoTipoCliente == self.clienteVIP:
            self.tipoCliente = "VIP"
         elif self.clienteNormal:
             self.tipoCliente = "Normal"
         elif self.clientePlatino:
             self.tipoCliente = "Platino"
        

        