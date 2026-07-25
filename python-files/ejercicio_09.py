# -------------------------------------------------------------------------------------------
# KATA 09
#
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva
# una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a
# excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter().
# -------------------------------------------------------------------------------------------

MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


def filtrar_mascotas_permitidas(lista_mascotas):
    """
    Recibe una lista de nombres de mascotas y devuelve una nueva lista
    excluyendo las que están en MASCOTAS_PROHIBIDAS, usando filter().
    """

    # filter(funcion, lista) se queda solo con los elementos para los que
    # la función devuelve "True". Aquí, el "True" significa "no está en la
    # lista de prohibidas", por lo tanto, la dejamos pasar.
    permitidas = filter(
        lambda mascota: mascota not in MASCOTAS_PROHIBIDAS, lista_mascotas
    )
    return list(permitidas)


if __name__ == "__main__":
    mascotas = ["Perro", "Gato", "Tigre", "Conejo", "Oso", "Loro"]
    print("Lista de mascotas:", mascotas)
    print("Resultado (mascotas permitidas):", filtrar_mascotas_permitidas(mascotas))

# -------------------------------------------------------------------------------------------
# Obervación:
# A diferencia del ejercicio 3 (que comprobaba si un texto estaba
# CONTENIDO dentro de otro), aquí comprobamos si el elemento coincide
# EXACTAMENTE con alguno de la lista de prohibidas.
