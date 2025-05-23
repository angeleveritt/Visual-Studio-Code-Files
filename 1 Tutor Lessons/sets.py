# sets
#  an unordered list of unique items
# uses same delimiter as dictionary but no colons so it knows it's a set

codes = {23, 1, 45}     # no particular sequence    AND no pairs    AND all items are unique
print(codes)
# rarely use sets in python

numbers = [1, 2, 3, 2, 3, 1, 4, 6, 9, 0]
#to remove all the duplicate entries, we use sets
numbers = set(numbers)    # if I had wanted to keep the list format:     numbers = list(set(numbers))
print(numbers)
print()                     # working
# if you wanted to keep the list


