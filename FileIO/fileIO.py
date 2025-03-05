# assignment file i/o - Angelique
print()
print("Assignment File I/O")
print()
file = open("test.txt")
content = file.readlines()
print("1st line : ", print(content[1]))



def read_first_line(file_name):
    print("inside read first line")         #working
    file = open(file_name, "r")
    print("closed :", file.closed)
    print("mode : ", file.mode)
    file_lines = file.readlines(1)
    print(file.readlines)
    file.close()
    print("file.closed + ", file.closed)
    return file_lines

def main(file_name):
    print("inside main")                    #working
    data = read_first_line(file_name)
    print(data)

    return(data)

main("test.txt")



#def read_first_line(file_name):
    print("inside read first line")         #working
    file = open(file_name, "r")
    print("closed :", file.closed)
    print("mode : ", file.mode)
    file_lines = file.readlines(1)
    print(file.readlines)
    file.close()
    print("file.closed + ", file.closed)
    return file_lines

def main(file_name):
    print("inside main")                    #working
    data = read_first_line(file_name)
    print(data)