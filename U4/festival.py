
# CLASE BASE
class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
        print(f"Genero musical: {self.genero}")
        print(f"Popular: {self.popularidad}/100")

    def actuar(self):
        print(f"{self.nombre} esta actuando")

    def despedirse(self):
        print(f"Gracias por estar aqui a {self.nombre}")


# SUBCLASE CANTANTE
class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f" {self.nombre} canta su exito {self.cancion_mas_popular} con gran energia.")


# SUBCLASE DJ
class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f" El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al publico.")


# SUBCLASE BANDA
class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


# FUNCION DEL FESTIVAL
def iniciar_festival(lista_artistas):
    print("\n===== FESTIVAL MUSICAL =====")

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuacion ")
        print("------------------------------")

    print("EL FESTIVAL HA TERMINADO")


# PROGRAMA PRINCIPAL
def main():
    lista_artistas = []

    cantidad = int(input("Cuantos artistas se presentaran? "))

    for i in range(cantidad):
        print(f"\nArtista {i + 1}")
        print("1. Cantante")
        print("2. DJ")
        print("3. Banda")

        tipo = input("Elige el tipo de artista: ")

        if tipo not in ("1", "2", "3"):
            print("Tipo de artista no valido")
            continue

        nombre = input("Nombre: ")
        genero = input("Genero musical: ")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                print("La popularidad debe estar entre 1 y 100")
            except ValueError:
                print("Ingresa un numero entero")

        if tipo == "1":
            cancion = input("Cancion mas popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)

        elif tipo == "2":
            estilo = input("Estilo musical del DJ: ")
            artista = DJ(nombre, genero, popularidad, estilo)

        elif tipo == "3":
            integrantes = int(input("Numero de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()
