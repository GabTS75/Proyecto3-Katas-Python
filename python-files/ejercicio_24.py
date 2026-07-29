# -------------------------------------------------------------------------------------------
# KATA 24
#
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().
# -------------------------------------------------------------------------------------------


from functools import reduce


def diferencia_total(numeros):
    """
    Recibe una lista de valores (números) y calcula la resta
    acumulada de izquierda a derecha, usando reduce().
    """

    # reduce va restando de izquierda a derecha, ejemplo:
    # Coje los primeros valores (50-10), luego el
    # siguiente (40-30), y finalmente (10-3) = 7
    return reduce(lambda n1, n2: n1 - n2, numeros)


if __name__ == "__main__":
    numeros = [50, 10, 30, 3]
    print("Números:", numeros)
    print("Resultado (resta):", diferencia_total(numeros))
