# -------------------------------------------------------------------------------------------
# KATA 08
#
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas
# excepciones de manera adecuada y muestra un mensaje indicando si la división fue
# exitosa o no.
# -------------------------------------------------------------------------------------------


def dividir_con_manejo(texto_num1, texto_num2):
    """
    Recibe dos valores en texto (tal como llegarían de input()), intenta
    convertirlos a número y dividirlos, y maneja los errores posibles.
    1ro. recibe el texto como parámetro (en vez de llamar a input() aquí
    dentro) para poder probar la función fácilmente en distintos casos.
    """
    try:
        num1 = float(texto_num1)
        num2 = float(texto_num2)
        resultado = num1 / num2
    except ValueError:
        print("Error: introduce un número válido.")
    except ZeroDivisionError:
        print("Error: no es posible dividir entre cero.")
    else:
        # Se ejecutará solo si el try NO lanzó ninguna excepción
        print(f"División exitosa. Resultado: {resultado}")


if __name__ == "__main__":
    print("Con datos para prueba:")
    print("\nEntrada: '5' y '2' (el caso correcto)")
    dividir_con_manejo("5", "2")

    print("\nEntrada: '10' y '0' (división entre cero)")
    dividir_con_manejo("10", "0")

    print("\nEntrada: '8' y 'abc' (valor no numérico)")
    dividir_con_manejo("8", "abc")
    print("========================================")

# -------------------------------------------------------------------------------------------
    # EJEMPLO:
    # Para usarlo de forma interactiva, ingresado por usuario:
    print("\nCon datos por input:")
    n1 = input("\nIntroduce el primer número: ")
    n2 = input("Introduce el segundo número: ")
    dividir_con_manejo(n1, n2)
