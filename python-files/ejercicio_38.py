# -------------------------------------------------------------------------------------------
# KATA 38
#
# Escribe un programa que determine qué calificación en texto tiene un alumno
# según su calificación numérica.
# - Reglas:
#     - 0 - 69: insuficiente
#     - 70 - 79: bien
#     - 80 - 89: muy bien
#     - 90 - 100: excelente
# -------------------------------------------------------------------------------------------


def calificacion_texto(nota):
    """
    Recibe una nota numérica (0-100) y devuelve su calificación en
    texto según las reglas: insuficiente, bien, muy bien o excelente.
    """

    if 0 <= nota < 70:
        return "insuficiente"
    elif 70 <= nota < 80:
        return "bien"
    elif 80 <= nota < 90:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "nota fuera de rango (0-100)"

    # Muy similar al anterior ejercicio, misma estructura if/elif/else
    # pero con rangos distintos para la nota.


if __name__ == "__main__":
    notas_prueba = [45, 69, 70, 79, 80, 89, 95, 120]
    for nota in notas_prueba:
        print(f"Nota: {nota} -> Calificación: {calificacion_texto(nota)}")
