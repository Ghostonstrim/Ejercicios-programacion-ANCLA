n1 = int(input("Ingrese n1: "))
n2 = int(input("Ingrese n2: "))

while n1 == n2:
    print("Ingrese dos numeros diferentes por favor")
    n1 = int(input("Ingrese n1: "))
    n2 = int(input("Ingrese n2: "))
    continue
if n1 != n2:
    if n1 > n2:
        print( str(n1) + " es el numero mayor")
    if n1 < n2:
        print( str(n2) + " es el numero mayor")