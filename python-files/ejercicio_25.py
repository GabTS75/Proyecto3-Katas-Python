# -------------------------------------------------------------------------------------------
# KATA 25
#
# Crea una función que cuente el número de caracteres en una cadena de texto dada.
# -------------------------------------------------------------------------------------------


def contar_caracteres(cadena):
    """
    Recibe una cadena de texto y devuelve su número total de caracteres
    (incluye espacios y signos de puntuación), usando len().
    """
    return len(cadena)


if __name__ == "__main__":
    cadena = "Prohibido rendirse, respira hondo y sigue"
    print("Cadena:", cadena)
    print("Resultado (número de caracteres):", contar_caracteres(cadena))
