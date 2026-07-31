# -------------------------------------------------------------------------------------------
# KATA 20
#
# Para una lista con elementos de tipo integer y string, obtén una nueva lista
# solo con los valores int. Usa la función filter().
# -------------------------------------------------------------------------------------------


def filtrar_int(elementos):
    """
    Recibe una lista con elementos de distintos tipos y devuelve una
    nueva lista solo con los que son de tipo int, usando isinstance()
    para comprobar el tipo de cada elemento.
    """
    return list(filter(lambda elemento: isinstance(elemento, int), elementos))


if __name__ == "__main__":
    elementos = ["Hola", 24, "vamos", 15, "puedes", 0.33]
    # Mostrará [24, 15], porque 0.33 también se excluye, ya que es de tipo float,
    # no int, aunque sea un número. ¡ojo!
    print("Lista:", elementos)
    print("Resultado (valores int):", filtrar_int(elementos))
