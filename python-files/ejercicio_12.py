# -------------------------------------------------------------------------------------------
# KATA 12
#
# Genera una función que, al recibir una frase, devuelva una lista con la longitud
# de cada palabra. Usa la función map().
# -------------------------------------------------------------------------------------------


def longitudes_palabras(frase):
    """
    Recibe una frase y devuelve una lista con la longitud (número de
    letras) de cada palabra.
    """
    palabras = frase.split()  # divide la frase por espacios
    return list(map(len, palabras))


# He usado split() para separar la frase en palabras independientes y
# map(len, ...) para medir cada una sin necesidad de lambda, igual que
# map(str, ...) en el ejercicio 7.

if __name__ == "__main__":
    frase = "Estoy aprendiendo Python paso a paso"
    print("Frase:", frase)
    print("Resultado (longitudes):", longitudes_palabras(frase))
