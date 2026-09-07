ano = int(input("Ingresa un año: "))

if ano % 400 == 0:
    print("El año es bisiesto")

elif ano % 100 == 0:
    print("El año no es bisiesto")

elif ano % 4 == 0:
    print("El año es bisiesto")

else:
    print("El año no es bisiesto")