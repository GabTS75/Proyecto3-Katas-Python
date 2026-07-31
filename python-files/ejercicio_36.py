# -------------------------------------------------------------------------------------------
# KATA 36
#
# Crea una función llamada procesar_texto
# - Procesa un texto según la opción especificada: contar_palabras,
#   reemplazar_palabras o eliminar_palabra.
# - Código a seguir:
#     a. Crear una función contar_palabras que cuente el número de veces
#        que aparece cada palabra en el texto y devuelva un diccionario.
#     b. Crear una función reemplazar_palabras para sustituir una
#        palabra_original por una palabra_nueva en el texto y devolver
#        el texto modificado.
#     c. Crear una función eliminar_palabra que elimine una palabra del
#        texto y devuelva el texto sin ella.
#     d. Crear la función procesar_texto que reciba un texto, una opción
#        ("contar", "reemplazar", "eliminar") y un número variable de
#        argumentos según la opción elegida.
# - Caso de uso:
#     - Verificar el funcionamiento completo de procesar_texto.
# -------------------------------------------------------------------------------------------


def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en el texto y devuelve
    un diccionario (similar al ejercicio 1, pero contando palabras
    completas en vez de letras individuales).
    """
    palabras = texto.lower().split()  # normalizamos y separamos por espacios
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = (
            conteo.get(palabra, 0) + 1
        )  # patrón ya visto en el ejercicio 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Sustituye todas las apariciones de palabra_original por
    palabra_nueva dentro del texto, y devuelve el texto modificado.
    """

    palabras = texto.split()
    resultado = []

    # Se compara palabra por palabra completa (no como substring), para
    # no reemplazar por error dentro de otra palabra más larga.
    for palabra in palabras:
        if palabra == palabra_original:
            resultado.append(palabra_nueva)
        else:
            resultado.append(palabra)
    return " ".join(resultado)  # .join() une la lista de vuelta en un solo texto


def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Elimina todas las apariciones de palabra_a_eliminar del texto
    y devuelve el texto sin ella, usando filter() para quedarnos
    solo con las palabras que NO coinciden.
    """
    palabras = texto.split()
    palabras_filtradas = filter(lambda palabra: palabra != palabra_a_eliminar, palabras)
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    """
    Función "despachadora": según el valor de 'opcion', llama a la
    función correspondiente, pasándole el texto y los argumentos extra
    recibidos en *args (una tupla con lo que se haya pasado de más).
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        palabra_original, palabra_nueva = args  # desempaquetamos la tupla args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == "eliminar":
        (palabra_a_eliminar,) = (
            args  # tupla de un solo elemento: la coma final es necesaria ¡ojo!
        )
        return eliminar_palabra(texto, palabra_a_eliminar)
    else:
        raise ValueError(f"Opción no reconocida: '{opcion}'")


if __name__ == "__main__":
    texto = "el perro corre el gato duerme el perro juega"
    print("Texto:", texto)

    print("\nOpción: contar")
    print("Resultado:", procesar_texto(texto, "contar"))

    print("\nOpción: reemplazar ('perro' por 'gato')")
    print("Resultado:", procesar_texto(texto, "reemplazar", "perro", "gato"))

    print("\nOpción: eliminar ('el')")
    print("Resultado:", procesar_texto(texto, "eliminar", "el"))
