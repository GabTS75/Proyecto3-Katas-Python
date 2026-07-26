# -------------------------------------------------------------------------------------------
# KATA 14
#
# Crea una función que retorne las palabras de una lista que comiencen con
# una letra en específico. Usa la función filter().
# -------------------------------------------------------------------------------------------


def palabras_que_empiezan_por(lista_palabras, letra):
    """
    Recibe una lista de palabras y una letra, y devuelve una nueva lista
    con las palabras que empiezan por esa letra, usando filter().
    """

    # Utilizo .lower() para la comparación de mayúsculas/minúsculas
    # (mismo criterio que en algunos ejercicios anteriores), conservando
    # la palabra original en el resultado.
    letra = letra.lower()  # normalización mayúsculas/minúsculas

    return list(
        filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras)
    )


if __name__ == "__main__":
    palabras = ["Python", "Java", "programa", "python", "", "PHP", "Super"]
    letra = "p"
    print("Lista de palabras:", palabras)
    print("Letra buscada:", letra)
    print("Resultado:", palabras_que_empiezan_por(palabras, letra))

# -------------------------------------------------------------------------------------------
# EXTRA
#
# Método .startswith()
#
# texto.startswith(prefijo) devuelve True si texto empieza exactamente por
# prefijo, y False si no. Es más robusto que comparar palabra[0] a mano,
# porque si igresan una palabra vacía "", siendo palabra[0] daría un error
# (no hay posición 0 en una cadena vacía), mientras que "".startswith("a")
# simplemente devuelve False sin fallar. Además de que distingue mayúsculas
# de minúsculas, ejemplo:
# "Python".startswith("Py")   # True
# "Python".startswith("py")   # False
