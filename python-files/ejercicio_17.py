# -------------------------------------------------------------------------------------------
# KATA 17
#
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
# -------------------------------------------------------------------------------------------


from functools import reduce  # Cargamos la herramienta reduce()


def digitos_a_numero(digitos):
    """
    Recibe una lista de dígitos y devuelve el número que forman, usando
    reduce(): en cada paso, el acumulado se multiplica por 10 y se le
    suma el siguiente dígito (5 -> 5*10+7=57 -> 57*10+2=572).
    """
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)


if __name__ == "__main__":
    digitos = [2, 0, 2, 6]  # Año de la 2da. estrella para España ¡Campeones!
    print("Dígitos:", digitos)
    print("Resultado:", digitos_a_numero(digitos))
