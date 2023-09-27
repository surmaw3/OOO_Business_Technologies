def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2  # Находим середину массива
        merge_sort(arr, left, mid)  # Сортируем левую половину
        merge_sort(arr, mid + 1, right)  # Сортируем правую половину
        merge(arr, left, mid, right)  # Сливаем отсортированные половины

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    # Создаем временные массивы для левой и правой половин
    left_half = [0] * (n1)
    right_half = [0] * (n2)
    
    # Копируем данные во временные массивы left_half и right_half
    for i in range(n1):
        left_half[i] = arr[left + i]
    for j in range(n2):
        right_half[j] = arr[mid + 1 + j]
    
    # Сливаем временные массивы обратно в основной массив arr
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    # Дополняем оставшиеся элементы, если такие есть
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

# Пример выполнения функции
my_array = [5, 2, 4, 6, 1, 3, 2, 6]
n = len(my_array)
merge_sort(my_array, 0, n - 1)
print(my_array)
