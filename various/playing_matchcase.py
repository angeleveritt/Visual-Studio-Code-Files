# angel playing with match case

print()
print("Playing w match case")

print()

command = "Hello, World!"

match command:
    case 'Hello, World!':
        print('Hello to you too.')
    case 'Goodbye, World!':
        print('See your later')
    case other:
        print('No match found')

print()
print("fin")
print()


match command.split():
    case ['show']:
        print('List all files and directories: ')
        #code to list files
    case ['remove', *files]:
        print('Removing files: {}'.format(files))
        #code to reove files
    case _:
        print('Command not recognized')

print()



