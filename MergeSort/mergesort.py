# assignment Merge Sort
print()
print("Merge Sort Assignment - Angelique Everitt")
print()

#set1 = [0:(length/2)]
#set2 = [(length/2 + 1):]
#print("This is set1 : ", set1)
#print("This is set2 : ", set2)

def merge(arr, l, m, r):                        # l and r are Left and Right, m might be middle
    n = len(arr)
    h = n/2                                     # why can't we just use half of the length like this?
    print("length of list is : ", n)
    print("half of the length is : ", h)
    n1 = m - l + 1                              # not sure what these really did
    n2 = r - m                                  # not sure what these really did
    print("n1, n2 : ", n1, n2)                  # these are working out to 1.0
    
    L = [0]*h                                   # temp arrays // L and R are Left and Right // [0] * n creates a list w n elements
    R = [0]*h                                   # [0] * n creates a list w n elements
    print("L, R are : ", L, R)                  # this is working
    print()

    for i in range(0, n1):                      # copying data into temp arrays
        L[i] = arr[l + i]
        print("\nprinting L[i] from inside first for loop : ", L[i])
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        print("\nprinting R[j] from inside second for loop : ", R[j])

    i = 0                                       # initial index of subarrays
    j = 0
    k = l

    while i < n1 and j < n2 :                   #merge the temp arrays back into arr[l...r]
        if L[i] <= R[j] :
            arr[k] = L[i]
            i += 1
        else : 
            arr[k] = R[j]
            j += 1
        k += 1
              
    
    while i < n1 :                              # copying remaining elements of L[] if there are any
        arr[k] = L[i]
        i += 1
        k += 1
        print("arr[k], i, k : ", arr[k], i, k)

    while j < n2 :                              # copying remaining elements of R[] if there are any
        arr[k] = R[j]
        j += 1
        k += 1
        print("arr[k], j, k : ", arr[k], j, k)

def mergeSort(arr, l, r) :                      # I'm thinking (list, initial index, last index)    
    if l < r :
        m = ((l+(r - 1))/2)                     # same as (l+r)/2 but avoids overflow for large l and h // m is middle.  this is working
        print("\nmiddle index is : ", m)        # this is printing but it prints twice
        print()
        mergeSort(arr, l, m)                    # sort L and R halves // (list, initial index, middle index)
        mergeSort(arr, m+1, r)                  #(list, middle index +1, last index )
        merge(arr, l, m, r)                     # merge (list, initial index, middle index, last index)
        print("l, m, r : ", l, m, r)
        print()


arr = [300, 200, 100, 50]                       # driver code to fire defined functions
print("The arr list begins as : ", arr)
n = len(arr)
print("The length of the list is : ", n)
print()
print("Given array is:")                        # this is printing
for i in range(n) :                             # this seems to be working
    print("\n %d" % arr[i], end = " ")             # %d allows us to print numbers within strings or other values ; this seems to be printing
    print()      
mergeSort(arr, 0, n-1)                          # (list, l = index of L, r = index of R)
print("\n\nSorted array is : ")                 # this is not printing
for i in range(n) :
    print("\n %d" % arr[i], end = " ")             # %d allows us to print numbers within strings or other values ; this is not printing




print()
print("fin")
print()