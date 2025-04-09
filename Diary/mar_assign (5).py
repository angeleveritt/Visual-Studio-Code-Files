import csv

def add_entries(diary):
    while True:
        diary_date = input("Enter the date of the diary entry (yyyy-mm-dd) or done: ")
        if diary_date == "done":
            break 
        diary_entry = input("Enter the diary entry: ")
        diary[diary_date] = diary_entry

    diary = dict(sorted(diary.items()))
    print("Diary Entries:")
    for key, value in diary.items():
        print(f"{key}: {value}")
    try:
        with open('simple.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Key', 'Value'])
            for key, value in diary.items():
                writer.writerow([key, value])
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        exit(1)
    except PermissionError:
        print("Permission denied. Please check the file permissions and try again.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    return diary

def read_existing_entries(diary):
    try:
        with open('simple.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    diary[row[0]] = row[1]
            return diary
    except FileNotFoundError:
        return diary
    except PermissionError:
        print("Permission denied. Please check the file permissions and try again.")
        return diary

    return diary

def initialize():
    diary = {}
    diary = read_existing_entries(diary)
    return diary


def main():
    diary = initialize()
    while True:
        print("Menu:")
        print("1. Add diary entries")
        print("2. Display diary entries")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_entries(diary)
        elif choice == "2":
            print("Diary Entries:")
            for key, value in diary.items():
                print(f"{key}: {value}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
