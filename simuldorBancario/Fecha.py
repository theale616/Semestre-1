class Fecha_():
    
    dia = 0
    mes = 0
    anio = 0
    

    
    def ConsultarDia(self):
        # Aqui va el codigo del metodo
        return self.dia
    def ConsultarMes(self):
        # Aqui va el codigo del metodo
        return self.mes
    def ConsultarAnio(self):
        # Aqui va el codigo del metodo
        return self.anio
    def fechaNacimiento(self, diaNacimiento, mesNacimiento, anioNacimiento):
        ConsultarDia = diaNacimiento + mesNacimiento + anioNacimiento
        return ConsultarDia
