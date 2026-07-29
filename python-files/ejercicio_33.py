# -------------------------------------------------------------------------------------------
# KATA 33
#
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# -------------------------------------------------------------------------------------------


def suma_listas(lista1, lista2):
    """
    Recibe dos listas de números y devuelve una nueva lista con la suma
    elemento por elemento, usando map() con un lambda de dos parámetros.
    """

    # es similar al ejercicio 4, cambiando resta por suma.
    return list(map(lambda a, b: a + b, lista1, lista2))


if __name__ == "__main__":
    lista_a = [10, 20, 30, 40]  # uso mismos datos
    lista_b = [2, 4, 7, 9]
    print("Lista 1:", lista_a)
    print("Lista 2:", lista_b)
    print("Resultado:", suma_listas(lista_a, lista_b))
