# -------------------------------------------------------------------------------------------
# KATA 27
#
# Crea una función que calcule el promedio de una lista de números.
# -------------------------------------------------------------------------------------------


def calcular_promedio(numeros):
    """
    Recibe una lista de números y devuelve su promedio
    (suma total entre cantidad de elementos).
    """
    return sum(numeros) / len(numeros)


if __name__ == "__main__":
    numeros = [4, 17, 6, 3]
    print("Números:", numeros)
    print("Resultado (promedio):", calcular_promedio(numeros))
