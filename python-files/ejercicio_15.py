# -------------------------------------------------------------------------------------------
# KATA 15
#
# Crea una función lambda que sume 3 a cada número de una lista dada.
# -------------------------------------------------------------------------------------------


sumar_tres = lambda numero: numero + 3


def sumar_tres_a_lista(lista_num):
    """
    Recibe una lista de números y devuelve una nueva lista con cada
    valor incrementado en 3.
    """
    return list(map(sumar_tres, lista_num))
    # Utilizo map() para aplicar lambda, puesto que el lambda (separado), opera
    # sobre UN solo número, con el map() consigo que aplique a cada elemento
    # de la lista, similar al ejercicio 2


if __name__ == "__main__":
    lista_num = [10, 20, 30, 40]
    print("Lista:", lista_num)
    print("Resultado:", sumar_tres_a_lista(lista_num))

# -------------------------------------------------------------------------------------------
# EXTRA
# Aprendí: Que cuando se usa lambda junto con map(), el lambda describe qué hacer
# con un elemento, y map() es quien se encarga de repetirlo para toda la lista,
# no hace falta un def alrededor que "devuelva" el lambda sin usarlo.
