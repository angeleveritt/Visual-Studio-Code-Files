# Insertion Sort Assignment - Angelique Everitt
print()
print("Insertion Sort Assignment")
print()

def insertionsort(arr):
    n = len(arr)
    
    if n<= 1 :
        return # already sorted
    
    for i in range(1, n) :             # iterate from second element
        key = arr[i]                   # store curren element as key to be inserted
        j = i-1
        while j>= 0 and key < arr[j] : # move element
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [20, 100, 2, 40, 76]
print("unsorted list", arr)
insertionsort(arr)
print()
print("sorted list", arr)

print()
print("fin")
print()
