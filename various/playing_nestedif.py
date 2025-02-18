# playing w nested if

print()
print("playing w nested if statements")
print()

x = 50
print("x =", x)
print()

if x < 60:
    print("x is less than 60")

    if x > 55:
        print("x is greater than 55")

    elif x == 50:
        print("x equals 50")

    elif x > 45:
        print("x is greater than 45")

    else:
        print("x is less than 45")

else:
    print("x is greater than 60")

    print()
print()    
print("Bye bye")

