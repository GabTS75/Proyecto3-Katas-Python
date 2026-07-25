# Comentarios y desarrollo

## Pasos seguidos durante el proyecto

### Paso 1: Planificación y configuración inicial

- [x] Creación del repositorio local y remoto en GitHub.

- [x] Configuración del entorno de desarrollo y estructura del proyecto.

- [x] Creación del panel de control base (main.py).

### Paso 2: Desarrollo de los ejercicios

- **Ejercicios A al B:** - POR DEFINIR [Ejemplo: Sintaxis básica, entrada/salida de datos y estructuras condicionales (if/else).]

- **Ejercicios C al D:** - POR DEFINIR [Ejemplo: Bucles (for/while) y manipulación de cadenas.]

- **Ejercicios E al F:** - POR DEFINIR [Ejemplo: Estructuras de datos (listas, tuplas y diccionarios).]

- **Ejercicios G al H:** - POR DEFINIR [Ejemplo: Funciones, gestión de errores y modularidad.]

### Dificultades encontradas y soluciones

#### `__init__.py` y `main.py`

`__init__.py`: Este es un archivo vacío que **declara** que python-files/ es un paquete de Python, para que `runpy` pueda encontrar y ejecutar los módulos dentro.

`main.py`: Este viene a ser el **panel de control** que permite lanzar cualquiera de los ejercicios desde un único punto de entrada, siendo el rango de ejercicios (desde el 1 hasta el 40), si no está creado avisará en lugar de fallar.

- **Dificultad:** Mi propuesta me ocasionó un aprendizaje interezante, puesto que al ejecutar los ejercicios desde `main.py` mediante un `import` normal (`importlib.import_module`), el bloque de prueba `if __name__ == "__main__":` de cada ejercicio no se ejecutaba, debido a que al importar un módulo su `__name__` pasa a ser la ruta del paquete (por ejemplo: "python-files.ejercicio_01"), no `__main__`.
- **Solución:** Se reemplazó por `runpy.run_module(ruta, run_name="__main__")`, que fuerza que `__name__` valga `__main__` al ejecutar el módulo elegido, disparando correctamente la demostración.

#### Ejercicio 01

Función que cuenta la frecuencia de letras de una cadena usando un diccionario, sin distinguir mayúsculas/minúsculas y sin contar espacios (`str.lower()` + `dict.get()`).

- **Dificultad:** Al principio pensé en usar `if/else` con `continue` para saltar los espacios al contar letras.
- **Solución:** Simplifiqué invirtiendo la condición ( if letra != " ": ), evitando el `continue` y quedando el código más compacto.

- **Dificultad:** Python distingue mayúsculas de minúsculas ("P" ≠ "p"), lo que duplicaría letras iguales en el conteo si no se controla.
- **Solución:** Por lo tanto, normalizo la cadena completa a minúsculas con `.lower()` antes de empezar a contar.

---

#### Limpiar pantalla

- **Dificultad:** Al ejecutar un ejercicio desde `main.py`, la salida aparecía debajo del panel anterior sin limpiar la pantalla, generando texto acumulado y desordenado.
- **Solución:** Se añadió `limpiar_pantalla()` (usa `cls` en Windows y `clear` en Linux/Mac según `os.name`), llamada antes de mostrar el panel y antes de ejecutar cada ejercicio.

---

#### Parpadeo en `main.py`

- **Dificultad:** Los mensajes de "ejercicio todavía no creado" y "opción no válida" en `main.py` aparecían y desaparecían casi instantáneamente ("parpadeo"), porque la siguiente vuelta del bucle limpiaba la pantalla antes de que se pudieran leer.

- **Solución:** Se añadió `input("Pulsa Enter para continuar...")` justo después de esos dos mensajes, igual que ya existía tras ejecutar un ejercicio, para pausar hasta que el usuario decida continuar.

---

etc. ...

---

## Autor 👨‍💻

- **Nombre:** José Gabriel Ternero Sifuentes

- **Curso:** 2º ASIR — **PROMETEO FP** by _The Power_

- **GitHub:** [GabTS75](https://github.com/GabTS75)
