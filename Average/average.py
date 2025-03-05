# Assignment - Calculate the Average - Angelique
print()
print("Assignment - Calculate the Average")
print()

import math

def calculate_average(ls1):
    if len(ls1) < 1:
        return 0
    return sum(ls1) / len(ls1)

ls1 = [5, 5, 10, 20, 60]                    
print(ls1)

average = calculate_average(ls1)
print("The average of the list is : ", average)

print()
print("fin")
print()




    