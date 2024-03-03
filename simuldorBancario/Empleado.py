from Fecha import  Fecha_


#Asociaciones
fechaNacimiento = Fecha_()
fechaIngreso = Fecha_()



class Empleado_:
    # Aqui va el codigo del empleado
    ''' # Atributos------------------------------------------------------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------------------------------------------------------------------'''
    nombre= ""
    apellido= ""
    nHijos = 0
    ''' 1= Masculino y 2 = Femenino
    '''
    sexo= 0
    salario = 0
    porcentaje_salario1= 0.05
    porcentaje_salario2= 0/100
    
    ''' Metodos

    '''
    
    


    def __init__(self, nombre, apellido, sexo, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.salario = salario



    
    '''# Informa el numero de hijos del empleado'''
   
    def NumeroDeHijos(self):
        
        return self.nHijos
        
        
    '''# Calcula el auxilio educativo del empleado. '''
   
    
    def AuxilioEducativo(self):
        
        auxilio = (self.salario*self.porcentaje_salario1 )*(self.nHijos)
        return auxilio
        
    '''# Calcula el auxilio educativo del empleado. '''

    def AuxilioEducativo2(self):

        auxilio2= self.salario* self.porcentaje_salario2
        return auxilio2
    
    '''# Calcula la diferencia salarial respecto a otro empleado '''
    
    def DiferenciaSalarial(self):

        from Inicio import empleado1, empleado2

        diferencia= abs(empleado1-empleado2)
        return diferencia






    
        
    
             
    def CambiarSalario( self, nuevoSalario):
        # Aqui va el codigo el metodo
        return 0
    def CambiarEmpleado( self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va el odigo del metodo
        return None
    def ConsultarSalario( self):
        # Aqui va el codigo del metodo
        return self.salario
    def ConsultarNombre(self):
        # Aqui va el codigo del metodo
        return self.nombre
    def ConsultarApellido(self):
        # Aqui va el codigo del metodo
        return self.apellido
    def ConsultarNombreCompleto(self):
        # Aqui va el codigo del metodo
        return self.nombre +"  "+ self.apellido
    def AumentoSalarial(self):
        nSalario =  self.salario * 0.05
        nSalario = nSalario+self.salario
        self.salario = nSalario
        return f" El nuevo salario es de:{nSalario} "
    def CamabiarApellido(self, nApellido):
        self.apellido = nApellido
        return " El nuevo apellido es:" + self.apellido
    def DuplicarSalario(self):
        # Aqui va el codigo
        # Forma1
        # self.salario = self.salario*2
        self.salario *=2

    def SalarioAnual(self):
        # Aqui va el codigo
        self.salario *= 12
        return " El salario anuela es de:" + self.salario
    
    
    
    
    


    def ConsultarDiaCumpleanios(self):
        return "El dia de su cumpleaños es:" + Fecha_.fechaNacimiento
    

    def CalcularImpuesto(self):

        #forma 1

        total = self.ConsultarSalario()
        return (total * 19,5 )/ 100
    
        # forma 2
        # return self.CalcularSalarioAnual() * 0.195
    




#del caso de estudio del simulador bancario vamos a crear las asociaciones y dentro de la clase de simulador bancario crear tres metodos 
      #consignar cuenta corriente, calcular el saldo total, pasar el saldo de ahorro a corriente"


#tarea " "En simulado bancario"
#dar saldo corriente, retirar todo y duplicar ahorro#