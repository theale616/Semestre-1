class LineaTelefonica:

    '''----------------------------------------------------------------
        # atributos
         ----------------------------------------------------------------'''
    
    saldoDispoible = 0
    descuentoLlamadas = 0.0
    estrato = 0
    # Numero de llamadas realizadas
    numeroLlamadas = 0
    # Numero de minutos consumidos
    numeroMinutos = 0
    # Costo total de las llamadas
    costoTotalLlamadas = 0
    

    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def definirEstrato(self, pEstrato):
        self.estrato = pEstrato



    def darEstrato (self):
        return self.estrato
  


    def motivarCliente(self):
        if self.numeroMinutos >= 30:
            self.saldo_Dispoible += 1000
        

    def agregarLlamadaLocal( self, pMinutos ):

        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        costoLlamada = pMinutos * 35 
        self.costoLlamadas += costoLlamada
        self.saldoDispoible -= costoLlamada

    def aumentarSaldo(self, valor):
        self.saldoDispoible += valor
    def saldo_Dispoible(self):
        return self.saldoDispoible
    
    def aplicarDescueto(self):
        return float((self.costoTotalLlamadas * self.descuentoLlamadas) / 100)

    def descuentoLinea(self):
        return self.descuentoLlamadas

    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numeroMinutos
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        #forma1:
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        #forma2:
        #reinicio = self.numeroLlamadas(0),self.numeroMinutos(0),self.costoLlamadas(0)
        #return reinicio


        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 999
        # TODO Parte2 PuntoG: Completar el método según la documentación dada