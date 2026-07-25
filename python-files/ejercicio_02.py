# -------------------------------------------------------------------------------------------
# KATA 02
#
# Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map().
# -------------------------------------------------------------------------------------------


def duplicar_valores(numeros):
    """
    Recibe una lista de números y devuelve una nueva lista con cada
    valor multiplicado por 2, usando map() en lugar de un bucle for.
    """
    # map(funcion, lista) aplica "funcion" a cada elemento de "lista"
    # lambda x: x * 2  ->  función anónima: "dado x, devuelve x*2"
    # list(...)        ->  convertimos el resultado de map() (para iterar)
    #                      en una lista normal, ya que map() por sí solo
    #                      no es una lista, sino que recorre "por encima"
    return list(map(lambda x: x * 2, numeros))


if __name__ == "__main__":
    lista = [1, 3, 4, 6]
    print("Lista de prueba: 1, 3, 4, 6")
    print("Resultado:", duplicar_valores(lista))
