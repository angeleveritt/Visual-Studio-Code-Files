# Calculate Factorial Using Recursion - Assignment - Angelique
print()
print("Assignment - Calculate Factorial Using Recursion")
print()


def factorial(n) :
    if n == 0 or n == 1 :
        return 1
    else :
        result = (n * factorial(n-1))
        return result
    

num = 5
print("number : ", num)
print("Factorial : ", factorial(num))

print()
print("fin")
print()
