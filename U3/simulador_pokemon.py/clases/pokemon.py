
class Pokemon:
    cantidad = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon.cantidad += 1
        print(self.nombre, "ha sido capturado.")

    def __del__(self):
        if hasattr(self, "nombre"):
            print(self.nombre, "ha sido liberado.")

    def entrenar(self, *args):
        self.nivel += 1

        if len(args) == 0:
            self.ataque += 5
            self.defensa += 5
            self.salud += 10
        else:
            if len(args) >= 1:
                self.ataque += args[0]
            if len(args) >= 2:
                self.defensa += args[1]
            if len(args) >= 3:
                self.salud += args[2]

        print(self.nombre, "subió al nivel", self.nivel)

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo)
        print("Nivel:", self.nivel)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)
        print("Salud:", self.salud)
        print("Poder total:", self.calcular_poder())

    def atacar(self, objetivo):
        dano = self.ataque - objetivo.defensa

        if dano < 1:
            dano = 1

        objetivo.salud -= dano

        if objetivo.salud < 0:
            objetivo.salud = 0

        print(self.nombre, "atacó a", objetivo.nombre)
        print("Daño causado:", dano)
        print("Salud restante de", objetivo.nombre, ":", objetivo.salud)

    def calcular_poder(self):
        return self.ataque + self.defensa + self.salud + self.nivel * 10

    @classmethod
    def total_pokemons(cls):
        print("Pokémon creados:", cls.cantidad)
