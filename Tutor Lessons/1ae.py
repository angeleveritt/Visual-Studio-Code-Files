#lesson 1ae.py
# nested loops / function

def addup(number1, number2):  # this is the way to do it.  This is a pure function.  Everything passed to it as parameters and everything passed out of it in a Return.  This is good.
    return number1+number2

result = addup(5, 10)
print(result)


def addup_2():      # this is not the way to do it.  not as modular
    number1 = 10
    number2 = 20
    return number1+number2
result = addup_2()


number1 = 10            #if they were constants by convention, they would need to be in uppercase like NUMBER1
number2 = 20            #NUMBER2 and NUMBER1 are not really "constants".  They are Module Level Variables.
                        # importing loses the module level variables
def addup_3():
    return number1+number2
result = addup_3()


def get_tax(type):          # this is the way to handle "constants" that are not constants
        if type = "food":
            return 0.03
        else:
            return 0.07
        
def calculate_price(value, type):  # he didn't include the type addition in here
     return value + (value * get_tax(type))     # this is inelegant but good for where I am now

# the message to remember is to keep functions pure
# be very careful w Module Level Globals --> put them in functions instead

# lesson 1 b
# nested for loop

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]         # if using range, first number included but last number has to be higher bc last number not inclusive
# could say numbers = range(10) which would be 0,1,2,...9

for letter in letters:          # you don't have to use i and j
    for number in numbers:
         print(f"{letter}{number}")
    # this is not a function so no need for Return here because it's just doing it's thing
    




     

