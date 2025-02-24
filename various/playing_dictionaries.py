# playing w dictionaries // key then value
print("playing w dictionaries")
print()
dict1 = {"h": "hello", "w": "welcome"} # h and hello are together, w and welcome are together
print("dict1 looks like this : ", dict1)
print("now we use the keys")
print("h will return : ", dict1['h'])
#print("k is not defined so it returns KeyError: 'k' : ", dict1["k"])

print()
print("new exercise")
dict2 = {"h": "hello", "w": "welcome", "r": "RoboGarden"}
print("This is dict2 :", dict2)
dict2["j"] = "John"
dict2["h"] = "hi"
print("This is dict2 now : ", dict2)
del dict2['w']
print("This is dict2 now : ", dict2)
dict2.clear()
print("This is dict2 after clearing : ", dict2)
del dict2 #deletes dict2
#print("Printing dict2 should throw an error : ", dict2) # it did


dict3 = {1: "Hi", 2: "welcome", 3: "RoboGarden"}
dict4 = dict3
dict5 = dict3.copy()
print("This is dict3 : ", dict3)
print("This is dict4 : ", dict4)
print("This is dict5 : ", dict5)
dict6 = {8: "yes", 9: "No"}
      
dict3.update(dict6)
print("This is dict3 : ", dict3)






print()
print("fin")
print()
