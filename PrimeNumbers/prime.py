# Prime Numbers mini project by Angelique Everitt
# prime numbers are those with no positive divisors other than 1 and itself
print()
print("Prime Numbers Mini Project")
print()
lower = int()
lower = 2
upper = int(input("The range of numbers begins at 2.  Please enter the last number of the range: "))
num = int()
primes = [2]

#for i in range(5, 15):   ### this is a little iteration that works.  Now figure out what's wrong with yours that doesn't work.
#    print(i)


def is_prime(num): # this function checks to see if a number is a prime number.  It is called from within find_primaries.  
    #print("MARKER 1 - made it to is_prime function:  ", num)
    if num <= 1 :
        print("False is returned for: ", num)
        return False
    else :
        for i in range(lower, upper) :
            if (num % i) == 0 :
                return False
            return True

def find_primaries(lower, upper) :  # this function runs through the range of numbers, calls is_prime(), and appends to primes[].  
    for num in range(lower, upper) :
        #print("MARKER 2 - made it inside find_primaries function: ", num)
        if is_prime(num):
            primes.append(num)
    return primes

find_primaries(lower, upper)


print()
#print(primes) 
print(f"Prime numbers between {lower} and {upper} : {primes} ")
print("BUT THIS LIST ALSO CONTAINS SOME NON_PRIME NUMBERS.")
print("I wish I cared more about prime numbers but I do not.")
print("This has already taken too much time and I have other exercises to get to.")

print()
print("fin")
print()




                