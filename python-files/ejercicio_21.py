# -------------------------------------------------------------------------------------------
# KATA 21
#
# Crea una función que calcule el cubo de un número dado mediante una función lambda.
# -------------------------------------------------------------------------------------------


cubo_num = lambda num: num ** 3
"""
Función que calcula el cubo de un número dado mediante
una función lambda simple.
"""


if __name__ == "__main__":
    numero = 4
    print("Número:", numero)
    print("Resultado (cubo):", cubo_num(numero))
