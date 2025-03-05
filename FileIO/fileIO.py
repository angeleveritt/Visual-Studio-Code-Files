# assignment file i/o - Angelique
print()
print("Assignment File I/O")
print()

import os.path

def read_first_line(file_name):
    print("inside read first line")         #working
    file_name=open("test.txt", "r")
    file_lines = file_name.readlines(1)
    print(file_name.readlines)
    file_name.close()
    print("file.closed + ", file.closed)
    return file_lines

def main():
    print("inside main")                    #working
    data = read_first_line("test.txt")
    print(data)
    
    return(data)

main()
