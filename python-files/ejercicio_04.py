# -------------------------------------------------------------------------------------------
# KATA 04
#
# Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map().
# -------------------------------------------------------------------------------------------


def diferencia_listas(lista1, lista2):
    """
    Recibe dos listas de números y devuelve una nueva lista con la
    diferencia elemento a elemento (lista1[i] - lista2[i]) usando map()
    con dos iterables a la vez.
    """
    # map(funcion, lista1, lista2) -> toma un elemento de lista1 y el
    # elemento de la MISMA posición de lista2, y se los pasa a la vez
    # a la función (aquí, la lambda con dos parámetros: a, b)
    return list(map(lambda a, b: a - b, lista1, lista2))


if __name__ == "__main__":
    lista_a = [10, 20, 30, 40]
    lista_b = [2, 4, 7, 9]
    print("Lista 1: 10, 20, 30, 40")
    print("Lista 2: 2, 4, 7, 9")
    print("Resultado:", diferencia_listas(lista_a, lista_b))

# Observación:
# Si las listas tuvieran longitudes diferentes, map() se detiene en la más
# corta, es decir, no mostrará error, simplemente ignorará los elementos
# sobrantes de la lista más larga.
