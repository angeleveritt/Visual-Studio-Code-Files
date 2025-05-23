#  counting frequency of words using dictionary instead
import pprint
sentence = "this is a sentence and another sentence that goes on forever and forever"
words = sentence.split(" ")      # if you put nothing in the parentheses, it assumes space but he prefers being explicit

counts = {}
for word in words: 
    counts[word] = counts.get(word, 0) + 1                        # go to the counts dictionary and use word as the key // to avoid keyerror, we have to do the get thing
pprint.pprint(counts)

for key, value in counts.items():
    print(key, value)

for key, value in counts.items():
    print(f"{key} : {value}") 

# figure out how to print in columns so the results are lined up      //  look up formatting in f strings.  it will be strange

for key, value in counts.items():
    print(f"{key=} : {value=}")

age = 42
print(f"{age=}")                     # the symbols are overloaded meaning tha they serve multiple purposes

print()