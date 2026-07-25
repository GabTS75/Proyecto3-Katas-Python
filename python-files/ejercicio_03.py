# -------------------------------------------------------------------------------------------
# KATA 03
#
# Escribe una función que tome una lista de palabras y una palabra objetivo como
# parámetros. La función debe devolver una lista con todas las palabras de la lista
# original que contengan la palabra objetivo.
# -------------------------------------------------------------------------------------------


def filtrar_palabras(lista_palabras, objetivo):
    """
    Recibe una lista de palabras y una palabra objetivo, y devuelve una
    nueva lista con las palabras originales que contienen "objetivo" en
    su interior. Uso .lower() sólo para la comparación, osea, la palabra
    devuelta conserva su forma original (no se guardará).
    """
    objetivo = objetivo.lower()  # normalizamos solo para la comparación
    resultado = []

    for palabra in lista_palabras:
        if objetivo in palabra.lower():  # comparamos ambas en minúsculas
            resultado.append(palabra)  # pero guardamos la palabra original

    return resultado


if __name__ == "__main__":
    palabras = ["Prometeo", "promesa", "improvisado", "programador", "programa"]
    print("Lista: Prometeo, promesa, improvisado, programador, programa")
    print("Objetivo: prom")
    print("Resultado:", filtrar_palabras(palabras, "prom"))
