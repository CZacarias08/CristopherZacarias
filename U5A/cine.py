
class Asiento:
    def __init__(self, estado):
        self.estado = estado

    def __str__(self):
        return self.estado


class Cine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.lugares = [[Asiento("L") for _ in range(columnas)] for _ in range(filas)]

    def reservar(self, fila, columna):
        if fila >= 0 and fila < self.filas and columna >= 0 and columna < self.columnas:
            asiento = self.lugares[fila][columna]

            if asiento.estado == "L":
                asiento.estado = "X"
                print("Asiento reservado correctamente")
            else:
                print("El asiento ya está ocupado")
        else:
            print("El asiento no existe")

    def liberar(self, fila, columna):
        if fila >= 0 and fila < self.filas and columna >= 0 and columna < self.columnas:
            asiento = self.lugares[fila][columna]

            if asiento.estado == "X":
                asiento.estado = "L"
                print("Asiento liberado correctamente")
            else:
                print("El asiento ya está libre")
        else:
            print("El asiento no existe")

    def contar_asientos(self):
        libres = 0
        ocupados = 0

        for fila in self.lugares:
            for asiento in fila:
                if asiento.estado == "L":
                    libres += 1
                else:
                    ocupados += 1

        print(f"Asientos libres: {libres}")
        print(f"Asientos ocupados: {ocupados}")

    def mostrar(self):
        print("ESTADO DE LA SALA")

        for fila in self.lugares:
            asientos = []
            for asiento in fila:
                asientos.append(f"[{asiento}]")
            print(" ".join(asientos))
        print()


filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

cine = Cine(filas, columnas)

opcion = 0

while opcion != 5:
    print("SISTEMA DE CINE")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        cine.mostrar()

    elif opcion == 2:
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        cine.reservar(fila - 1, columna - 1)

    elif opcion == 3:
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        cine.liberar(fila - 1, columna - 1)

    elif opcion == 4:
        cine.contar_asientos()

    elif opcion == 5:
        print("Gracias por utilizar el sistema")

    else:
        print("Opción no válida")
