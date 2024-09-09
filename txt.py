def insertion_sort(arr):
    count_swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            count_swaps += 1
            j -= 1
        arr[j + 1] = key
    return count_swaps

def selection_sort(arr):
    count_swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            count_swaps += 1
    return count_swaps

def bubble_sort(arr):
    count_swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count_swaps += 1
                swapped = True
        if not swapped:
            break
    return count_swaps

vetor_ordenado_crescente = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor_ordenado_decrescente = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
vetor_nao_ordenado = [3, 8, 5, 2, 9, 1, 7, 4, 6, 10]

def ordenar_insertion(arr1, arr2, arr3):
    # Vetores no Insertion Sort
    vetor_ordenado_crescente_insertion = insertion_sort(arr1.copy())
    vetor_ordenado_decrescente_insertion = insertion_sort(arr2.copy())
    vetor_nao_ordenado_insertion = insertion_sort(arr3.copy())

    print(vetor_ordenado_crescente_insertion)
    print(vetor_ordenado_decrescente_insertion)
    print(vetor_nao_ordenado_insertion)

def ordenar_selection(arr1, arr2, arr3):
    # Vetores no Selection Sort
    vetor_ordenado_crescente_selection = selection_sort(arr1.copy())
    vetor_ordenado_decrescente_selection = selection_sort(arr2.copy())
    vetor_nao_ordenado_selection = selection_sort(arr3.copy())

    print(vetor_ordenado_crescente_selection)
    print(vetor_ordenado_decrescente_selection)
    print(vetor_nao_ordenado_selection)

def ordenar_bubble(arr1, arr2, arr3):
    # Vetores no Bubble Sort
    vetor_ordenado_crescente_bubble = bubble_sort(arr1.copy())
    vetor_ordenado_decrescente_bubble = bubble_sort(arr2.copy())
    vetor_nao_ordenado_bubble = bubble_sort(arr3.copy())

    print(vetor_ordenado_crescente_bubble)
    print(vetor_ordenado_decrescente_bubble)
    print(vetor_nao_ordenado_bubble)


ordenar_insertion(vetor_ordenado_crescente, vetor_ordenado_decrescente, vetor_nao_ordenado)
ordenar_selection(vetor_ordenado_crescente, vetor_ordenado_decrescente, vetor_nao_ordenado)
ordenar_bubble(vetor_ordenado_crescente, vetor_ordenado_decrescente, vetor_nao_ordenado)