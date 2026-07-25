# ----------------------------------------------------------------------
# main.py - Panel de control del Proyecto 3: Katas Python
#
# Permite elegir un ejercicio por número (1-40), lo ejecuta, y vuelve
# automáticamente a este panel para elegir otro (o salir con "S").
# ----------------------------------------------------------------------

import os
import runpy

CARPETA_EJERCICIOS = "python-files"
TOTAL_EJERCICIOS = 40


def nombre_modulo(numero):
    """
    Convierte un número de ejercicio (ej: 2) en el nombre de archivo
    esperado (ej: 'ejercicio_02'), usando :02d para rellenar con un
    cero a la izquierda si hace falta (1 -> '01', 12 -> '12').
    """
    return f"ejercicio_{numero:02d}"


def ejercicio_existe(numero):
    """
    Comprueba si el archivo del ejercicio elegido ya está creado en
    python-files/. Así el panel no falla si eliges un número de un
    ejercicio que todavía no has resuelto.
    """
    ruta = os.path.join(CARPETA_EJERCICIOS, nombre_modulo(numero) + ".py")
    return os.path.isfile(ruta)


def ejecutar_ejercicio(numero):
    """
    Ejecuta el ejercicio elegido como si lo hubieras lanzado directamente
    con "python ejercicio_XX.py" (ver explicación de runpy más abajo).
    """
    ruta_paquete = f"{CARPETA_EJERCICIOS}.{nombre_modulo(numero)}"
    runpy.run_module(ruta_paquete, run_name="__main__")
    # runpy.run_module con run_name="__main__" hace que, para ESE archivo,
    # __name__ valga "__main__" al ejecutarlo. Un import normal no lo haría
    # (el __name__ pasaría a ser la ruta del paquete), así que el bloque
    # if __name__ == "__main__": de cada ejercicio no se dispararía.


def limpiar_pantalla():
    """
    Limpia la terminal: 'cls' en Windows, 'clear' en Linux/Mac.
    os.name vale 'nt' en Windows y 'posix' en Linux/Mac.
    """
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_panel():
    print("\n" + "=" * 40)
    print("------ PROYECTO 3: KATAS PYTHON ------")
    print(f"---- Panel de Control | {TOTAL_EJERCICIOS} scripts ----")
    print("=" * 40)
    print(f"Elige un ejercicio (del 1 al {TOTAL_EJERCICIOS})")
    print('Elige "S" para Salir')
    print("=" * 40)


def main():
    while True:  # <- volvemos aquí tras cada ejecución
        limpiar_pantalla()  # pantalla limpia antes de mostrar el panel
        mostrar_panel()
        eleccion = input("Elige un ejercicio (número): ").strip()

        if eleccion.lower() == "s":
            print("¡Hasta la próxima!")
            break

        if not eleccion.isdigit() or not (1 <= int(eleccion) <= TOTAL_EJERCICIOS):
            print(
                f'Opción no válida. Escribe un número entre 1 y {TOTAL_EJERCICIOS}, o "S" para salir.'
            )
            continue

        numero = int(eleccion)

        if not ejercicio_existe(numero):
            print(f"El ejercicio {numero} todavía no está creado.")
            continue

        limpiar_pantalla()  # pantalla limpia antes de mostrar el resultado
        print(f"\n--- Ejecutando {nombre_modulo(numero)} ---\n")
        ejecutar_ejercicio(numero)
        input("\nPulsa Enter para volver al panel...")


if __name__ == "__main__":
    main()
