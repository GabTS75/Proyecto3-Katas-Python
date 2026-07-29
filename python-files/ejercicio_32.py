# -------------------------------------------------------------------------------------------
# KATA 32
#
# Crea una función que tome un nombre completo y una lista de empleados, busque
# el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo
# contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# -------------------------------------------------------------------------------------------


def buscar_empleado(nombre, lista_empleados):
    """
    Busca nombre en lista_empleados (lista de diccionarios con claves
    "nombre" y "puesto"). Devuelve el puesto si lo encuentra, o un
    mensaje de "no trabaja aquí" en caso contrario.
    """
    nombre = nombre.lower()  # normalizo a minúsculas
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre:
            return empleado["puesto"]
    return f"'{nombre.title()}' no trabaja aquí."
    # Uso .title() para devolver el nombre con la primera letra en
    # mayúsculas, por si el nombre se encuentra en minúscula se
    # vea un poco mejor.


if __name__ == "__main__":
    lista_empleados = [
        {"nombre": "Juan Pérez", "puesto": "Administrador"},
        {"nombre": "Maria Martinez", "puesto": "Directora ejecutiva"},
        {"nombre": "Carlos López", "puesto": "Técnico de sistemas"},
    ]

    # Recordemos:   print() con sep="\n", el operador asterisco (*)
    #               desempaqueta la lista y luego separa cada elemento
    #               con un salto de línea (\n), como el ejercicio 18
    print("Lista de empleados:", *lista_empleados, sep="\n")

    print("\nNombre buscado: 'maria martinez'")
    print("Resultado:", buscar_empleado("maria martinez", lista_empleados))

    print("\nNombre buscado: 'Pedro Sánchez'")  # ¡claro que no trabaja aquí!
    print("Resultado:", buscar_empleado("Pedro Sánchez", lista_empleados))
