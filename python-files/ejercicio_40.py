# -------------------------------------------------------------------------------------------
# KATA 40
#
# Escribe un programa en Python que utilice condicionales para determinar el monto
# final de una compra en una tienda en línea, después de aplicar un descuento.
#
# El programa debe:
#
# a. Solicitar al usuario el precio original de un artículo.
# b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
# c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
# d. Aplicar el descuento al precio original, siempre que el valor del cupón sea
#    válido (mayor a cero).
# e. Mostrar el precio final de la compra, considerando o no el descuento.
# f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las
#    acciones.
# -------------------------------------------------------------------------------------------


def calcular_precio_final(precio_original, tiene_cupon, valor_cupon=0):
    """
    Calcula el precio final de una compra en linea.
    Devuelve el precio final tras aplicar el descuento, si corresponde.
    """

    # Criterios a considerar:
    # - precio_original: precio antes de cualquier descuento.
    # - tiene_cupon: "si" o "no" (texto), indica si el usuario tiene cupón.
    # - valor_cupon: porcentaje de descuento del cupón (ejemplo: 20 = 20%),
    #   solo se usa si tiene_cupon es "si".
    #   Se asume que es un porcentaje, ya que el enunciado no lo especifica
    #   y es lo más habitual en tiendas online (también se puede cambiar a
    #   un descuento en importe fijo si se prefiere).

    tiene_cupon = tiene_cupon.lower()  # normalizamos, casos: "Sí"/"SI"/"si" -> "si"

    if tiene_cupon == "si":
        # Solo se aplica el descuento si el valor del cupón es mayor a 0;
        # un cupón de 0 o negativo quedaría "sin efecto".
        if valor_cupon > 0:
            descuento = precio_original * (valor_cupon / 100) # cálculo en %
            precio_final = precio_original - descuento
        else:
            precio_final = precio_original
    elif tiene_cupon == "no":
        precio_final = precio_original
    else:
        # Cualquier otra respuesta que no sea "si" ni "no" se considera inválida
        raise ValueError(
            f"Respuesta no válida: '{tiene_cupon}' (se esperaba 'si' o 'no')."
        )

    return precio_final


if __name__ == "__main__":
    # Casos de prueba: cada uno protegido con try/except, ya que cualquiera de
    # ellos podría lanzar ValueError (respuesta inválida en tiene_cupon) y el
    # programa no debe romperse por eso.
    casos_prueba = [
        (500, "si", 20),  # Caso 1: cupón válido del 20%
        (400, "si", 0),  # Caso 2: cupón inválido (0%), no se aplica
        (300, "no", 0),  # Caso 3: sin cupón
        (200, "quizas", 0),  # Caso 4: respuesta inválida, no es "si" ni "no"
    ]

    print("----- casos de prueba -----")

    for precio, tiene_cupon, valor_cupon in casos_prueba:
        print(
            f"\nPrecio original: {precio}, tiene cupón: {tiene_cupon}, valor del cupón: {valor_cupon}%"
        )
        try:
            print(
                "Precio final:", calcular_precio_final(precio, tiene_cupon, valor_cupon)
            )
        except ValueError as error:
            print("Error:", error)

    # -------------------------------------------------------------------------------------------
    # Para usarlo de forma interactiva:
    print("\n--- ingreso por input() ---")

    try:
        # float() también puede lanzar ValueError si el precio introducido no es
        # un número válido. Por ejemplo, si el usuario escribe "si" o "no" aquí
        # por error, como me paso a mí.

        precio_original = float(input("\nIntroduce el precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ")
        if tiene_cupon.lower() == "si":
            valor_cupon = float(input("Introduce el valor del cupón (%): "))
        else:
            valor_cupon = 0

        print(
            "Precio final:",
            calcular_precio_final(precio_original, tiene_cupon, valor_cupon),
        )
    except ValueError as error:
        print("Error: introduce 'valores válidos por favor'.", error)
