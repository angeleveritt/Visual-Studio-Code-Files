# assignment file i/o - Angelique
print()
print("Assignment File I/O")
print()

def read_first_line(file_name):
    with open(file_name) as f:
        return f.readline()


def main():
    data = read_first_line(r"C:\Users\angel\OneDrive - ABEveritt Inc\8 ABE Training & Courses\00 2025 02 - UWO Python Programming\Visual Studio Code Files\FileIO\test.txt")
    print(data)             # the little r above tells Windows that this is a raw string and not to be confused by the slashes
    return data

main()






