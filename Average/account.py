# playing w classes
print()

class Account():
    def __init__(self, balance):
        self.balance = balance              # when you create a new instance of Account, you need to include balance // the Class has the functions, the instance has the data // self means I belong to the instance not the class

    def show_balance(self):                 # method show_balance belongs to the class Account // # every function inside a Class must have the Self parameter
        print("Balance is : " self.balance")            


andy = Account(2000)
andy.show_balance()
print(andy.balance)

fred = Account(5000)
fred.show_balance()
print(fred.balance)                         # on the whole Classes should never have more than 5 to 10 functions and 5 to 10 data items // the bigger the class gets, the harder to understand and harder to re-use it
                                            # a Class is a way to deal w complexity by grouping things together



                                            # you can only call a function that's inside a Class by referring to an instance of that Class first

                                            # all class definitions first // all function definitions first // module-level global variables up near the top too  - these are usu uppercase// then executable code including those instances

print()
#print(type(andy))             # the type of the andy variable is Account // andy's type is Account // it's like we've added a new type to the Python Type System


