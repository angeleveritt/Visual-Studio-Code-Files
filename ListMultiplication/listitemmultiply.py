# List Items for Multiplication - Angelique Everitt
print()
print("List Items for Multiplication Assignment")
print()


def main() :
    ls = [12, 70, -4, 16, 22]                                          
    result = 1
    print("result is : ", result)
    n = len(ls)
    print("The length of the list is " , n)            
    for num in ls:                                             
        result *= num
    print("result from inside the function : ", result)
    return(result)                                                            
    

main()

print
print("fin")
print()

