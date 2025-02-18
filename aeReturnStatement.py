# aeReturnStatement
def main():
    a=3
    a=(a+4)
    print("a is now ", a)

    b=2
    print("b is ", b)
    
    c = a ^ b
    print(a, " XOR ", b, " = ", c)
    print("c is ", c)
    
    print("a is still ", a)
    return a


main()
