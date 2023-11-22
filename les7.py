def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def selection_sort(array, method):
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i + 1, len(array)):
            if method == 0:
                if array[j] < array[minimum]:
                    minimum = j
            elif method == 1:
                if array[j] > array[minimum]:
                    minimum = j
            elif method == 2:
                if array[j] % 2 == 0:
                    minimum = j
            elif method == 3:
                if array[j] % 2 != 0:
                    minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array


def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)
    return array

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def print_array(array):
    for i in array:
        print(i, end=" ")
    print()

array = [2, 7, 1, 6, 3, 5, 4, 10, 8]
print("масив:")
print_array(array)

print("Сортування бульбашкою:")
array = bubble_sort(array)
print_array(array)

print("Сортування вставкою:")
array = insertion_sort(array)
print_array(array)

print("Сортування вибором:")
array = selection_sort(array, 0)
print_array(array)

print("Швидке сортування:")
array = quick_sort(array, 0, len(array) - 1)
print_array(array)