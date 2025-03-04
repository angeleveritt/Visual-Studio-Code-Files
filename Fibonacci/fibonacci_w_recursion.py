# assignment - Python fibonacci w recursion - Angelique
print()
print("Assignment - Python Fibonacci Function w Recursion")
print()

def fibonacci(n) :
    if n <= 0 :
        return "Input should be a positive integer."
    elif n == 1 :
        return 0
    elif n == 2 :
        return 1
    else :
        #print(fibonacci(n-1) + fibonacci(n-2))                     # this is a very long list of numbers
        return (fibonacci(n-1) + fibonacci(n-2))
    
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
      

print()
print("fin")
print()






