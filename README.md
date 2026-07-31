# Indicaciones para el Proyecto 3

## Katas Python

Este **tercer proyecto** consiste en completar, validar y entregar **todos los ejercicios de Python** que os planteamos a continuación.

Una vez terminado tendréis que enviar el proyecto a `antonio.rosales@thepower.education` con el asunto **Proyecto 3: Katas Python - Vuestro nombre** y en el cuerpo del correo el **link** de un **repositorio de GitHub**.

### ¿Cómo enfocar las katas?

Las katas pueden hacerse de distintas maneras para obtener el mismo resultado. A lo largo del proyecto debes demostrar los siguientes conocimientos:

- Manejo de tipos de datos básicos y funciones incorporadas.
- Manejo de estructuras de datos en Python y sus métodos.
- Manejo de condicionales.
- Manejo de estructuras de iteración
- Manejo de funciones en Python.
- Manejo de Clases y entendimiento de la programación orientada a objetos.
- Uso de módulos.
- Buenas prácticas.

> ❗️ Es importante que demuestres un entendimiento de tu código, recuerda poner comentarios explicativos de los pasos que más te hayan costado.
>
> ❗️❗️ El uso de herramientas de **IA** está permitido pero recuerda que este proyecto está pensado para que afiances tus conocimientos en **Python**, asegúrate de usar estás herramientas con moderación y de que entiendes todos los pasos que has seguido.

### Método de entrega

Tu repositorio tiene que constar, al menos, de los siguientes archivos/carpetas:

- **Comentarios** que recojan los pasos seguidos durante el proyecto.
- **Un archivo .py** con los ejercicios resueltos.
- Cada ejercicio tiene que ir encabezado con un comentario con el enunciado del ejercicio.

---

### PROPUESTA DE DESARROLLO: Estructura para la entrega

Repositorio preparado y listo para la entrega del **Proyecto 3: Katas Python** del Máster _by Antonio Rosales_.

Proyecto con la resolución de **40 ejercicios de programación en Python**, abarcando progresivamente tipos de datos y estructuras, funciones `lambda`/`map`/`filter`/`reduce`, manejo de condicionales y excepciones (incorporadas y personalizadas), recursividad, clases, programación orientada a objetos (POO) y modularización — con un registro detallado del proceso y las dificultades encontradas en `comentarios.md`.

Además, incluí para el proyecto, un **panel de control** `main.py` para ejecutar cualquier ejercicio de forma interactiva, con el objetivo de facilitar la corrección y evaluación.

```bash
📂 Proyecto3-Katas-Python   # nombre del repositorio principal
├── 📂 python-files/        # Carpeta con todos los módulos (ejercicios)
│   ├── 📄 __init__.py      # archivo que enlaza los módulos (ejercicios) al menú
│   ├── 📄 ejercicio_01.py
│   ├── 📄 ejercicio_02.py
│   ├── 📄 ejercicio_03.py
│   ├── ...
│   └── 📄 ejercicio_40.py
├── comentarios.md          # Interacción progresiva de los pasos seguidos
├── main.py                 # Panel interactivo para ejecutar los ejercicios
└── README.md               # Indicaciones del proyecto (este mismo)
```

### Pasos previos para la ejecución correcta

En la carpeta principal del proyecto `Proyecto3-Katas-Python`, abre el terminal de tu Sistema Operativo (Windows o Linux) y desde allí sigue las siguientes indicaciones:

```bash
# En Windows, escribimos en el CMD (terminal) lo siguiente:
python --version

# Si no lo tenemos, instalamos Python 3 siguiendo los pasos:
# Abre el navegador y descarga el ejecutable desde python.org, luego ejecuta
# el instalador y asegurate de marcar "Add Python to PATH" antes de instalar.

# Para ejecutar el script escribiremos:
python main.py

# También se puede ejecutar individualmente (opcional)
python python-files/ejercicio_01.py
```

```bash
# En Linux, abrimos el terminal (Ctrl + Alt + T) y escribimos:
python --version

# Por lo general viene siempre pre-instalado Python en Linux

# Para ejecutar el script, escribimos:
python3 main.py
```

---

> **NOTA:** También es posible ejecutarlo en el mismo **Visual Studio Code**, abriendo un terminal (**CTRL + ñ**) en la carpeta principal del repositorio y ejecutar `python main.py` o `python3 main.py` tal y como se muestra en la siguiente imagen. 👇

![VSCode_img1.jpg](./python-files/imgs/img1.jpg)

> Debería mostrarse así:

![VSCode_img2.jpg](./python-files/imgs/img2.jpg)

---

### Entorno de Desarrollo

- **Lenguaje:** Python 3.x
- **Editor:** Visual Studio Code
- **Control de Versiones:** Git & GitHub
- **Sistema Operativo:** Windows / Ubuntu
