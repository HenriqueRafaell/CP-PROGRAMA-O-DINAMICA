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
