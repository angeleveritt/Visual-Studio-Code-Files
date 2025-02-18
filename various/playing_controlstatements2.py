# playing w control statements
print()
print("playing w control statements")
print()

st = "Robogarden"
for ind in range(len(st)):  #break example
    letter = st[ind]
    if "g" == letter: break
    print("current letter is:", letter)
print()
print("The letter 'g' was found in the string at the index = ", ind)
print()
x = 0
print("x is", x)
print("start while loop")
while x < 6:  #continue example
    x += 1
    if x == 3:
        continue
    print("Current x value is:", x)
print("end while loop") 
print()
ls = [10, 2.6, "hello", 8, 9.1]
for item in ls:  #pass example
    if item==8:
        pass
        print("line after pass statement")

    print("item is:", item)

print()
print("Bye bye")
print()
