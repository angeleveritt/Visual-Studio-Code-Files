#  counting frequency of words using dictionary instead
import pprint
sentence = "this is a sentence and another sentence that goes on forever and forever"
print("This is the sentence whose words we are counting: ", sentence)

print()
print("spliting the sentence up into separate list items using split")
words = sentence.split(" ")      # if you put nothing in the parentheses, it assumes space but he prefers being explicit
print(words)
print("##############################")

print()
print("just a simple pprint.pprint of counts")
print()
counts = {}
for word in words: 
    counts[word] = counts.get(word, 0) + 1                        # go to the counts dictionary and use word as the key // to avoid keyerror, we have to do the get thing
pprint.pprint(counts)
print()
print("########################")
    
print()
print("printing for key, value in counts.items")

for key, value in counts.items():
    print(key, value)
print()
print("##########################")

print()
print("for key, value in counts.items then print f {key} : {value}")
for key, value in counts.items():
    print(f"{key} : {value}") 
print()
print("#############################")
print()
# figure out how to print in columns so the results are lined up      //  look up formatting in f strings.  it will be strange

print()
print("printing the word key and value in front of the actual key and value")

for key, value in counts.items():
    print(f"{key=} : {value=}")

age = 42
print(f"{age=}")                     # the symbols are overloaded meaning that they serve multiple purposes

print()
print("########################")

# trying to print in columns
print()
print("trying to print in columns using f{key:<10} etc")
print()

for key, value in counts.items():
    print(f"{key:<10} {value: <5}")                               # left aligns key and makes sure it takes up at least 10 characters
    print()                                                         # then left aligns value and reserves 5 characters

print()
print("###################")
