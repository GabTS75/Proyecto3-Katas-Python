# -------------------------------------------------------------------------------------------
# KATA 10
#
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
# -------------------------------------------------------------------------------------------


class ListaVaciaError(Exception):
    """
    Excepción personalizada: se lanza cuando se intenta calcular el
    promedio de una lista vacía. Hereda de Exception, la clase base
    de la que parten todas las excepciones en Python.
    """

    pass


def calcular_promedio(numeros):
    """
    Recibe una lista de números y devuelve su promedio.
    Lanza ListaVaciaError si la lista está vacía (no se
    puede dividir entre 0 elementos).
    """
    if len(numeros) == 0:
        raise ListaVaciaError(
            "Esta lista está vacía, no se puede calcular su promedio."
        )
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    lista_1 = [4, 8, 6, 2]  # lista con números
    print("Lista:", lista_1)
    try:
        print("Resultado (promedio):", calcular_promedio(lista_1))
    except ListaVaciaError as error:
        print("Error:", error)

    lista_2 = []  # caso de lista vacía
    print("\nLista:", lista_2)
    try:
        print("Resultado (promedio):", calcular_promedio(lista_2))
    except ListaVaciaError as error:
        print("Error:", error)

# -------------------------------------------------------------------------------------------
# EXTRA
# En esta versión se muestra un try/except independiente por cada caso:
# Así, si uno falla, los demás siguen ejecutándose sin verse afectados
# (cada prueba es aislada de las otras). Si en un futuro se desea probar
# muchos casos sin repetir el bloque try/except una y otra vez, se puede
# meter las listas en una "lista de listas" y recorrerlas con un for,
# con el try/except dentro del bucle (así cada vuelta es independiente)

# Ejemplo:

# casos = [[4, 8, 6, 2], [], [10, 20, 30]]
# for lista in casos:
#     print("Lista:", lista)
#     try:
#         print("Resultado (promedio):", calcular_promedio(lista))
#     except ListaVaciaError as error:
#         print("Error:", error)
