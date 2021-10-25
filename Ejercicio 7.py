mts = int(input("Ingrese los metros de tela a pedir: "))

conv = 0.0254

pul = mts*1/0.0254

val = 0#variable para descuento

print(f'Las pulgadas a pedir son: {round(pul,2)}')

pre = pul*3

if pul >= 1000:
    val = pre*12.25/100
    print("El valor con descuento por mayoreo es" + str(val))
    print(f'El valor total a pagar con descuento es {round(pre-val,2)}')
else:
    print(f'El valor total a pagar es: {round(pre)}')