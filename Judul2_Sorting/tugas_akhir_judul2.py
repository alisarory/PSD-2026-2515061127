
def selection_sort(data):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(data):
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Data awal
data = [64, 34, 25, 12, 22, 11, 90]

print("================================")
print(" PROGRAM SORTING PYTHON")
print("================================")
print("Data awal:", data)
print("--------------------------------")
print("Hasil Bubble Sort   :", bubble_sort(data))
print("Hasil Selection Sort:", selection_sort(data))
print("Hasil Insertion Sort:", insertion_sort(data))
print("================================")
