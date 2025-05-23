# lists

names = ["Andy", "Angel", "Steven"]
more_names = names

more_names.append("bob")
print (names)

# lists can get enormous in size so python helps out by giving names two labels name and more_names
# so when we print names, it is actually printing the more_names which includes the appended "bob"

# if I want more_names to be a freestanding copy of names, more_names = names.copy()

more_names2 = names.copy()             # freestanding copy
more_names2.append("fanny")
print (names)
print (more_names2)

print()

