# Comentarios y desarrollo

## Pasos seguidos durante el proyecto

### Paso 1: Planificación y configuración inicial

- [x] Creación del repositorio local y remoto en GitHub.

- [x] Configuración del entorno de desarrollo y estructura del proyecto.

- [x] Creación del panel de control base `main.py`.

### Paso 2: Desarrollo de los ejercicios

**Bloque 1 (Ejercicios 01-16):** *fundamentos sin dependencias externas*

- Tipos de datos (diccionarios, tuplas, conjuntos)
- Funciones lambda combinadas con `map()`/`filter()`
- Manejo de excepciones (incorporadas y personalizadas) y recursividad.
- Todo usando solo funciones incorporadas de Python, sin necesidad de ningún import.

**Bloque 2 (Ejercicios 17-33):** *módulos externos y estructuras avanzadas*

- Uso de `functools reduce()`, primer módulo que requiere `import`.
- Uso de `isinstance()`, slicing con índices negativos, `sorted()` para comparar contenido.
- Listas de diccionarios y excepciones personalizadas algo más elaboradas.

**Bloque 3 (Ejercicios 34-40):** *Programación Orientada a Objetos y función `*args`*

- Clases en POO (Arbol y UsuarioBanco)
- función despachadora con `*args` (argumentos variables), y
- Condicionales con franjas/rangos.

### Dificultades encontradas y soluciones

#### `__init__.py` y `main.py`

`__init__.py`: Este es un archivo vacío que **declara** que python-files/ es un paquete de Python, para que `runpy` pueda encontrar y ejecutar los módulos dentro.

`main.py`: Este viene a ser el **panel de control** que permite lanzar cualquiera de los ejercicios desde un único punto de entrada, siendo el rango de ejercicios (desde el 1 hasta el 40), si no está creado avisará en lugar de fallar.

- **Dificultad:** Mi propuesta me ocasionó un aprendizaje interezante, puesto que al ejecutar los ejercicios desde `main.py` mediante un `import` normal (`importlib.import_module`), el bloque de prueba `if __name__ == "__main__":` de cada ejercicio no se ejecutaba, debido a que al importar un módulo su `__name__` pasa a ser la ruta del paquete (por ejemplo: "python-files.ejercicio_01"), no `__main__`.
- **Solución:** Reemplazé por `runpy.run_module(ruta, run_name="__main__")`, que fuerza que `__name__` valga `__main__` al ejecutar el módulo elegido, disparando correctamente la demostración.

#### Ejercicio 01

Función que cuenta la frecuencia de letras de una cadena usando un diccionario, sin distinguir mayúsculas/minúsculas y sin contar espacios (`str.lower()` + `dict.get()`).

- **Dificultad:** Al principio pensé en usar `if/else` con `continue` para saltar los espacios al contar letras.
- **Solución:** Simplifiqué invirtiendo la condición ( if letra != " ": ), evitando el `continue` y quedando el código más compacto.

- **Dificultad:** Python distingue mayúsculas de minúsculas ("P" ≠ "p"), lo que duplicaría letras iguales en el conteo si no se controla.
- **Solución:** Por lo tanto, normalizo la cadena completa a minúsculas con `.lower()` antes de empezar a contar.

---

#### Limpiar pantalla

- **Dificultad:** Al ejecutar un ejercicio desde `main.py`, la salida aparecía debajo del panel anterior sin limpiar la pantalla, generando texto acumulado y desordenado.
- **Solución:** Añado `limpiar_pantalla()` (usa `cls` en Windows y `clear` en Linux/Mac según `os.name`), que es llamada antes de mostrar el panel y antes de ejecutar cada ejercicio.

---

#### Parpadeo en `main.py`

- **Dificultad:** Los mensajes de "ejercicio todavía no creado" y "opción no válida" en `main.py` aparecían y desaparecían casi instantáneamente ("parpadeo"), porque la siguiente vuelta del bucle limpiaba la pantalla antes de que se pudieran leer.

- **Solución:** Añadí `input("Pulsa Enter para continuar...")` justo después de esos dos mensajes, igual que ya existía tras ejecutar un ejercicio, para pausar hasta que el usuario decida continuar.

---

#### Ejercicio 6

- **Dificultad:** Encuentro la necesidad de utilizar el "caso base", de lo contrario, el factorial pediría `n-1` indefinidadmente en la formula `n! = n * factorial(n-1)`, provocando error.
- **Solución:** Calculo el factorial de forma recursiva con caso base `0! = 1` (ejemplo visual al final del propio script).

---

#### Ejercicio 11

- **Dificultad:** Para calcular el rango utilizo: `edad > 0 or edad < 120`, pero encuentro un error de lógica en esta condición (ver ejemplo visual al final del script).
- **Solución:** Cambio por un rango válido: `0<= edad <= 120`, que resuelve bien si se ingresa una edad "negativa", porque `or` entre dos condiciones tan amplias termina siendo casi siempre `True` para cualquier número.

---

#### Ejercicio 12

- **Dificultad:** En principio utilicé **lambda**, aunque investigando un poco, encontré una mejora en `map()`.
- **Solución:** Aplico `len()` dentro del `map()`, ejemplo: `map(len, lista_palabras)`, puesto que `len()` también es una función lista para usar directamente con `map()` como `str()`, tal y como se ve en el ejercicio 7 pasado, **sin lambda**.

---

#### Ejercicio 14

- **Dificultad:** Para este ejercicio pensé primero en la indexación `palabra[0] == letra` (por la posición), pero resulta que Python tiene un método hecho justo para esto, más legible y seguro.
- **Solución:** Investigando, encontré el método `.startswith()` de los strings, que devuelve True/False según si el texto empieza por el prefijo indicado (más seguro que comparar `palabra[0]`, que fallaría con una palabra vacía).

---

#### Ejercicio 15

- **Dificultad:** Para este ejercicio, intenté definir una función que hacía `return lambda lista_num: [...]`, devolviendo el lambda como objeto sin ejecutarlo nunca.
- **Solución:** Separo el lambda (que opera sobre un solo número) del uso de `map()` (que lo aplica a toda la lista). Si lo dejo dentro de la función `def`, lo devuelve sin usarlo.

---

#### Ejercicio 18

- **Dificultad:** Al principio intenté escribir las claves del diccionario sin comillas (`{nombre: "Jose", ...}`) y accedí a un valor con paréntesis (`estudiante(calificacion)`), como si fuera una llamada a función. Sí, muy mal.
- **Solución:** Corregí el error, puesto que las claves de un diccionario son strings y deben ir entre comillas (`{"nombre": "Jose", ...}`), y para leer un valor por su clave se usan corchetes, no paréntesis (`estudiante["calificacion"]`). Ahora sí.

---

#### Ejercicio 20

- **Dificultad:** Por desconocimiento inicial, creía que era un **método** cuando es **una función independiente**, escribí `elemento.isinstance(elemento, int)`, con el punto, dando el error `AttributeError: 'str' object has no attribute 'isinstance'`.
- **Solución:** Al saber que `isinstance(valor, tipo)` es una función independiente de Python (como `len()` o `str()`), entonces cambio `elemento.isinstance(elemento, int)` por `isinstance(elemento, int)`, pasando el valor como argumento.

---

#### Ejercicio 28

- **Dificultad:** Al principio intento plantear `set(elementos)` sobre toda la lista para buscar el duplicado, pero recuerdo que `set()` elimina el orden y no distingue "cuál se repitió primero", es decir, solo da los valores únicos, sin información sobre repetición ni posición.
- **Solución:** Usé un `set()` vacío como "memoria de vistos", recorrido con un `for` en orden, osea, para cada elemento se comprueba si ya está en "vistos" (duplicado encontrado) o lo añade por primera vez.

---

#### Ejercicio 31

- **Dificultad:** En este ejercicio no me quedaba claro cómo pedir al usuario varios nombres, es decir, la lista completa usando `input()`, ya que hasta ahora solo se había pedido un valor por línea, honestamente estuve muy liado.
- **Solución:** En mi busqueda, encuentro que la mejor forma es pedir toda la lista es **en una sola línea y separada por comas**, luego se separa con `.split(",")`; además aplico `.strip()` a cada nombre para quitar los espacios sobrantes que quedan tras la coma (aprendí que sin esto, "Ana, Luis" generaría " Luis" con un espacio al inicio, y una búsqueda de "Luis" fallaría aunque esté en la lista).

---

#### Ejercicio 34

- **Dificultad:** Al empezar el ejercicio 34 (primera clase del proyecto), tuve una tremenda confusión sobre lo qué es una clase y para qué sirve, incluso creía que hablábamos de un árbol de directorios (carpetas). También me surgió la duda de cómo modificar cada elemento de una lista (no solo leerlo) dentro de un método, vaya!.
- **Solución:** Luego de profundizar en el tema, aclaro el concepto de clase (en resumen la clase define la plantilla; cada objeto tiene sus propios datos). Luego, para modificar elementos de una lista aplico un `for` por índice (`for i in range(len(lista)): y lista[i] += 1`), en vez de for elemento in lista:, que solo daría copias temporales de lectura.

---

#### Ejercicio 37

- **Dificultad:** Cuando busco ampliar este ejercicio para que acepte el formato `hh:mm`, un primer intento aplicó `int()` sobre el texto completo antes de separarlo por **':'** `texto = int(input(...))`, dando `ValueError: invalid literal for int() with base 10: '14:10'`, ya que **':'** no es parte de un número entero válido.
- **Solución:** El texto se mantiene como string y se separa primero con `.split(":")`; solo cada parte por separado (horas, minutos) se convierte a `int()` después de separarlas.

---

#### Ejercicio 40

- **Dificultad:** Cuando pruebo con respuestas inválidas ("quizas", "ss", "nn", "quiza") en distintos casos, el programa se rompía en varios de ellos (traceback), y además escribir "si" (o cualquier cosa) como precio en el bloque interactivo también rompía el programa.
- **Solución:** Incluyo todos los casos por igual mediante un bucle `for` sobre una lista de "casos de prueba". Además, en el bloque interactivo, modifico el `try/except` para cubrir también la conversión `float()` del precio (que puede fallar con ValueError igual que la validación de "si"/"no").

---

## Autor 👨‍💻

- **Nombre:** José Gabriel Ternero Sifuentes

- **Curso:** 2º ASIR — **PROMETEO FP** *by The Power*

- **Máster:** Ciberseguridad — **Prometeo Cyber** *by Antonio Rosales*

- **GitHub:** [GabTS75](https://github.com/GabTS75)

> ✨ « Siempre parece imposible hasta que se consigue » ✨
