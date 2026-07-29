# -------------------------------------------------------------------------------------------
# KATA 29
#
# Crea una función que convierta una variable en una cadena de texto y
# enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
# -------------------------------------------------------------------------------------------


def enmascarar(variable):
    """
    Convierte la variable recibida a texto y devuelve una nueva cadena
    con todos los caracteres reemplazados por '#', excepto los últimos
    4, que se mantienen visibles.
    """
    texto = str(variable)
    oculto = texto[:-4]  # oculta todo menos los últimos 4 caracteres
    visible = texto[-4:]  # deja visible los últimos 4 caracteres
    return "#" * len(oculto) + visible
    # repite '#' las veces como caracteres tenga "oculto" y le suma "visible"

if __name__ == "__main__":
    valor_1 = "1234567890123456"
    print("Variable:", valor_1)
    print("Resultado (enmascarado):", enmascarar(valor_1))

    # Si el texto tiene 4 caracteres o menos, texto[:-4] queda vacío de
    # forma natural, así que no se enmascara nada (no hay nada que esté
    # "de más" para ocultar).
    valor_2 = 789
    print("\nVariable:", valor_2)
    print("Resultado (enmascarado):", enmascarar(valor_2))

# -------------------------------------------------------------------------------------------
# EXTRA
#
# Slicing ("rebanado", cortar cadenas por posición): es una función para cortar
# y extraer partes de una secuencia, como listas, cadenas de texto o tuplas.
# 
# Estructura general del corte: secuencia[inicio:fin:paso] (Start, Stop, Step),
# Si dejamos "vacío" Step, el valor por defecto es 1 (de uno en uno)
# 
# En principio podemos "cortar" la cadena con texto[inicio:fin]. Además, usaremos
# los índices negativos, los cuales cuentan desde el final hacia atrás (inicio):
# texto[-1] es el último carácter, texto[-4] es el cuarto empezando por el final.
#
# Entonces tenemos, dos cortes:
#
# texto[:-4] → todo menos los últimos 4 caracteres (la parte a enmascarar).
# Es como decir "desde el principio, hasta 4 antes del final".
#
# texto[-4:] → solo los últimos 4 caracteres (la parte visible). "Desde 4 antes
# del final, hasta el final".
