# Sequential Search
def sequential_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


# Binary Search
def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Main Program
data1 = [3, 8, 1, 9, 0, 6, 7, 5]
target1 = int(input("Enter number for Sequential Search: "))

result1 = sequential_search(data1, target1)

if result1 != -1:
    print("Found at index:", result1)
else:
    print("Not Found")


print("\nBinary Search")

data2 = [1, 3, 5, 7, 9, 11, 13, 15]

target2 = int(input("Enter number for Binary Search: "))

result2 = binary_search(data2, target2)

if result2 != -1:
    print("Found at index:", result2)
else:
    print("Not Found")
