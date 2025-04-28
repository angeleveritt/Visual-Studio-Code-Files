# homework for 2025 03 22
print()
print()

questions = [
    "Lastname, firstname:  ",
     "email address:  ", 
     "If you would like text notifications during the conference, enter your cell:  "
]

#print(questions)           # how do I get this to be on multiple lines so I can see everything?

for question in range (len(questions)+3):  # I toyed with a while loop that would just keep going but I couldn't write it
    print("Welcome to the ABC Conference")
    print()
    print("Please register below")
    print()
    name = input(questions[0])          # I was going to use an index and increase it by one to get to the next question
    if name == "quit":                  # my thinking here is the administrator would know this but not normal users
        break
    email = input(questions[1])
    notification = input(questions[2])
    print("You have registered:  ", name, email, notification)
    questions.append(name)              # I could probably put rules here about the time of input I'm expecting
    questions.append(email)             # I tried to do questions.append(name, email, notification) // is there something like that?
    questions.append(notification)
    
    print("You are registered.  Have an excellent conference!")
  
print() 

print("The complete list of registrants is:  ", questions)  # this works as long as the program is not reinitialized.  need to print to an external file prob.
# how do I get the list to be printed 1,2,3  1,2,3

print()
print(*"fin")
print()


# coupling between logic that captures the input and that which prints it out
# put them together // but we don't like it // prefer to ask questions in the proper sequence and print answers
# modify this program so that questions are in one place // list, not a dictionary, not a set
# all questions go in one place, will put answers in same place
# at end print all answers together
# realpython.com // join and signup for newsletter
#    questions and answers --> good articles on whatever I'm looking for
# geeks for geeks // also very good.  some of the best articles.


#walrus = False
#print(walrus)
#print(walrus  := True) # this assigns True to walrus, makes walrus a boolean, and prints walrus
#print(walrus)
#type(walrus)  # this didn't do anything for me - should get <class 'bool'>
#print("this is right after type(walrus)")

#index = 0

#while index < (len(questions)+1):
  

#name = input("Enter your name (first name [space] last name): ")
#email = input("Enter your email address: ")
#notification = input("If you would like text notifications during the conference, enter your cell: ")
#print(name, email, notification)