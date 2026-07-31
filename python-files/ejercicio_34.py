# -------------------------------------------------------------------------------------------
# KATA 34
#
# Crea la clase Arbol
# - Define un árbol genérico con un tronco y ramas como atributos.
# - Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
# - Código a seguir:
#     a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#     b. Implementar el método crecer_tronco para aumentar la longitud del tronco en
#        una unidad.
#     c. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a
#        la lista de ramas.
#     d. Implementar el método crecer_ramas para aumentar en una unidad la longitud de
#        todas las ramas existentes.
#     e. Implementar el método quitar_rama para eliminar una rama en una posición
#        específica.
#     f. Implementar el método info_arbol para devolver información sobre la longitud
#        del tronco, el número de ramas y sus longitudes.
# - Caso de uso:
#     1. Crear un árbol.
#     2. Hacer crecer el tronco una unidad.
#     3. Añadir una nueva rama.
#     4. Hacer crecer todas las ramas una unidad.
#     5. Añadir dos nuevas ramas.
#     6. Retirar la rama situada en la posición 2.
#     7. Obtener información sobre el árbol.
# -------------------------------------------------------------------------------------------


class Arbol:
    """
    Representa un árbol genérico. Cada objeto Arbol tiene su propio
    tronco (un número que representa su longitud) y su propia lista de
    ramas (cada rama también representada por su longitud, un número).
    """

    def __init__(self):
        # __init__ se ejecuta automáticamente al crear un Arbol nuevo,
        # por ejemplo: mi_arbol = Arbol()
        self.tronco = 1  # todo árbol nuevo empieza con tronco de longitud 1
        self.ramas = []  # y sin ninguna rama todavía (lista vacía)

    def crecer_tronco(self):
        """Aumenta la longitud del tronco de ESTE árbol en 1 unidad."""
        self.tronco += 1  # equivalente a: self.tronco = self.tronco + 1

    def nueva_rama(self):
        """Añade una rama nueva, de longitud inicial 1, a la lista de ramas."""
        self.ramas.append(1)  # .append() que agrega al final de la lista

    def crecer_ramas(self):
        """Aumenta en 1 unidad la longitud de TODAS las ramas existentes."""
        # Recorremos por índice (posición), no por valor directo, porque
        # necesitamos MODIFICAR cada elemento de la lista, no solo leerlo.
        # range(len(self.ramas)) genera 0, 1, 2... hasta el último índice válido.
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        """Elimina la rama situada en 'posicion' (empezando a contar desde 0)."""
        del self.ramas[posicion]  # 'del' elimina el elemento en esa posición

    def info_arbol(self):
        """
        Devuelve un diccionario con la longitud del tronco, el número de
        ramas y la longitud de cada una (similar al ejercicio 18).
        """
        return {
            "tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "ramas": self.ramas,
        }


if __name__ == "__main__":
    # 1. Crear un árbol
    mi_arbol = Arbol()
    print("Árbol recién creado:", mi_arbol.info_arbol())

    # 2. Hacer crecer el tronco una unidad
    mi_arbol.crecer_tronco()
    print("\nTras crecer_tronco():", mi_arbol.info_arbol())

    # 3. Añadir una nueva rama
    mi_arbol.nueva_rama()
    print("\nTras nueva_rama():", mi_arbol.info_arbol())

    # 4. Hacer crecer todas las ramas una unidad
    mi_arbol.crecer_ramas()
    print("\nTras crecer_ramas():", mi_arbol.info_arbol())

    # 5. Añadir dos nuevas ramas (dos llamadas más a nueva_rama)
    mi_arbol.nueva_rama()
    mi_arbol.nueva_rama()
    print("\nTras añadir dos ramas más:", mi_arbol.info_arbol())

    # 6. Retirar la rama situada en la posición 2 ¡ojo!
    mi_arbol.quitar_rama(2)
    print("\nTras quitar_rama(2):", mi_arbol.info_arbol())

    # 7. Obtener información final sobre el árbol
    print("\nInformación final del árbol:", mi_arbol.info_arbol())
