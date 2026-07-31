# -------------------------------------------------------------------------------------------
# KATA 31
#
# Crea una función que solicite al usuario ingresar una lista de
# nombres y luego un nombre para buscar en esa lista. Si el nombre
# está en la lista, imprime un mensaje indicando que fue encontrado;
# de lo contrario, lanza una excepción.
# -------------------------------------------------------------------------------------------


class NombreNoEncontradoError(Exception):
    """
    Excepción personalizada: se lanza cuando el nombre buscado no está
    en la lista de nombres.
    """

    pass  # en espera


def buscar_nombre(lista_nombres, nombre_buscado):
    """
    Busca nombre_buscado dentro de lista_nombres.
    Si lo encuentra, imprime un mensaje de éxito.
    Si no lo encuentra, lanza NombreNoEncontradoError.
    """
    if nombre_buscado in lista_nombres:
        print(f"'{nombre_buscado}' fue encontrado en la lista.")
    else:  # es cuando hace la llamada a la excepción personalizada
        raise NombreNoEncontradoError(
            f"'{nombre_buscado}' no fue encontrado en la lista."
        )


if __name__ == "__main__":
    lista_nombres = ["Ana", "Luis", "Carlos", "Victoria", "Antonio"]
    print("--- Usando lista de prueba ---")
    print("Lista de nombres:", lista_nombres)
    print("Nombre buscado: Antonio")
    try:
        buscar_nombre(lista_nombres, "Antonio")
    except NombreNoEncontradoError as error:
        print("Error:", error)

    print("\nLista de nombres:", lista_nombres)
    print("Nombre buscado: Pedro")
    try:
        buscar_nombre(lista_nombres, "Pedro")
    except NombreNoEncontradoError as error:
        print("Error:", error)

    # Para usarlo de forma interactiva:
    print("\n----- Usando input() -----")
    print("Recordar que Python distingue entre mayúsculas y minúsculas")
    texto = input("\nIntroduce los nombres separados por comas: ")
    lista_nombres = []
    for nombre in texto.split(","):
        lista_nombres.append(nombre.strip())
        # .strip() le quita los espacios sobrantes

    nombre_buscado = input("Introduce el nombre a buscar: ").strip()
    try:
        buscar_nombre(lista_nombres, nombre_buscado)
    except NombreNoEncontradoError as error:
        print("Error:", error)
