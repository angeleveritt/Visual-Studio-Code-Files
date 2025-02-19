#Factorial Mini Project by Angelique Everitt
print()
print("Factorial Mini Project")
print()
x = int() #initializes as an integer without specifying value
print("x is initially set to: ", x)
factorial = 1
print("factorial is initiall set to: ", factorial)
print()


x = int(input("Please enter an positive integer number to be used in the factorial calculation:  "))
print()       


if x < 0 :
    print("Sorry, factorials do not work for negative numbers.")
elif x == 0 :
    print("The factorial of 0 is 1.")
else :
    for i in range(1, x + 1) :
        factorial *= i  
    print("The factorial of", x, "is", factorial)
    print()
    print("fin")
    print()

