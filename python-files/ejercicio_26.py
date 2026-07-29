# -------------------------------------------------------------------------------------------
# KATA 26
#
# Crea una función lambda que calcule el resto de la división entre dos números dados.
# -------------------------------------------------------------------------------------------


resto = lambda n1, n2: n1 % n2


if __name__ == "__main__":
    n1 = 18
    n2 = 5
    print("Números:", n1, "y", n2)
    print("Resultado (resto):", resto(n1, n2))
