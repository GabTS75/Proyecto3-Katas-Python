# -------------------------------------------------------------------------------------------
# KATA 39
#
# Escribe una función que tome dos parámetros: figura (una cadena que puede
# ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos
# necesarios para calcular el área de la figura).
# -------------------------------------------------------------------------------------------


PI = 3.1416


def calcular_area(figura, datos):
    """
    Recibe el nombre de una figura y una tupla con sus datos, y
    devuelve el área calculada según el tipo de figura.
    """

    # Formulas:
    # - "rectangulo": datos = (largo, ancho)    -> área = largo * ancho
    # - "circulo":    datos = (radio,)          -> área = PI * radio ** 2
    # - "triangulo":  datos = (base, altura)    -> área = (base * altura) / 2

    figura = figura.lower() # normalizo a minúsculas para la comparación

    if figura == "rectangulo":
        largo, ancho = datos
        return largo * ancho
    elif figura == "circulo":
        (radio,) = datos  # tupla de un solo elemento (coma final necesaria)
        return PI * radio**2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError(f"Figura no reconocida: '{figura}'")
        # lanza el error si se ingresa otra figura, ejemplo: "pentagono"


if __name__ == "__main__":
    print("Rectángulo (largo=5, ancho=3):", calcular_area("rectangulo", (5, 3)))
    print("Círculo (radio=4):", calcular_area("circulo", (4,)))  # aquí la coma ¡ojo!
    print("Triángulo (base=6, altura=8):", calcular_area("triangulo", (6, 8)))
