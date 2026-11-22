
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Grupo:
    def __init__(self, estudiantes, materias):
        self.estudiantes = estudiantes
        self.materias = materias
        self.calificaciones = [[None] * materias for _ in range(estudiantes)]

    def capturar_calificaciones(self):
        for i in range(self.estudiantes):
            print("\nEstudiante", i + 1)

            for j in range(self.materias):
                calificacion = float(input("Calificación de materia " + str(j + 1) + ": "))

                while calificacion < 0 or calificacion > 100:
                    print("Calificación inválida")
                    calificacion = float(input("Ingresa nuevamente: "))

                self.calificaciones[i][j] = calificacion

    def promedio_estudiantes(self):
        promedios = []

        for fila in self.calificaciones:
            promedio = sum(fila) / self.materias
            promedios.append(round(promedio, 2))

        return promedios

    def promedio_materias(self):
        promedios = []

        for j in range(self.materias):
            suma = 0

            for i in range(self.estudiantes):
                suma += self.calificaciones[i][j]

            promedio = suma / self.estudiantes
            promedios.append(round(promedio, 2))

        return promedios

    def calificacion_mayor(self):
        return max(max(fila) for fila in self.calificaciones)

    def calificacion_menor(self):
        return min(min(fila) for fila in self.calificaciones)

    def mostrar(self):
        print("\nESTADO DE LA MATRIZ")

        for fila in self.calificaciones:
            print(fila)

        print()

    def resultados(self):
        print("PROMEDIO POR ESTUDIANTE")

        for i, promedio in enumerate(self.promedio_estudiantes()):
            print(f"Estudiante {i + 1}: {promedio}")

        print("\nPROMEDIO POR MATERIA")

        for j, promedio in enumerate(self.promedio_materias()):
            print(f"Materia {j + 1}: {promedio}")

        print("\nCalificación más alta:", self.calificacion_mayor())
        print("Calificación más baja:", self.calificacion_menor())


estudiantes = int(input("¿Cuántos estudiantes hay? "))
materias = int(input("¿Cuántas materias tienen? "))

grupo = Grupo(estudiantes, materias)

grupo.capturar_calificaciones()
grupo.mostrar()
grupo.resultados()
