# -------------------------------------------------------------------------------------------
# KATA 01
#
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
# -------------------------------------------------------------------------------------------


def contar_letras(cadena):
    """
    Recibe una cadena de texto y devuelve un diccionario con la frecuencia de
    cada letra (sin distinguir mayúsculas/minúsculas, sin contar espacios).
    """
    cadena = cadena.lower()  # normalizamos: todo a minúsculas
    resultado = {}  # diccionario vacío donde iremos contando

    for letra in cadena:
        if letra != " ":  # solo contamos si NO es un espacio
            resultado[letra] = resultado.get(letra, 0) + 1
        # .get(letra, 0) -> si "letra" ya existe como clave, devuelve su valor actual;
        #                   si no existe todavía, devuelve 0 (valor por defecto)
        # y a ese resultado le sumamos 1 y lo guardamos de nuevo en esa misma clave

    return resultado


# Comprobamos:
if __name__ == "__main__":
    texto = "Aprendiendo Python"
    print("Cadena de texto: Aprendiendo Python")
    print("Resultado:", contar_letras(texto))
