# Algoritmos de busqueda

def busqueda_lineal (lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria (lista_ordenada, elemento_objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista_ordenada[medio] == elemento_objetivo:
            return medio
        elif lista_ordenada[medio] < elemento_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def busqueda_interpolacion (lista_ordenada, elemento_objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha and lista_ordenada[izquierda] <= elemento_objetivo <= lista_ordenada[derecha]:
        if izquierda == derecha:
            if lista_ordenada[izquierda] == elemento_objetivo:
                return izquierda
            return -1
        
        denominador = lista_ordenada[derecha] - lista_ordenada[izquierda] 
        if denominador == 0:
            if lista_ordenada[izquierda] == elemento_objetivo:
                return izquierda
            else:
                return -1
            
        pos = izquierda + ((elemento_objetivo - lista_ordenada[izquierda]) * \
                           (derecha - izquierda) // denominador)
        
        if lista_ordenada[pos] == elemento_objetivo:
            return pos
        elif lista_ordenada[pos] < elemento_objetivo:
            izquierda = pos + 1
        else:
            derecha = pos - 1
    return -1

# Algoritmos de ordenamiento

def bubble_sort(lista): 
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista): 
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n): 
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mid = len(lista) // 2

    left_half = lista[:mid]
    right_half = lista[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return _merge(left_sorted, right_sorted)

def _merge(left, right):
    merged = []

    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged