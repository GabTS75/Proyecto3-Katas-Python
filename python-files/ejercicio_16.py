# -------------------------------------------------------------------------------------------
# KATA 16
#
# Escribe una función que tome una cadena de texto y un número entero n como parámetros
# y devuelva una lista de todas las palabras que sean más largas que n.
# Usa la función filter().
# -------------------------------------------------------------------------------------------


def palabras_mas_largas_que(cadena, n):
    """
    Recibe una cadena de texto y un número n, y devuelve una lista con
    las palabras cuya longitud es mayor que n.
    """

    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


if __name__ == "__main__":
    cadena = "Las oportunidades no aparecen, las creas"
    n = 4
    print("Cadena:", cadena)
    print("n:", n)
    print("Resultado:", palabras_mas_largas_que(cadena, n))
