# assignment file i/o - Angelique
print()
print("Assignment File I/O")
print()

def read_first_line(file_name):
    open(file_name)
    return file_name.readlines


def main():
    data = read_first_line("test.txt")
    print(data)
    return(data)

main()






