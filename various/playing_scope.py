# playing w scope
print()
print("Playing w Scope")
print()

#x = 1                                           #this throws an error.  Python notices that a change to x happens inside the function AFTER the print statement and it assumes we screwed up.
#def func():
#    print("inside function :", x)
#    x = 2
#func()
#print("x is : ", x)

print("foo() - x is global scope, y is inside function only")
x=1                                             # any variable called must exist before it is called.  if this were declared after foo() is called, it wouldn't work.
def foo():                                      # the function can see x and y
    y = 12                                          
    print(f'foo can see global x and it is {x}')
    print(f'foo can see the y defined inside foo and it is {y}')
foo()
print("global x outside of foo() remains : ", x)
print()


print("foo2() x is changed temporarily inside the function, not at the global scope")
x = 1
def foo2():
    x = 11                                      # this resets x to 11 just inside the function
    y = 12                                      # if I wanted to adjust the global x value from inside the function, I would write a line global x before this.  then global x is modified.
    print(f'foo2 can see x that has been defined inside foo2() and it is {x}')
    print(f'foo2 can see the y defined inside foo2 and it is {y}')
foo2()
print("global x outside foo2() remains : ", x)
print()

print()
print("foo3() global x is changed from inside the function")
x = 1
def foo3():
    global x
    x = 11
    y = 12
    print(f'foo3 can see global x, and prints the change to it that happened inside foo3() - the updated global x is {x}')
    print(f'foo2 can see the y defined inside foo3 and it is {y}')
foo3()
print("global x was changed from inside foo3() and it is now : ", x)
print()


print("nested functions showing when things will print")
a = 1
def outer() :
    a = 2
    def inner():
        a = 3
        print(a, f'inner() sees a defined in inner and it is : ', a)
        return
    inner()
    print(a, f'outer sees a defined in outer() and it is : ', a)
    return
outer()
print(a, f'global a is seen from the top level and it is : ', a)
print()



print()
print('fin')
print()