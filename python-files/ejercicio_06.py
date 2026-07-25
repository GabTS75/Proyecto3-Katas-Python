# -------------------------------------------------------------------------------------------
# KATA 06
#
# Escribe una función que calcule el factorial de un número de manera recursiva.
# -------------------------------------------------------------------------------------------


def factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    Caso base: 0! = 1 (detiene la cadena de llamadas).
    Caso general: n! = n * (n-1)!  (la función se llama a sí misma
    con un número más pequeño, hasta llegar al caso base).
    """
    if n == 0:
        return 1  # caso base: aquí se detienen las llamadas
    return n * factorial(n - 1)  # caso general: la función se llama a sí misma


if __name__ == "__main__":
    numero = 7
    print("Número:", numero)
    print("Resultado (factorial):", factorial(numero))

    numero = 0
    print("\nNúmero:", numero)
    print("Resultado (factorial):", factorial(numero))

# -------------------------------------------------------------------------------------------
# EJEMPLO "a mano" de aplicación del "caso base" para "visualizarlo" mejor
#
# factorial(3) = 3 * factorial(2)
#              = 3 * (2 * factorial(1))
#              = 3 * (2 * (1 * factorial(0)))
#              = 3 * (2 * (1 * 1))          <- aquí se toca el caso base (0! = 1)
#              = 3 * (2 * 1)
#              = 3 * 2
#              = 6
# -------------------------------------------------------------------------------------------
