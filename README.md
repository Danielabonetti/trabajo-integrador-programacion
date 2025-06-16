# Algoritmos de Búsqueda y Ordenamiento en Python

## 🚀 Resumen del Proyecto

Este proyecto es un análisis exhaustivo y una implementación práctica de diversos algoritmos de búsqueda y ordenamiento fundamentales en el ámbito de la programación. Desarrollado en Python, tiene como objetivo principal comparar el rendimiento de estos algoritmos en diferentes escenarios y evaluar su impacto en la eficiencia de la manipulación y organización de datos. La correcta aplicación de estos algoritmos es crucial para la optimización de software y la gestión eficiente de grandes volúmenes de información en diversas aplicaciones, desde bases de datos hasta sistemas inteligentes.

## 🎯 Objetivos

* **Analizar y aplicar** distintos métodos de búsqueda (Lineal, Binaria, Interpolación) y ordenamiento (Burbuja, Inserción, Selección, Quick Sort, Merge Sort) en Python.
* **Comparar el desempeño** de cada algoritmo en función del tamaño de los datos de entrada, identificando sus fortalezas y debilidades.
* **Comprender en profundidad** los principios que rigen cada algoritmo y su complejidad computacional.
* **Optimizar el código** y tomar decisiones informadas en el diseño de software para mejorar la eficiencia y el rendimiento de las aplicaciones.

## ⚙️ Algoritmos Implementados

El proyecto implementa y evalúa los siguientes algoritmos:

### Algoritmos de Búsqueda

* **Búsqueda Lineal:** Un método simple que revisa secuencialmente cada elemento de la lista hasta encontrar el objetivo.
* **Búsqueda Binaria:** Requiere que la lista esté ordenada. Divide repetidamente por la mitad la porción de la lista que podría contener el elemento hasta encontrarlo.
* **Búsqueda por Interpolación:** Una mejora de la búsqueda binaria para listas uniformemente distribuidas, que estima la posición del objetivo de manera más inteligente.

### Algoritmos de Ordenamiento

* **Bubble Sort (Ordenamiento Burbuja):** Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto, repitiendo el proceso hasta que la lista esté ordenada.
* **Insertion Sort (Ordenamiento por Inserción):** Construye la lista ordenada un elemento a la vez, insertando cada elemento en su posición correcta en la parte ya ordenada.
* **Selection Sort (Ordenamiento por Selección):** Encuentra el elemento mínimo (o máximo) en la parte no ordenada de la lista y lo coloca al principio de la parte ordenada.
* **Quick Sort (Ordenamiento Rápido):** Un algoritmo eficiente que utiliza la estrategia de "divide y vencerás", seleccionando un "pivote" y particionando la lista en elementos menores y mayores que el pivote.
* **Merge Sort (Ordenamiento por Mezcla):** Otro algoritmo de "divide y vencerás" que divide la lista en mitades, las ordena recursivamente y luego las combina.

## 💻 Estructura del Proyecto

El proyecto se compone de dos archivos principales:

* `algoritmos.py`: Contiene las implementaciones en Python de cada uno de los algoritmos de búsqueda y ordenamiento.
* `analisis.py`: Script encargado de realizar las pruebas de rendimiento. Genera listas aleatorias de diferentes tamaños, mide el tiempo de ejecución de cada algoritmo y muestra los resultados en la consola.

## 🛠️ Requisitos

Para ejecutar este proyecto, solo necesitas tener Python instalado en tu sistema.

* **Python 3.x**

## 🚀 Cómo Ejecutar el Proyecto

Sigue estos pasos para poner en marcha y probar los algoritmos:

1.  **Clonar el Repositorio (si aplica):**
    Si este proyecto se encuentra en un repositorio, clónalo a tu máquina local:
    ```bash
    git clone [https://github.com/Danielabonetti/trabajo-integrador-](https://github.com/Danielabonetti/trabajo-integrador-)...  # Reemplaza con el enlace real si es diferente
    cd nombre-del-repositorio
    ```

2.  **Navegar al Directorio del Proyecto:**
    Asegúrate de estar en el directorio donde se encuentran `algoritmos.py` y `analisis.py`.

3.  **Ejecutar el Script de Análisis:**
    Abre tu terminal o línea de comandos y ejecuta el siguiente comando:
    ```bash
    python analisis.py
    ```

    El script `analisis.py` imprimirá en la consola los tiempos promedio de ejecución de cada algoritmo para diferentes tamaños de listas, tanto para búsqueda como para ordenamiento.

## 📊 Resultados Esperados

Al ejecutar `analisis.py`, verás una comparación de los tiempos de ejecución promedio para cada algoritmo en listas de diferentes tamaños (1000, 5000, 10000, 50000 elementos).

**Ejemplo de Salida (formato simplificado):**
Comparación de Algoritmos de Búsqueda (Elementos Existentes)
Nota: Para búsqueda binaria e interpolación, las listas se ordenan previamente.
Probando con tamaño de lista: 1000
Búsqueda Lineal: 0.000050 segundos
Búsqueda Binaria: 0.000002 segundos
Búsqueda Interpolación: 0.000001 segundos
Probando con tamaño de lista: 5000
Búsqueda Lineal: 0.000250 segundos
Búsqueda Binaria: 0.000003 segundos
Búsqueda Interpolación: 0.000002 segundos
...

Comparación de Algoritmos de Ordenamiento
Probando con tamaño de la lista: 1000
Bubble Sort: 0.080000 segundos
Insertion Sort: 0.040000 segundos
Selection Sort: 0.060000 segundos
Quick Sort: 0.000500 segundos
Merge Sort: 0.000700 segundos
...

*(Los valores de tiempo son solo ejemplos y variarán según el hardware y las ejecuciones.)*

## 💡 Conclusiones del Proyecto

Dominar estos algoritmos es fundamental para optimizar el código y tomar decisiones informadas en el diseño de software. Este conocimiento es directamente aplicable a futuros proyectos que manejen grandes volúmenes de datos, mejorando significativamente la eficiencia y el rendimiento de las aplicaciones.

Se observó que los algoritmos de búsqueda avanzada (Binaria, Interpolación) superan en rendimiento a la Búsqueda Lineal en listas ordenadas, especialmente a medida que aumenta el tamaño de la lista. En cuanto a los algoritmos de ordenamiento, Quick Sort y Merge Sort demostraron ser consistentemente más eficientes que Bubble Sort, Insertion Sort y Selection Sort para listas de mayor tamaño, debido a su menor complejidad temporal.

## 📈 Mejoras y Extensiones Futuras

Este proyecto puede ser ampliado y mejorado de diversas maneras:

* **Implementación de más algoritmos:**
    * **Ordenamiento:** Heap Sort, Radix Sort, Counting Sort.
    * **Búsqueda:** Búsqueda Hash.
* **Visualización de resultados:** Creación de gráficos comparativos del rendimiento de los algoritmos utilizando librerías como `matplotlib` o `seaborn`.
* **Casos de prueba adicionales:** Evaluar el rendimiento con listas parcialmente ordenadas, listas ya ordenadas, o listas inversamente ordenadas.
* **Análisis de memoria:** Medir el consumo de memoria de cada algoritmo además del tiempo de ejecución.
* **Interfaz de usuario:** Desarrollar una interfaz gráfica simple para facilitar la interacción y visualización de los resultados.

## 🤝 Contribuciones

Este proyecto fue desarrollado por:

* **Cabrera Ezequiel Dario** - dario.cabrera17@gmail.com
* **Bonetti Kunt Daniela Sofia** - danielabonetti51@gmail.com

**Materia:** Programación I
**Profesor/a:** Prof. Cinthia Rigoni
**Fecha de Entrega:** 09/06/2025

## 📚 Bibliografía

Para la elaboración de este trabajo, se consultó la siguiente información:

* Material del aula virtual: PDFs y archivos Collab proporcionados en el curso de Programación I.
* Apuntes de clase y recursos complementarios sobre algoritmos de búsqueda y ordenamiento.

## 🔗 Anexos

* **Video Explicativo del Proyecto:**
    [https://youtu.be/LmWDORWYyJE](https://youtu.be/LmWDORWYyJE) (Enlace de ejemplo, por favor, reemplaza con el enlace real de YouTube si es diferente)
* **Código Fuente Completo del Proyecto:**
    [https://github.com/Danielabonetti/trabajo-integrador-...](https://github.com/Danielabonetti/trabajo-integrador-...) (Enlace del repositorio de GitHub, por favor, reemplaza con el enlace real si es diferente)
