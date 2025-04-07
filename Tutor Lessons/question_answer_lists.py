# homework for 2025 03 22
print()
print()

questions = [
    "email address:  ", 
     "If you would like text notifications during the conference, enter your cell:  ",
     "Conference badge number:  "  
]
while True:

    attendee_name = input("Enter your name (lastname, firstname), QUIT to leave:  ")
    if attendee_name.upper() == "QUIT":         #.upper causes the response to be converted to uppercase
        break

    #print(questions)          
    answers = []

    print("Welcome to the ABC Conference")
    print()
    print("Please register below")

    for question in questions:    # not a good idea to use a single character variable name.  Less opportunity for misinterpreting.
        answer = input(question)          
        answers.append(answer)
            
    print("You are registered.  Have an excellent conference!")


    number_of_questions = len(questions)
    for index in range(number_of_questions):    # for index in range(len(questions))
        print(questions[index], answers[index])  # eventually, when multiple users, you will have a nested list for the answers

   print()

    # eventually the questions and answers would be combined into a dictionary and stored in a file
    # might use the badge number as a key 

    # he will take me through some teaching next week
