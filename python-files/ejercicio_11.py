# -------------------------------------------------------------------------------------------
# KATA 11
#
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# -------------------------------------------------------------------------------------------


class EdadInvalidaError(Exception):
    """
    Excepción personalizada: se lanza cuando la edad es un número válido
    pero se encuentra fuera del rango permitido (0-120).
    """

    pass  # a la espera de ... fuera de rango



def validar_edad(texto_edad):
    """
    Recibe la edad como texto (tal como llegaría de input()), la
    convierte a número y valida que esté en el rango 0-120.
    """

# - Si el texto no se puede convertir a int, Python lanza ValueError
#   automáticamente (no hace falta un raise manual para este caso).
# - Si el número está fuera de rango, lanzamos nuestra excepción
#   EdadInvalidaError, para poder distinguirlo del ValueError.
    edad = int(texto_edad)
    # puede lanzar ValueError si se ingresa texto (valor no numérico)

    if not (0 <= edad <= 120):
        raise EdadInvalidaError(
            f"La edad {edad} está fuera del rango permitido (0-120)."
        )

    return edad


if __name__ == "__main__":
    casos = ["30", "-5", "150", "abc"]

    for texto in casos:
        print("Entrada:", texto)
        try:
            edad = validar_edad(texto)
        except ValueError:
            print("Error: introduce un número válido.")
        except EdadInvalidaError as error:
            print("Error:", error)
        else:
            print(f"Resultado: edad válida ({edad} años).")
            # La f antes de las comillas sirve para crear una f-string (cadena formateada)
            # Permite incluir variables directamente dentro de un texto sin tener que usar
            # signos de suma (+) ni comas. Python reemplaza automáticamente el nombre de
            # la variable entre llaves {} por su valor real.
        print()  # print vacío para generar un espacio en cada caso (vuelta)

# -------------------------------------------------------------------------------------------
# EJEMPLO:
# Para usarlo de forma interactiva, ingresado por usuario.
# SE DEBE "comentar o quitar" el bloque "for texto in casos" de arriba ¡ojo!
#
# print("Con datos por input:")
# texto_edad = input("\nIntroduce tu edad: ")
# try:
#     edad = validar_edad(texto_edad)
# except ValueError:
#     print("Error: introduce un número válido.")
# except EdadInvalidaError as error:
#     print("Error:", error)
# else:
#     print(f"Resultado: edad válida ({edad} años).")


# -------------------------------------------------------------------------------------------
# EXTRA
# Si por ejemplo probamos: edad > 0 or edad > 120

# -50 > 0 -> False
# -50 < 120 -> True
# False or True -> True

# Es decir, esa condición da True (la trata como "válida") incluso con una "edad negativa",
# porque un "or" entre dos condiciones tan amplias termina siendo casi siempre True para
# cualquier número.
# Para lanzar el error en (edad < 0 or edad > 120), basta con que se cumpla una de las dos
# condiciones extremas.
