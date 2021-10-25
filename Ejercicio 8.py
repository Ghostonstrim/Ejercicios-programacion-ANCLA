Personas = int(input("Ingrese el numero de personas: "))
if Personas <= 200:
    print(f'El total a pagar es: {Personas*95}')
elif Personas > 200 and Personas <= 300:
    print(f'El costo total a pagar es: {Personas*85}')
elif Personas > 300:
    print(f'El costo total a pagar es{Personas*75}')
