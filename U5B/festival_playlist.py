
nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    cantidad = int(input("¿Cuántas canciones deseas agregar?: "))

    for i in range(cantidad):
        print("\nCanción", i + 1)

        nombre = input("Nombre: ")
        artista = input("Artista: ")
        duracion = float(input("Duración en minutos: "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\nCanciones agregadas correctamente.")

def ver_reportes():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)
    promedio = sum(popularidades) / total

    mayor = popularidades.index(max(popularidades))
    menor = popularidades.index(min(popularidades))

    print("\n--- REPORTES ---")
    print("Total de canciones:", total)
    print("Duración total:", duracion_total, "minutos")
    print("Canción más popular:", nombres[mayor])
    print("Canción menos popular:", nombres[menor])
    print("Promedio de popularidad:", round(promedio, 2))

def buscar_canciones():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    print("\n1. Buscar por artista")
    print("2. Buscar por popularidad")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        artista = input("Nombre del artista: ").lower()
        encontrado = False

        for i in range(len(nombres)):
            if artistas[i].lower() == artista:
                print(nombres[i], "-", artistas[i], "-", popularidades[i])
                encontrado = True

        if encontrado == False:
            print("No se encontraron canciones.")

    elif opcion == "2":
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))
        encontrado = False

        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(nombres[i], "-", artistas[i], "-", popularidades[i])
                encontrado = True

        if encontrado == False:
            print("No se encontraron canciones.")

    else:
        print("Opción no válida.")

def playlist_recomendada():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\n--- PLAYLIST RECOMENDADA ---")

    encontrado = False

    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(nombres[i], "-", artistas[i], "-", popularidades[i])
            encontrado = True

    if encontrado == False:
        print("No hay canciones recomendadas.")

while True:
    print("\n===== FESTIVAL PLAYLIST =====")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_canciones()

    elif opcion == "2":
        ver_reportes()

    elif opcion == "3":
        buscar_canciones()

    elif opcion == "4":
        playlist_recomendada()

    elif opcion == "5":
        print("Gracias por utilizar Festival Playlist.")
        break

    else:
        print("Opción no válida.")
