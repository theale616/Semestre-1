def calcular_imc(altura, peso):

    return peso / (altura**2)


altura = float(input(" Por favor, introduce tu altura en metros: "))
peso = float( input( "Por favor, introduce tu peso en kilogramos: "))

imc = calcular_imc(altura, peso)

print("{:.2f}".format(imc))

if imc < 18.5:
    print("Peso muy bajo")
elif imc >= 18.5 and imc < 24.9:
    print("peso normal")    
elif imc >= 24.9 and imc < 29.9:
    print("sobrepeso")    
elif imc >= 29.9 and imc < 34.9:
    print(" obesidad")
else:
    print(" Obesidad morbida")
