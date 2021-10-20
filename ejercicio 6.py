Num = int(input("Ingrese numero de la tabla que desea generar: "))
Mul = int(input("Ingrese numero de la tabla en la que inicia: "))



Ban = int(input("Ingrese el numero en el que termina la tabla: "))

while Mul != Ban:
    print(f'{Num} x {Mul} = {Num*Mul}')
    Mul += 1