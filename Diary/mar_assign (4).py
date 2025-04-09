import csv
diary = {}

with open('simple.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row) >= 2:
            diary[row[0]] = row[1]

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

with open('simple.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Key', 'Value'])
    for key, value in diary.items():
        writer.writerow([key, value])