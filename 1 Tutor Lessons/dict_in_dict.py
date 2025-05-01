# creating dictionaries
# creating dictionaries in dictionaries
# https://pythonguides.com/dictionaries/

print()
print("1111111111111111111111111111111")    # Andy's example
print("create dictionary booking using curly brackets and incl extra attributes --> customer_name: name: Customer name, value: None")
print("nested dictionaires, I believe")
booking = {                                                               # method 1
    "customer_name": {"name": "Customer name", "value": None},
    "weight_kg": {"name": "Weight in kg", "value": None},
    "volume_m3": {"name": "Volume in cubic meters", "value": None},
}
for field_name, value in booking.items():    # how I like to print things
    booking[field_name]["value"] = input(booking[field_name]["name"] + ": ")
print(booking)
print()
for key, value in booking.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)    
print()
print("trying to print specific item")
print (booking["volume_m3"])
print()
# question for Andy:  why use the dict() constructor ever
print()
print("22222222222222222222222222222222222222")
print("this doesn't use curly brackets --> customer = dict([('name', 'John Smith') ...    ])")
print()
my_dict = dict()                                                         # method 2 - no curly brackets but it's still a dictionary?
customer = dict([
    ('name', 'John Smith'),
    ('age', 35),
    ('city', 'New York'),
    ('is_active', True)
])
print("customer: ", customer)
print(customer)
for key, value in customer.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)    
print()
print("accessing a value --> print(customer['name'])")
print(customer['name'])
print()



print("333333333333333333333333333333333333333333")
print()
# ask Andy about this too
print()
print("creating a dictionary using {x:x*x for x in range(1, 6)}")
squares = {x:x*x for x in range(1, 6)}
print(squares)
for key, value in squares.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)    
print()
print("trying to print specific item")
print (squares[3])
print()
print("4444444444444444444444444444444444444")
print("creating a dictionary from lists")
cities = ["New York", "Los Angeles", "Chicago"]
populations = [8804190, 3898747, 2746388]
city_pops = {city: pop for city, pop in zip(cities, populations)}                     # is zip a function?
print(city_pops)
print()
for key, value in city_pops.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)    
print()
print("trying to print specific item")
print (city_pops["Chicago"])
print()
print("55555555555555555555555555")
print()

# what is get() about?
print()
print("get(), etc")
print()
product = {
       "name": "Laptop",
       "price": 999.99,
       "brand": "TechPro",
       "in_stock": True
}

print("get all keys")
print(list(product.keys()))
print()
print("get all values")
print(list(product.values()))
print()
print("get all key-value pairs as tuples")
print(list(product.items()))
print()
print("6666666666666666666666666666666666666666")
# what is setdefault() about
# what is creating a dictionary with conditionals about and does that apply to my air shipping cost part of the packages assignment?
# nested dictionaries
print()
print("nested dictionaries, again?")
print()
employees = {
       'E001':{
              "name":"James Smith",
              "department": "Sales",
              "salary": 65000,
              "contact": {
                     "email": "james@example.com", 
                     "phone": "555-555-1234"

              }
       },
       'E002':{
              "name": "Lisa Johnson",
              "department": "Marketing", 
              "salary": "70000",
              "contact": {
                     "email": "lisa@example.com",
                     "phone": "555-555-6565"
              }
       }
}

print(employees)
print(list(employees.items()))
print()
for key, value in employees.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)    
        
print()
print()


print("777777777777777777777777777777777777777777777777777777777")
print()
a = "2"                                                               # this is working // I don't know what I've done wrong in the other program
b = 4
c = int(a)
print(a, b, c)