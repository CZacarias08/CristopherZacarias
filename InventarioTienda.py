class InventarioTienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio > 0 and cantidad > 0:
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            self.productos.append(producto)
            print("Producto agregado correctamente")
        else:
            print("El precio y la cantidad deben ser positivos")

    def vender_producto(self, nombre, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
            return

        for producto in self.productos:
            if producto["nombre"] == nombre:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print("Venta realizada correctamente")
                else:
                    print("No hay suficiente stock")
                return

        print("El producto no existe")

    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print("El inventario está vacío")
        else:
            for producto in self.productos:
                print("Nombre:", producto["nombre"])
                print("Precio:", producto["precio"])
                print("Cantidad:", producto["cantidad"])
                print("--------------------")

    def producto_mas_caro(self):
        if len(self.productos) == 0:
            return None

        caro = self.productos[0]

        for producto in self.productos:
            if producto["precio"] > caro["precio"]:
                caro = producto

        return caro["nombre"], caro["precio"]


tienda = InventarioTienda("Mi tienda")

opcion = 0

while opcion != 5:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Producto más caro")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            tienda.agregar_producto(nombre, precio, cantidad)

        elif opcion == 2:
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a vender: "))

            tienda.vender_producto(nombre, cantidad)

        elif opcion == 3:
            tienda.mostrar_inventario()

        elif opcion == 4:
            resultado = tienda.producto_mas_caro()

            if resultado is None:
                print("No hay productos en el inventario")
            else:
                print("Producto más caro:", resultado[0])
                print("Precio:", resultado[1])

        elif opcion == 5:
            print("Saliendo del programa...")

        else:
            print("Opción no válida")

    except ValueError:
        print("Ingresa un número válido")