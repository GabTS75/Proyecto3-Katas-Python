# -------------------------------------------------------------------------------------------
# KATA 05
#
# Escribe una función que tome una lista de números como parámetro y un valor opcional
# nota_aprobado (por defecto 5). La función debe calcular la media de los números en la
# lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado
# será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que
# contenga la media y el estado.
# -------------------------------------------------------------------------------------------


def evaluar_notas(notas, nota_aprobado=5):
    """
    Recibe una lista de notas y un umbral opcional (por defecto 5).
    Devuelve una tupla (media, estado), donde estado es "aprobado" si
    la media es >= nota_aprobado, o "suspenso" en caso contrario.
    """
    media = sum(notas) / len(notas)  # suma total / cantidad de elementos

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)  # tupla: par de valores empaquetado


if __name__ == "__main__":
    notas_a = [4, 9, 10]
    print("Notas A: 4, 9, 10")
    print("Resultado:", evaluar_notas(notas_a))  # usa el umbral por defecto (5)

    notas_b = [1, 3, 5]
    print("Notas B: 1, 3, 5")
    print(evaluar_notas(notas_b))  # también con el umbral por defecto

    # EJEMPLO ADICIONAL (si cambiamos el umbral)
    notas_c = [5, 6, 6]
    print("Notas C: 5, 6, 6 (nota_aprobatoria es 7 en este caso)")
    print(evaluar_notas(notas_c, nota_aprobado=7))
    # Demostración de que el parámetro opcional es determinante.
