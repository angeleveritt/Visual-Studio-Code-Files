# assignment Bubble Sort
print("BubbleSort Assignment - Angelique Everitt")
print()

ls1 = [5, 8, 100, 20, 55, 2]
print("ls1 is : ", ls1)
print()
lowest = min(ls1)
highest = max(ls1)
length = len(ls1)
print("lowest is : ", lowest, "and highest is : ", highest)
print("length is : ", length)

#sorted_list = sorted(ls1)
#print("The sorted list using sorted() is : ", sorted_list)

def bubble_sort(ls1): # this is all not working and I'm giving up until I need it
    for i in range(length - 1) : #do I have to do the len thing in here or is up top good enough?
        swapped = False # to track if any swaps happen
        for j in range(length-1):
            if ls1[j] > ls1[i+1]:
                ls1[j], ls1[j+1] = ls1[j+1], ls1[j] # I had temp variables to swap things around.  Not necessary.  This is simple.
                swapped = True #bc a swap happened
                print("printing list ls1 from inside inner loop : ", ls1)       
        if not swapped: # if no elements swapped during inner loop, then break 
            break
            
    return ls1
    
def bubble_sort(result): #I'm running it through twice in order to complete the sort.
    for i in range(length - 1) : 
        swapped = False # to track if any swaps happen
        for j in range(length-1):
            if result[j] > result[i+1]:
                result[j], result[j+1] = result[j+1], result[j] # I had temp variables to swap things around.  Not necessary.  This is simple.
                swapped = True #bc a swap happened
                print("printing list result from inside inner loop : ", ls1)       
        if not swapped: # if no elements swapped during inner loop, then break 
            break
            
    return result

       

result = bubble_sort(ls1)
print("The list is now : ", result)  # this worked but didn't run enough times to catch all the required changes.  I found sorted(list) and it works

result2 = bubble_sort(result)
print("The list is now : ", result2)

print()
print("fin")
print()


            
              
   
