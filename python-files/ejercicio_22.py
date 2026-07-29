# -------------------------------------------------------------------------------------------
# KATA 22
#
# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
# -------------------------------------------------------------------------------------------


from functools import reduce


def producto_total(valores):
    """
    Recibe una lista de números y devuelve el producto de todos ellos,
    usando reduce() para ir multiplicando el acumulado por cada valor.
    """
    return reduce(lambda n1, n2: n1 * n2, valores)
    # (5 * 2) -> (10 * 7) -> (70 * 1) -> (70 * 6) = 420

if __name__ == "__main__":
    valores = [5, 2, 7, 1, 6]
    print("Valores:", valores)
    print("Resultado (producto):", producto_total(valores))
