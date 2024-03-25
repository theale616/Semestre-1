from enum import Enum 
#enum para enumeracion, va dentro de la misma clase
class Tipo (Enum):
    """
    #enumeraciones para los tipos de productos
    """
    PEPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3
    
class Producto:
    
    """
    # constantes
    """
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMACIA = 0.12

    PRECIO_MAXIMO = 500000
    """
    #Atributo
    """
    __nombre = None
    __tipo = Enum('Tipo',['PAPELERIA','SUPERMERCADO','FARMACIA'])
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0
    
    """
    Metodos
    """
    def getNombre (self):
        return self.__nombre
    def getTipo (self):
        return self.__tipo
    def getValorUnitario (self):
        return self.__valorUnitario
    def getCantidadBodega (self):
        return self.__cantidadBodega
    def getCantidadMinima (self):
        return self.__cantidadMinima
    def getCantidadUnidadesVendidas (self):
        return self.__cantidadUnidadesVendidas






