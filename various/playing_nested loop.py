#playing w nested loop
print()
print("playing w nested loop")
print()
tp = ("hello", "hi", "Robo")

for i in range(len(tp)):
    print("tuple index:", i, "tuple item:", tp[i])
    for letter in tp[i]:
        print("letter:", letter)

print()
print("fin")
print()

