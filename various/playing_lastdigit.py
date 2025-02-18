# playing w last digit divisible by 3 - Angelique Everitt
print()
print("Decision-Making on a Last Digit")
print()

num = 27
print("The number is", num)

lastdigit = (27 % 10)
print("The last digit is", lastdigit)

if (lastdigit / 3) > 0:
    remainder = False
    print("The last digit is not divisible by 3")

else:
    remainder = True
    print("The last digit is divisible by 3")

print()
print("fin")
print()


