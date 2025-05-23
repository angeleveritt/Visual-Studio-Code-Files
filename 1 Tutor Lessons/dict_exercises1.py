# dictionary exercises
#1 Exercise 1: merge 2 dictionaries where dict_b values overwrite dict_a values

import pprint
import json

print()                                                 # working
print("Exercise 1 - merge 2 dictionaries")
print()
dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"b": 4, "d": 5, "e": 6}
print("dict_a", dict_a)
print("dict_b", dict_b)
print()

dict_a.update(dict_b)                             
print("The merged results: ", dict_a)             

print()
print("end of 1")
print()
#########################################
print()
print("Exercise 1a - merge 2 dictionaries - includes adding 2 values together when the key repeats")
print()                                          # not yet attempted
dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"b": 4, "d": 5, "e": 6}
print("dict_a", dict_a)
print("dict_b", dict_b)
print()

dict_a.update(dict_b)                             # a different exercise might ask us to add the results a value + b value (6)
print("The merged results: ", dict_a)             # homework:  do this exercise for next week - for every key in dict_a, look for the same key in dict_b.  If doesn't exist, simply add the new key to the combined dictionary.  If does exist, add the values together for the value in the combined dictionary.

print()
print("end of 1a")
print()


# Exercise 2 - write a function called word_frequency that takes a string as an input
# returns a dictionary where the keys are the words in the string and the values are the number of times each word appears
print()
print("Exercise 2 - frequency counter")
print()
string = input("Please input the string to analyze: ")  # when entering, need a comma or it won't work
print("The string to be analyzed is:")
print(string)

print()
list_of_words = string.split(",")           # probably a better idea to have " " a space be the delimiter // silly me
print(list_of_words)                            


print()
print("2a - The frequency of the words in the string.")  # last wk I didn't get to the frequency portion bc I hadn't understood that the commas were to be incl in the input.


                                                    # haven't started writing this code yet





#####################################################################################
# copied from Digital Ocean examples            # is this not the same thing?
# Using split()
"""string = "apple,banana,cherry"
list_of_fruits = string.split(",")
print(list_of_fruits)  # Output: ['apple', 'banana', 'cherry']

# Using list()
string = "hello"
list_of_chars = list(string)
print(list_of_chars)  # Output: ['h', 'e', 'l', 'l', 'o']"""
#######################################################################################

print()
print("end of 2, 2a")
print()
###########################################################
print()
print("Exercise 3 - Dictionary Transformation")
print()

mydict = {"name": "Angel", "year_registered": "2025", "status": "active"}
print()
print("original mydict contains: ", mydict)
print()
def invert_dict(mydict):
    inverted_dict = {}
    for key, value in mydict.items():         # In this case he would use key, value.  But in other cases, he would change name of key to something that is very informative.  Same for value.
        inverted_dict[value] = key
    print (inverted_dict)
    return inverted_dict

invert_dict(mydict)

print()
print("end of 3")
print()

#tuple unpacking key, value
#print(mydict.items())   this creates a list items.  the items are tuples.  tuples contain key, value pairs
# print(f"{key=}")  This gives you both the variable name and the value.
# print(f"{value=}")   This gives you both the variable name and the value.

##############################################################

print()
print("Exercise 4 - Nested Dictionary")
print()

data = { 'user': { 'profile': { 'name': 'John', 'age': 30 }, 'settings': { 'theme': 'dark' } } }
print("data is: ", data)
print()
def get_nested_value(nested_dict, keys, default=None):
    current = data
    for key in keys:                                    # use of key in keys here is ok 
        try:                                            # try/except very useful and helps w robust code
            current = current[key]                      # this sample is kind of oldfashioned Python code // try/except being used for keys that don't exist is oldfashioned
        except (KeyError, IndexError, TypeError):       # modern python one line of code can replace 89 to 92 // this is homework to track down
            return default                              # you will still need try/except for other things - just not for finding missing keys
    return current
    
print("Looking for name: ")
print(get_nested_value(data, ['user', 'profile', 'name'])) #should return 'John'
print()
print("Looking for email: ")
print(get_nested_value(data, ['user', 'profile', 'email'], 'Not found')) #should return 'Not found'  // no email key and I changed None to "Not found".  I think.
print()
print("end of 4")
print()
####################################################
print()
print("Exercise 4a - Nested Dictionary - using the single line instead of try/except")
print()

data = { 'user': { 'profile': { 'name': 'John', 'age': 30 }, 'settings': { 'theme': 'dark' } } }
print("data is: ", data)
print()
def get_nested_value(nested_dict, keys, default=None):
    current = data
    for key in keys:                                    # use of key in keys here is ok 
        try:                                            # try/except very useful and helps w robust code
            current = current[key]                      # this sample is kind of oldfashioned Python code // try/except being used for keys that don't exist is oldfashioned
        except (KeyError, IndexError, TypeError):       # modern python one line of code can replace 89 to 92 // this is homework to track down
            return default                              # you will still need try/except for other things - just not for finding missing keys
    return current
print("Looking for name: ")
print(get_nested_value(data, ['user', 'profile', 'name'])) #should return 'John'
print()
print("Looking for email: ")
print(get_nested_value(data, ['user', 'profile', 'email'], 'Not found')) #should return 'Not found'  // no email key and I changed None to "Not found".  I think.
print()
print("end of 4a")
print()