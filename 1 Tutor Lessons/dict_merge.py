# dictionary exercises
#1 Exercise 1: merge 2 dictionaries where dict_b values overwrite dict_a values

import pprint
import json

print()
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
# Exercise 2 - write a function called word_frequency that takes a string as an input
# returns a dictionary where the keys are the words in the string and the values are the number of times each word appears
print()
print("Exercise 2 - frequency counter")
print()
string = input("Please input the string to analyze: ")
print("The string to be analyzed is:")
print(string)

print()
list_of_words = string.split(",")
print(list_of_words)                            # not working.  I did import json.  not sure if that's wrong
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
print("end of 2")
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
    for key, value in mydict.items():
        inverted_dict[value] = key
    print (inverted_dict)
    return inverted_dict

invert_dict(mydict)

print()
print("end of 3")
print()

##############################################################

print()
print("Exercise 4 - Nested Dictionary")
print()

data = { 'user': { 'profile': { 'name': 'John', 'age': 30 }, 'settings': { 'theme': 'dark' } } }
print("data is: ", data)
print()
def get_nested_value(nested_dict, keys, default=None):
    current = data
    for key in keys:
        try:                                            # lets go through this
            current = current[key]
        except (KeyError, IndexError, TypeError):
            return default
    return current
    
print("Looking for name: ")
print(get_nested_value(data, ['user', 'profile', 'name'])) #should return 'John'
print()
print("Looking for email: ")
print(get_nested_value(data, ['user', 'profile', 'email'], 'Not found')) #should return 'Not found'  // no email key and I changed None to "Not found".  I think.
print()
print("end of 4")
print()


