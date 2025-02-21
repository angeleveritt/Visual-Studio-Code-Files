# playing w List Operators
print()
print("Playing with List Operators")
print()

ls1 = [2,7,8]
ls2 = ["hi", "hello", "welcome"]

print("ls1+ls2: ", ls1+ls2) #working
print()
print("ls1*3: ", ls1*3) #working
print()
print("7 in ls1: ", 7 in ls1) # checks to see if 7 is a member of ls1 and returns True / working
print()
print('hi not in ls2: ', "hi" not in ls2) # checks to see if "hi" is not a member of ls2 and returns False (bc it is there) / working
print()

print("len(list) : ", len(ls1)) # prints the number of elements in the list / working
print()
print("max(list) :", max(ls1)) # prints the last element in the list / working
print()

print("list.count(item) : ", ls1.count(2)) # gives the number of times the item in parentheses occurs in the list / working
print()

print("list.extend(seq): ", ls1.extend([25, 26])) # not working and need to research more 
print(ls1)
print()

print("list.index(0): ", ls1.index(7)) # gives the index number for the value in parentheses / working
print()

print("list.insert(idx, itm) : ", ls1.insert(2, 15)) # at a specific spot in the index, insert this value / working
print(ls1)
print()

print("list.sort(key=func], reverse = True/False) : ", ) # not sure about how to write this.  needs research
print("NOT WORKING")




