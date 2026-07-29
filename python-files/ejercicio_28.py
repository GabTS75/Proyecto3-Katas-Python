# -------------------------------------------------------------------------------------------
# KATA 28
#
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# -------------------------------------------------------------------------------------------


def primer_duplicado(lista):
    """
    Recibe una lista y devuelve el primer elemento que aparece repetido
    (recorriendo en orden), o None si no hay ningún duplicado.
    """
    vistos = set()
    # Un set() vacío que irá guardando los elementos "ya vistos" a medida que se
    # avanza, recordemos que un set() en Python NO respeta el orden original
    for elemento in lista:
        if elemento in vistos:
            return elemento
        else:
            vistos.add(elemento)
    return None  # None, si recorre toda la lista y no encuentra repetidos


if __name__ == "__main__":
    lista_1 = [4, 7, 2, 7, 9, 4]
    print("Lista con repetidos:", lista_1)
    print("Resultado (primer duplicado):", primer_duplicado(lista_1))

    lista_2 = [1, 2, 3, 4]
    print("\nLista sin repetidos:", lista_2)
    print("Resultado (primer duplicado):", primer_duplicado(lista_2))

# -------------------------------------------------------------------------------------------
# EXTRA
#
# Se usa .add() para añadir un elemento al conjunto sin importar la posición, ya que
# los conjuntos no tienen un orden fijo, además .add() se usa exclusivamente con objetos de
# tipo conjunto, como .set(), en cambio .append() es para listas.
#
# Se usa set() en Python para crear un conjunto vacío, eliminar elementos duplicados
# de una lista o convertir otro tipo de dato iterable en un conjunto de valores únicos.
#
# Casos de uso principales:
#
# - Borrar duplicados:              Pasas una lista con elementos repetidos
#                                   a set() para quedarte solo con los valores
#                                   únicos de forma rápida.
#
# - Crear un conjunto vacío:        Escribes mi_conjunto = set() (no uses {}
#                                   porque eso crea un diccionario vacío).
#
# - Buscar elementos con rapidez:   Los conjuntos están optimizados para comprobar
#                                   si un dato ya existe dentro de ellos en menor
#                                   tiempo que las listas.
#
# - Hacer operaciones matemáticas:  Sirven para unir, restar o buscar intersecciones
#                                   entre grupos de datos.
