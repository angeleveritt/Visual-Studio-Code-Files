# assignment - personal diary - Angelique
print()
print("Assignment - Personal Diary")
print()
diary = {}

# there is a date type but bc I want the date to be the key of the dictionary, keep it string

print("Welcome to your diary")
print()
#dictionaries scale well up to very large

diary_file = r"C:\Users\angel\OneDrive - ABEveritt Inc\8 ABE Training & Courses\00 2025 02 - UWO Python Programming\Visual Studio Code Files\Diary\diary.txt"

with open(diary_file, 'r') as f:        #no errors but I don't think we are ever opening the file, nothing prints from in here
    content = f.read()
    print(content)
    print("printing inside with open block", f)
    print()
    #for line in f:
    #    (key, value) = line.split()
    #    d[key] = value
    #print(f)

date = input("Date : ")
entry = input("How was your day? ") #working
newdata[date] = entry
d.update(newdata)
print("printing the dictionary in the entry portion", d)              #working

for key, value in d.items():
    print("printing in the for key area")
    print(f"{key} : {value}")

print()

#temp = currententry.split(':')
#print(currententry)
#for key, value in diary.items():
#print('Date: {}, Entry: {}'. format(key, value))




#exceptions

# print entire diary

