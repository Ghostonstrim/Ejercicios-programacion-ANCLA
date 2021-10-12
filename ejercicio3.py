Nota = int(input("Ingresar nota: "))
if (Nota == 10):
    print("Sobresaliente")
if(Nota == 9):
    print("Muy bueno")
if(Nota in range(7, 9)):
     print("Bueno")
if(Nota in range(5, 7)):
     print("Regular")
if(Nota in range(1, 5)):
     print("Deficiente")
if(Nota == 0):
    print("Error... El valor ingresado no es correcto")
if(Nota > 10):
    print("Error valor imposible")