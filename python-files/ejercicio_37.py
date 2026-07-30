# -------------------------------------------------------------------------------------------
# KATA 37
#
# Genera un programa que nos indique si es de noche, de día o de tarde
# según la hora proporcionada por el usuario.
# -------------------------------------------------------------------------------------------


def periodo_del_dia(hora):
    """
    Recibe una hora (0-23) y devuelve si es "día", "tarde" o "noche",
    según las franjas: día 6h-14h, tarde 14h-22h, noche 22h-6h
    (24 horas repartidas en 3 franjas de 8 horas cada una).
    """
    if 6 <= hora < 14:
        return "día"
    elif 14 <= hora < 22:
        return "tarde"
    elif 22 <= hora < 24:
        return "noche"
    elif 0 <= hora < 6:
        return "noche"
    else:
        # opción para cualquier otra "hora" que este
        # fuera del rango horario (0-23)
        return "se encuentra fuera del rango horario (0-23)"


if __name__ == "__main__":
    horas_prueba = [10, 18, 2, 23, 6, 14, 22]
    print("- Lista con horas de prueba -")
    for hora in horas_prueba:
        print(f"Hora: {hora}h -> Resultado: {periodo_del_dia(hora)}")

    # Para usarlo de forma interactiva, ingreso por input():
    print("\n- Ingreso de la hora por usuario -")
    hora_usuario = int(input("Introduce la hora (0-23): "))
    print("Resultado:", periodo_del_dia(hora_usuario))

# -------------------------------------------------------------------------------------------
# EXTRA
#
# Desbloquear esta sección para probarlo (formato hh:mm)
# ========================================
# def periodo_del_dia(minutos_totales):
3
#     if 360 <= minutos_totales < 840:  # rango 6:00 - 13:59
#         return "día"
#     elif 840 <= minutos_totales < 1320:  # rango 14:00 - 21:59
#         return "tarde"
#     elif 1320 <= minutos_totales < 1440:  # rango 22:00 - 23:59
#         return "noche"
#     elif 0 <= minutos_totales < 360:  # rango 00:00 - 05:59
#         return "madrugada"
#     else:
#         return "Se encuentra fuera del rango horario (00:00 - 23:59)"

# print("\n- Ingreso de la hora en formato 'hh:mm' -")
# texto = input("Introduce una hora (Ejemplo 12:35): ")
# partes = texto.split(":")  # -> separa ['12', '35']
# horas = int(partes[0])  # -> 12
# minutos = int(partes[1])  # -> 35
# minutos_totales = horas * 60 + minutos  # -> 755
# print("Resultado:", periodo_del_dia(minutos_totales))
# ========================================
# Realicé esto como "curiosidad" mía, por otro lado, no creo que
# alguien escriba 38:65 ¿oh sí?, para evitarlo agregué + elif
# y así darle consistencia al rango horario.
# Solo faltaría corregir si ingresan más de 59 minutos, por
# ejemplo: 14:89 es de ¿tarde? (929 minutos)
