import time
import random
from algoritmos import (
    busqueda_lineal,
    busqueda_binaria,
    busqueda_interpolacion,
    bubble_sort,
    insertion_sort,
    selection_sort,
    quick_sort,
    merge_sort
)


# Tamaños de lista para evaluar el rendimiento de los algoritmos.
TAMANOS_LISTA = [1000, 5000, 10000, 50000]

NUM_PRUEBAS = 3

def generar_lista_aleatoria(tamano):
    return [random.randint(0, tamano * 2) for _ in range(tamano)]

def medir_tiempo(algoritmo, *args, **kwargs):
    
    inicio = time.perf_counter()
    algoritmo(*args, **kwargs)
    fin = time.perf_counter()
    return fin - inicio

#Pruebas de Algoritmos de Búsqueda
print("Comparación de Algoritmos de Búsqueda (Elementos Existentes)")
print("Nota: Para búsqueda binaria e interpolación, las listas se ordenan previamente.")

for tamano in TAMANOS_LISTA:
    print(f"Probando con tamaño de lista: {tamano}")
    lista_original = generar_lista_aleatoria(tamano)
    
    elemento_a_buscar = random.choice(lista_original)

    lista_ordenada = sorted(lista_original)

    # Búsqueda Lineal
    tiempos_lineal = []
    for _ in range(NUM_PRUEBAS):
        tiempos_lineal.append(medir_tiempo(busqueda_lineal, lista_original, elemento_a_buscar))
    print(f"  Búsqueda Lineal: {sum(tiempos_lineal) / NUM_PRUEBAS:.6f} segundos")

    # Búsqueda Binaria
    tiempos_binaria = []
    for _ in range(NUM_PRUEBAS):
        tiempos_binaria.append(medir_tiempo(busqueda_binaria, lista_ordenada, elemento_a_buscar))
    print(f"  Búsqueda Binaria: {sum(tiempos_binaria) / NUM_PRUEBAS:.6f} segundos")

    # Búsqueda por Interpolación
    tiempos_interpolacion = []
    for _ in range(NUM_PRUEBAS):
        tiempos_interpolacion.append(medir_tiempo(busqueda_interpolacion, lista_ordenada, elemento_a_buscar))
    print(f"  Búsqueda por Interpolación: {sum(tiempos_interpolacion) / NUM_PRUEBAS:.6f} segundos")

# Pruebas de Algoritmos de Ordenamiento
print("Comparación de Algoritmos de Ordenamiento")

for tamano in TAMANOS_LISTA:
    print(f"tamaño de la lista: {tamano}")


    # Bubble Sort
    tiempos_bubble = []
    for _ in range(NUM_PRUEBAS):
        lista_test = generar_lista_aleatoria(tamano)
        tiempos_bubble.append(medir_tiempo(bubble_sort, lista_test.copy()))
    print(f"  Bubble Sort: {sum(tiempos_bubble) / NUM_PRUEBAS:.6f} segundos")

    # Insertion Sort
    tiempos_insertion = []
    for _ in range(NUM_PRUEBAS):
        lista_test = generar_lista_aleatoria(tamano)
        tiempos_insertion.append(medir_tiempo(insertion_sort, lista_test.copy()))
    print(f"  Insertion Sort: {sum(tiempos_insertion) / NUM_PRUEBAS:.6f} segundos")

    # Selection Sort
    tiempos_selection = []
    for _ in range(NUM_PRUEBAS):
        lista_test = generar_lista_aleatoria(tamano)
        tiempos_selection.append(medir_tiempo(selection_sort, lista_test.copy()))
    print(f"  Selection Sort: {sum(tiempos_selection) / NUM_PRUEBAS:.6f} segundos")

    # Quick Sort
    tiempos_quick = []
    for _ in range(NUM_PRUEBAS):
        lista_test = generar_lista_aleatoria(tamano)
        tiempos_quick.append(medir_tiempo(quick_sort, lista_test.copy()))
    print(f"  Quick Sort: {sum(tiempos_quick) / NUM_PRUEBAS:.6f} segundos")

    # Merge Sort
    tiempos_merge = []
    for _ in range(NUM_PRUEBAS):
        lista_test = generar_lista_aleatoria(tamano)
        tiempos_merge.append(medir_tiempo(merge_sort, lista_test.copy()))
    print(f"  Merge Sort: {sum(tiempos_merge) / NUM_PRUEBAS:.6f} segundos")

print("Análisis Completado")