# List Items for Multiplication - Angelique Everitt
print()
print("List Items for Multiplication Assignment")
print()


def main(ls) :
    print("The list inside the main function is : ", ls)
    result = 1
    print("result is : ", result)
    n = len(ls)
    print("The length of the list is " , n)             # getting this far
    for i in ls :
        print(ls[i])
        if ls[i] <= (ls[-1]) :
            result = result * ls[i]
            return result
            print("inside the if loop, this is result : ", result)
        else :
            return result
    print("result inside the function : ", result)
    return mul_out

ls = [12, 70, -4, 16, 22]
main(ls)

print
print("fin")
print()

