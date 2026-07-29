# -------------------------------------------------------------------------------------------
# KATA 23
#
# Concatena una lista de palabras. Usa la función reduce().
# -------------------------------------------------------------------------------------------


from functools import reduce


def concatena_palabras(palabras):
    """
    Recibe una lista de palabras y las concatena en una sola cadena,
    separadas por un espacio.
    """
    return reduce(lambda p1, p2: p1 + " " + p2, palabras)
    # Con reduce() vamos "pegando" cada palabra nueva
    # al resultado acumulado y agregamos el espacio también.


if __name__ == "__main__":
    palabras = ["Siempre", "se", "puede", "mejorar"]
    print("Palabras:", palabras)
    print("Resultado (concatenación):", concatena_palabras(palabras))
