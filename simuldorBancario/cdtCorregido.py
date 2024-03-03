class CDT():
    def __init__(self, invertir, interes_mensual, mes_apertura):
        self.saldo = invertir
        self.interesMensual = interes_mensual
        self.mesDeApertura = mes_apertura

    def invertir_dinero(self):
        ingreso = float(input("¿CUÁNTO DINERO DESEA INVERTIR?: "))
        self.saldo += ingreso
        print(f" TU SALDO ES DE: {self.saldo} ")

    def consultar_saldo_e_intereses(self):
        intereses_generados = self.saldo * self.interesMensual
        print(f"Saldo actual: {self.saldo}")
        print(f"Intereses generados: {intereses_generados}")

    def cerrar_inversion(self):
        intereses_generados = self.saldo * self.interesMensual
        total_final = self.saldo + intereses_generados
        print(f"Se cerró el CDT. El saldo final con intereses es: {total_final}")
        quit()

# Crear una Cuenta o instancia de CDT
mi_cdt = CDT(invertir=0, interes_mensual=0.02, mes_apertura="Febrero")

print("Bienvenido al CDT:")

while True:
    print("\nSeleccione:")
    print("1= Invertir dinero")
    print("2= Consultar saldo e intereses generados")
    print("3= Cerrar la inversión")
    print("4= Salir")

    opcion = int(input())

    if opcion == 1:
        mi_cdt.invertir_dinero()
    elif opcion == 2:
        mi_cdt.consultar_saldo_e_intereses()
    elif opcion == 3:
        mi_cdt.cerrar_inversion()
    elif opcion == 4:
        quit()
    else:
        print("Opción no válida. Inténtalo de nuevo.")
