cadena = input("Por favor, introduce una cadena: ")

cadena = cadena.lower()


l_cadena=list(cadena)


while " " in l_cadena:
    l_cadena.remove(" ")



l_cadena_alReves=list(l_cadena)

l_cadena_alReves.reverse()


while " " in l_cadena_alReves:
    l_cadena_alReves.remove(" ")

if l_cadena == l_cadena_alReves:
    print("la cadena introducida es un polindromo")

else:
    print("la cadena introducida no es un polindromo")





