class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    cantidadMinutosLlamadasCelular = 0 
    costoMinutosLlamadasCelular = 0
    estrato = 0
    segundosTotal = 0
    costoLlamadas = 0
    costoLlamadasDolares = 0
    saldoDisponible = 0
    descuentoLlamadas = 0.0
    # Numero de llamadas realizadas
    numeroLlamadas = 0
    # Numero de minutos consumidos
    numeroMinutos = 0
    # Costo total de las llamadas
    costoTotalLlamadas = 0
    
    '''----------------------------------------------------------------
    # Metodos
    -----------------------------------------------------------------'''
    def darMinutosPorEstrato (self):
        return self.numeroMinutos*self.estrato
    def definirEstrado(self, pEstrato):
        self.estrato = pEstrato
    def darEstrato (self):
        return self.estrato
    def motivarCliente (self):
        if self.numeroMinutos >= 30:
            self.saldoDisponible += 1000
    def agregarLlamadaLocal(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += 1
        costoLlamada = pMinutos * 35
        self.costoLlamadas += costoLlamada
        self.saldoDisponible -= costoLlamada
    def aumentarSaldo(self,valor):
        self.saldoDisponible += valor
    def saldo_Disponile (self):
        return self.saldoDisponible
    def descuentoLinea (self):
        return self.descuentoLlamadas
    def aplicarDescuento (self):
        return float ((self.costoTotalLlamadas * self.descuentoLlamadas)/100)
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        self.costoLlamadasDolares = 0
        self.segundosTotal = 0
        self.costoMinutosLlamadasCelular = 0
        self.cantidadMinutosLlamadasCelular = 0
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
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        self.segundosTotal = 0
        self.costoLlamadasDolares = 0
        self.cantidadMinutosLlamadasCelular = 0
        self.costoMinutosLlamadasCelular = 0

    def convertirPesosADolares(self):
        self.darCostoLlamadas / 3100


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
        self.costoMinutosLlamadasCelular += pMinutos * 999
        self.cantidadMinutosLlamadasCelular += pMinutos
    

        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
    def consultarCantidadMinutosCelular (self):
            return self.cantidadMinutosLlamadasCelular
    def consultarCostoLlamadasCelular (self):
            return self.costoMinutosLlamadasCelular * self.consultarCantidadMinutosCelular ()
