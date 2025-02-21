# ae playing w Lists
print()
print("Playing w Lists")
print()
list1 = [1, 2.5, "hello", True]
list2 = [2, 1, 9, 5]

ls1 = [5, "RoboGarden", 20.2, 66, False]
print("ls1 = ", ls1) # entire list
print("ls1[0] = ", ls1[0]) # initial position is 0
print("ls1[-2]=", ls1[-2]) # 2nd from the end
print("ls1[1:3] = ", ls1[1:3]) # positions 1, 2 but not 3
ls1[1] = "Hello" # position 1 value is changed to "Hello"
ls1[2:4] = [4, 20] # positions 2, 3 (not 4) are changed to 4 and 20
print("ls1 after change = ", ls1) # entire list after changes
    

# now two ways of removing elements in a list remove() or del    
print()

del ls1[1] # this will delete "Hello"
print(ls1)

ls1.remove(False) # this will remove the first element that matches what is inside the parentheses
print(ls1)




print("fin")

