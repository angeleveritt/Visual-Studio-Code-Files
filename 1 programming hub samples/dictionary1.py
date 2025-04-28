# from the Programming Hub app - Dictionary program
# access dictionary elements

print()
myDict = {"hello": 13, "world": 31, "!": 71, "zzz": "zzz"}
print("Contents of dictionary: ", myDict)
length = len(myDict)                                          
print("Dictionary's number of items: ", length)
print()

# Angel's attempt to just print the key and value without the labels on separate lines
print("Angel's additional for loop")
print("Angel's attempt to print only key and value")
for key, value in myDict.items():
    print(key, value)                                                           # this is working
print("end extra loop")
print()
print("NB:  had trouble getting a while loop to work")
print()

#iterate over key-value pairs
print("1st loop")
for key, value in myDict.items():
    print("key=%s, value=%s" % (key, value))
print("end 1st loop")
print()

print("2nd loop")
#iterate over keys
for key in myDict:
    print("key = %s" % key)
print("end 2nd loop")
print()

# is a shortcut for              # produces same output as 2nd loop
print("3rd loop")
for key in myDict.keys():        # shorter and easier to type
    print("key = %s" % key)
    
print("end 3rd loop")
print()

# iterate over values
print("4th loop")
for value in myDict.values():
    print("value = %s" % value)
   
print("end 4th loop")

print()
print("fin")
print()        