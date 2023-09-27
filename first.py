# Первый вариант решения на python

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)

    for i in range(n1):
        left[i] = A[p + i]
    for j in range(n2):
        right[j] = A[q + j + 1]

    left[n1] = float('inf')  # Бесконечность как маркер окончания
    right[n2] = float('inf')

    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


# Пример массива
A = [5, 2, 4, 6, 1, 3, 2, 6]
n = len(A)
merge_sort(A, 0, n - 1)
print(A)

