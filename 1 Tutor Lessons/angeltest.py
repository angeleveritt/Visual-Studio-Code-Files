# trying to create a simple dictionary
#from pprint import pprint  # allows you to just call this pprint rather than repeating pprint.pprint
import pprint

mytest = {"name": "Angel", "course": "Python"}
print(mytest)
for key, value in mytest.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)   
print()
print("1")
print()
states = {
        "California": {
            "capital": "Sacramento",
               "flower": "California Poppy"
        },
        "New York": {
            "capital": "Albany",
            "flower": "Rose"
        }
     
}
print()
print(states)
for state, facts in states.items():
    print(state, facts["flower"])

print(states["New York"]["capital"])

## Real Python - Dictionaries in Python
# Real Python - How to iterate through a dictionary
# Real Python - Sorting a dictionary - values, keys, more

print()
print("2")
print()
person = {
    "first_name": "John", 
    "last_name": "Doe",
    "age": 35, 
    "spouse": "Jane",
    "children": ["Ralph", "Betty", "Bob"],      # I think this is a list
    "pets": {"dog": "Frieda", "cat": "Sox"}, # here is a nested dictionary
}
print()
print(person)
print()
print("PRINTING pets")
print(person["pets"]["dog"])                  # I seem to want to put a dot after the dictionary name all the time
print()
print("PRINTING specific value using get()")
print(person.get("children"))
print()
print("PRINTING values")
print(person.values())                       #just the values except nexted dictionary has its keys
print()
print("PRINTING keys")
print(person.keys())
print()
print("PRINTING items")
print(person.items())
print()
print("NOW updated John to Angel")
print()
person.update({                                     # the way I've done this, I replaced John's info w mine // this is right
 "first_name": "Angel", 
    "last_name": "Everitt",
    "age": 60, 
    "spouse": None,
    "children": ["Ralph", "Betty", "Bob"],      # I think this is a list
    "pets": {"dog": "Fanny", "cat": "Tewkesbury"}
})
print("PRINTING person")
print(person)
print()
print()
print("ANGEL's Nested Dictionary")
big_cats = {
    "Panthera Tigris": {
        "weight_male_kg_avgmax": 260,
        "weight_female_kg_avgmax": 160, 
        "status": "Endangered"
    },
    "Panthero Leo": {   
        "weight_male_kg_avgmax": 190,
        "weight_female_kg_avgmax": 143, 
        "status": "Vulnerable"
    },
    "Lynx Canadensis": {
        "weight_male_kg_avgmax": 17,
        "weight_female_kg_avgmax": 12, 
        "status": "Vulnerable"
    },
    "Lynx Rufus": {
        "weight_male_kg_avgmax": 18,
        "weight_female_kg_avgmax": 15, 
        "status": "CITES Appendix II"  
    },    
    "Puma Concolor": {    
        "weight_male_kg_avgmax": 72,
        "weight_female_kg_avgmax": 48, 
        "status": "Least Concern"  
     
    }
}

print(big_cats)
print()
print("Angel's preferred method of printing dictionaries")
for key, value in big_cats.items():
      print(key, value)
print()
print("PRINTING get(Puma Concolor)")
print(big_cats.get("Puma Concolor"))
print()


pprint.pprint(big_cats)     # this is what you're choosing to learn for now
#print=pprint.pprint   # this would replace your normal print.  won't always work
#print(big_cats)

