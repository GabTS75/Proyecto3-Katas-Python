# -------------------------------------------------------------------------------------------
# KATA 13
#
# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas
# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map().
# -------------------------------------------------------------------------------------------


def mayus_minus_unicas(caracteres):
    """
    Recibe una cadena de caracteres y devuelve una lista de tuplas
    (MAYÚSCULA, minúscula) para cada letra distinta, sin repetidos.
    """
    letras_unicas = set(caracteres)
    resultado = map(lambda letra: (letra.upper(), letra.lower()), letras_unicas)
    return sorted(resultado)


if __name__ == "__main__":
    caracteres = "banana"
    print("Caracteres:", caracteres)
    print("Resultado (tuplas mayús/minús):", mayus_minus_unicas(caracteres))

# -------------------------------------------------------------------------------------------
# EXTRA
# - set(caracteres) elimina duplicados automáticamente.
#
# - map(lambda letra: (letra.upper(), letra.lower()), ...) construye la tupla de
#   cada letra, ya que esta transformación no es una función incorporada de Python
#   (a diferencia de str() o len() de los ejercicios anteriores) y por eso es que
#   se necesita un lambda propio.
#
# - sorted(...) es solo para que el resultado salga siempre en el mismo orden al
#   probarlo, ya que un set() en Python NO garantiza ningún orden concreto, de tal
#   manera que el resultado podría salir en distinto orden cada vez que se ejecute
#   el programa.
