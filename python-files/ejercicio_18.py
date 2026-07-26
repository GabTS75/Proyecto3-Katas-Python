# -------------------------------------------------------------------------------------------
# KATA 18
#
# Escribe un programa en Python que cree una lista de diccionarios con información
# de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes
# con una calificación mayor o igual a 90.
# -------------------------------------------------------------------------------------------


def estudiantes_destacados(estudiantes):
    """
    Recibe una lista de diccionarios de estudiantes (cada uno con las
    claves "nombre", "edad" y "calificacion") y devuelve una nueva lista
    solo con los que tienen calificacion >= 90.
    """
    return list(
        filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)
    )


if __name__ == "__main__":
    estudiantes = [
        {"nombre": "Jose", "edad": 25, "calificacion": 98},
        {"nombre": "Maria", "edad": 22, "calificacion": 80},
        {"nombre": "Victoria", "edad": 20, "calificacion": 93},
        {"nombre": "Pedro", "edad": 27, "calificacion": 79},
    ]
    # Si uso print() con sep="\n", desempaqueta la lista usando el operador asterisco (*)
    # y separa cada elemento con un salto de línea (\n).
    print("Estudiantes:", *estudiantes, sep="\n")
    print(
        "\nResultado (calificación >= 90):",
        *estudiantes_destacados(estudiantes),
        sep="\n"
    )
