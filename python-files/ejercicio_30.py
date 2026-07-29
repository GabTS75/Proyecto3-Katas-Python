# -------------------------------------------------------------------------------------------
# KATA 30
#
# Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.
# -------------------------------------------------------------------------------------------


def son_anagramas(palabra1, palabra2):
    """
    Recibe dos palabras y devuelve True si son anagramas (mismas letras,
    mismas cantidades, distinto orden), comparando sus letras ordenadas
    alfabéticamente.
    """

    palabra1 = palabra1.lower()  # normalización usando .lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)


if __name__ == "__main__":
    p1 = "Fresa"
    p2 = "Frase"
    print(f"Palabras: '{p1}' y '{p2}'")
    print("Resultado (son anagramas):", son_anagramas(p1, p2))

    p3 = "Alicante"
    p4 = "Caliente"
    print(f"\nPalabras: '{p3}' y '{p4}'")
    print("Resultado (son anagramas):", son_anagramas(p3, p4))


# -------------------------------------------------------------------------------------------
# EXTRA
#
# Diferencia entre sorted() y .sort()
#
# sorted() es una función que ordena, crea y entrega una lista nueva
# y deja intacto el dato original.
#
# .sort() es un método exclusivo de las listas que modifica la misma
# lista en el lugar (in situ) y no crea una copia.
