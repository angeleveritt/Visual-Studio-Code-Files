# training on dictionaries

person = {}

person["name"] = "Joseph"
print(person)

person["name"] = "Andy"
print(person)
print()
print(person["name"])
#print(person["age"])           # this throws a key errorm 
# or do it this way
print(person.get("age", 0))     # age doesn't exist as a key but this, it will print 0 bc 0 is the default if age doesn't exist




print()