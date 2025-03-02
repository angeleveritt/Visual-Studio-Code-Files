# BubbleSort Assignment - Angelique Everitt
print()
print("BubbleSort Assignment")
print()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    numbers = [60, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)

    sorted_list = bubble_sort(numbers)
    print("Sorted list:", sorted_list)
    numbers2 = [5, 1, 4, 2, 8]
    print("\nOriginal list:", numbers2)

    sorted_list2 = bubble_sort(numbers2)
    print("Sorted list:", sorted_list2)
print()
print("fin")
print()