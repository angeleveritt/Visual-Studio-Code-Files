# assignment - personal diary - Angelique
print()
print("Assignment - Personal Diary")
print()
diary = {'DATE' : 'ENTRY', '1964-04-13' : "born", '1965-04-13' : 'first birthday'}
newdata = dict()

print("Welcome to your diary")
print()
date = input("Date : ")
entry = input("How was your day? ")
newdata[date] = entry
print(diary)
print(newdata)
diary.update(newdata)

for key, value in diary.items():
    print(f"{key} : {value}")

print()

#temp = currententry.split(':')
#print(currententry)
#for key, value in diary.items():
#print('Date: {}, Entry: {}'. format(key, value))




#exceptions

# print entire diary

