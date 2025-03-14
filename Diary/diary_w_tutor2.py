# assignment - personal diary - Angelique
print()
print("Assignment - Personal Diary")
print()
diary = {}
# 
print("Welcome to your diary")
print()

while True:
    diary_date = input("Enter the date of the diary entry (yyyy-mm-dd): ")
    if diary_date == "quit":
        break 
    diary_entry = input("How do you feel?: ")
    diary[diary_date] = diary_entry

diary = dict(sorted(diary.items()))

print("Diary Entries:")
for key, value in diary.items():
    print(f"{key}: {value}")


# there is a date type but bc I want the date to be the key of the dictionary, keep it string
#dictionaries scale well up to very large

print()
print("fin")
print
