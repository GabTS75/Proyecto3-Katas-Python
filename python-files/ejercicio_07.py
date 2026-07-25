# -------------------------------------------------------------------------------------------
# KATA 07
#
# Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map().
# -------------------------------------------------------------------------------------------


def tuplas_a_strings(lista_tuplas):
    """
    Recibe una lista de tuplas y devuelve una nueva lista donde cada
    tupla se ha convertido a su representación en texto (str), usando
    map() con la función incorporada str() directamente (sin necesidad
    de lambda(), porque str() ya es una función que hace justo eso).
    """
    return list(map(str, lista_tuplas))


if __name__ == "__main__":
    tuplas = [(3, 2), (5, 4), (1, 7)]
    print("Lista de tuplas:", tuplas)
    print("Resultado (lista de strings):", tuplas_a_strings(tuplas))
