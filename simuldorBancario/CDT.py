class CDT_:

    valorInvertido = 0
    tasaIntereses = 0
    mesesInvertidos = 0
    saldoTotal = 0


    def ConsultarsaldoCDT(self):
        # Aqui va el codigo del metodo
        print(f"Su saldo CDT es de : {self.saldoTotal}")
    def invertirValor(self):
        # Aqui va el codigo del metodo
        self.saldoTotal+= self.valorInvertido
        return self.valorInvertido 
    def CerrarCDT(self):
        self.saldoTotal= self.valorInvertido + (self. tasaIntereses* self.mesesInvertidos)
        return self.saldoTotal
    print(f"Su saldo total es de {saldoTotal}")      