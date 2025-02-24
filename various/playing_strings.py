#playing w strings
print()
print("Playing with Strings")
print()
st1 = "hello, everyone"
st2 = "RoboGarden"
st3 = "hi"

print("st1 : ", st1, "\nst2 : ", st2, "\nst3 : ", st3) #\n inside the string to cause new line
print()

print("changing st3 by coding st3 = st2")
st3 = st2 # changes "hi" to "RoboGarden"
print()
print("st1 : ", st1, "\nst2 : ", st2, "\nst3 : ", st3) #after change
print()

print("new exercise")
print("The value of st1 is: ", st1)
print("now altering st1 by coding st1 = st1[0:3] + ' Python'") 
st1 = st1[0:3] + "Python"
print("st1 is now: ", st1)
print()

print("now playing w string operators")
st = "hello"
print("st : ", st)
st = st+ " everyone" #concatenation
print(st)

print()
st = st*3 # repetition operator
print("st after repetition operator: ", st)
print()
print("playing with slice operator")
print("st[1] = ", st[1])
print("st2[0:4] = ", st2[0:4])
print()

print("membership exercise")
print("st2 is: ", st2)
if "eve" in st2: 
    print("'eve' exists in st2")
else:
    print("eve is not in st2")
if "Gard" in st2: 
    print("'Gard' exists in st2")
else:
    print("Gard is not in st2")
print()

print()
print("new exercise - escape characters")
print("hello \nworld \nnew line")
print()
print("hello\tworld\ntab")
print()
print("hello!!\rworld\ncarriage return") #I don't understand what happens here.  world replaces hello
print("12345678\rabcd\ndifferent lengths") #replaces the initial characters with the new string.  why is it called carriage return?  
#not sure when this would be useful
print()

print("new exercise - formatting operator")
name = "Robo"
age = 10
marks = 30.8
degree = -10
string1 = "Hi, %s" % (name) 
print(string1)
# % can be used to define the structure of a string.  allows for different variable types within a string. 
string2 = "Hey, %s, my age is %u" % (name, age) #name early, age at the end     
print(string2)
string3 = "Hey %s, my subject mark is %f" % (name, marks) #name early, age at the end
print(string3)
string4 = "Hey, %s, the weather is %d" % (name, degree) # name early, age at the end
print(string4)

print()
print("fin")
print()


