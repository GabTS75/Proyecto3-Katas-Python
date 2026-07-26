# -------------------------------------------------------------------------------------------
# KATA 19
#
# Crea una función lambda que filtre los números impares de una lista dada.
# -------------------------------------------------------------------------------------------


# El lambda (separado) comprueba si UN número es impar (True/False); luego
# filter() lo aplica a toda la lista, quedándose solo con los que dan True
es_impar = lambda n: n % 2 != 0


def filtrar_impares(lista_num):
    """
    Recibe una lista de números y devuelve una nueva lista solo con los
    valores impares, usando el lambda es_impar junto con filter().
    """
    return list(filter(es_impar, lista_num))


if __name__ == "__main__":
    lista_num = [12, 5, 8, 3, 24, 17, 20]
    print("Lista:", lista_num)
    print("Resultado (impares):", filtrar_impares(lista_num))
