number = input("Enter a number: ")
try:
    number = int(number)
except ValueError:
    print("Invalid number")
except TypeError:
    print("Invalid number")
else:
    print(number + 1)
finally:
    print("This is always printed")
