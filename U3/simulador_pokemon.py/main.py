
from clases.pokemon import Pokemon

pokemons = []

def capturar():
    nombre = input("Nombre del Pokémon: ")
    tipo = input("Tipo: ")

    try:
        ataque = int(input("Ataque: "))
        defensa = int(input("Defensa: "))
        salud = int(input("Salud: "))

        if ataque < 0 or defensa < 0 or salud < 0:
            print("Las estadísticas no pueden ser negativas.")
            return

        pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)
        pokemons.append(pokemon)

    except ValueError:
        print("Debes ingresar números enteros en las estadísticas.")

def seleccionar():
    if len(pokemons) == 0:
        print("No hay Pokémon capturados.")
        return None

    for i in range(len(pokemons)):
        print(i + 1, "-", pokemons[i].nombre)

    try:
        numero = int(input("Selecciona un Pokémon: "))

        if 1 <= numero <= len(pokemons):
            return pokemons[numero - 1]

        print("Número incorrecto.")

    except ValueError:
        print("Debes ingresar un número.")

    return None

def entrenar():
    pokemon = seleccionar()

    if pokemon is not None:
        print("1. Entrenamiento normal")
        print("2. Personalizar mejoras")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pokemon.entrenar()

        elif opcion == "2":
            try:
                ataque = int(input("Mejora de ataque: "))
                defensa = int(input("Mejora de defensa: "))
                salud = int(input("Mejora de salud: "))

                if ataque < 0 or defensa < 0 or salud < 0:
                    print("Las mejoras no pueden ser negativas.")
                    return

                pokemon.entrenar(ataque, defensa, salud)

            except ValueError:
                print("Debes ingresar números enteros.")

        else:
            print("Opción incorrecta.")

def mostrar_pokemons():
    if len(pokemons) == 0:
        print("No hay Pokémon capturados.")
        return

    for pokemon in pokemons:
        print("--------------------")
        pokemon.mostrar_info()

def calcular_poder():
    pokemon = seleccionar()

    if pokemon is not None:
        print("Poder total de", pokemon.nombre, ":", pokemon.calcular_poder())

def atacar():
    print("Selecciona el Pokémon atacante:")
    atacante = seleccionar()

    if atacante is None:
        return

    print("Selecciona el Pokémon objetivo:")
    objetivo = seleccionar()

    if objetivo is None:
        return

    if atacante is objetivo:
        print("No puedes elegir el mismo Pokémon.")
    else:
        atacante.atacar(objetivo)

def liberar():
    pokemon = seleccionar()

    if pokemon is not None:
        pokemons.remove(pokemon)
        print(pokemon.nombre, "fue eliminado de la lista.")

def menu():
    opcion = ""

    while opcion != "0":
        print("\n--- SIMULADOR POKÉMON ---")
        print("1. Capturar Pokémon")
        print("2. Entrenar Pokémon")
        print("3. Mostrar todos los Pokémon")
        print("4. Contar Pokémon creados")
        print("5. Atacar a otro Pokémon")
        print("6. Liberar Pokémon")
        print("7. Calcular poder total")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            capturar()
        elif opcion == "2":
            entrenar()
        elif opcion == "3":
            mostrar_pokemons()
        elif opcion == "4":
            Pokemon.total_pokemons()
        elif opcion == "5":
            atacar()
        elif opcion == "6":
            liberar()
        elif opcion == "7":
            calcular_poder()
        elif opcion == "0":
            print("Fin del simulador.")
        else:
            print("Opción incorrecta.")

if __name__ == "__main__":
    menu()
