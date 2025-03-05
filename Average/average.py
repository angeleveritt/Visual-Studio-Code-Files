# Assignment - Calculate the Average - Angelique
print()
print("Assignment - Calculate the Average")
print()

def total() :
    for i in range(len(ls1)-1) :
        print(ls1[i])
        interim = interim + ls1[i]
        print("The interim total is now : ", interim)
    return interim
    
ls1 = [5, 5, 10, 20, 60]
length = len(ls1)
print("The list length is : ", length)                              # this is working
total(ls1)
print("The sum of all list elements is : ", interim)
      
      
average = interim / length
print("The average is : ", average)


print()
print("fin")
print()




    