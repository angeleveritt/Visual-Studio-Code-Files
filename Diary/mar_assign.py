diary = {}
while True:
    diary_date = input("Enter the date of the diary entry (yyyy-mm-dd): ")
    if diary_date == "quit":
        break 
    diary_entry = input("Enter the diary entry: ")
    diary[diary_date] = diary_entry

diary = dict(sorted(diary.items()))
print("Diary Entries:")
for key, value in diary.items():
    print(f"{key}: {value}")