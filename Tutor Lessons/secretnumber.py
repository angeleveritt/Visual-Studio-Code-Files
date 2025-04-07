# keyboard-oriented game


# computer thinks of a secret number and player must guess number

# in order to keep it simple at first, do not worry about the random number generator initially
# do not try to solve the entire problem at once - build it up piece by piece

import random      #always do your imports before anything else
user_score = 100
high_score = 0
secret_number = random.randrange(1, 101)   # this is called a literal bc I'm assigning a specific number // this is an integer variable whose value is 4
# the FROM value is always inclusive and the TO value is always exclusive so you need to go one above

print("Welcome to Secret Number")
print()
print("You have up to 10 guesses to get to the randomly chosen number.")
print("You begin with 100 points and lose 10 points for each incorrect guess.")
print()
print()

#def secret_number():                                        
while True:
    guess = int(input("Please enter your guess for the secret number:  "))  # the input function always returns a string UNLESS we add the int
    if guess == secret_number:                # comparison is ==      assignment is single =
        print()
        print("You guessed correctly!!!")               # this is working
        break
    """else:
        print("Incorrect. Try again.")                  # control C to break out of loop in the Terminal Window
                                                        # changed the structure here so that it breaks once number achieved
"""
    user_score -= 10                                    # this one line handles both ways the guess can be wrong
    if user_score == 0:
        print("You have used up all your points.")      # this is working    
        break
    
    if guess < secret_number:                           # this is all working
        print("Your guess is low. 10 point deduction.")
    else:
        print("Your guess is high. 10 point deduction.")

print()
print("The secret number is:  ", secret_number)         # this is all working
print("Your score is:  ", user_score)
if user_score > high_score:
    high_score = user_score
    print("Congratulations! You have the new high score.")

print("The current high score is: ", high_score)
print()
"""play_again = input("Would you like to play again?  ")
if play_again == "No":                                   # I    
    break      """                                          # I tried to get it to allow for multiple plays - not working       

print("Thank you for playing.  Goodbye.")
print()



# homework - add functionality to play again.  if player answers yes then goes again, if no, then game over
# I haven't figured this out yet.  Do I need to define a function?
# each game starts with 100 points for user
# maintain a high score as well and tell the player if they achieved that / this is working but needs to work once I get the multiple game thing working
# I noticed that it let me make too many wrong choices so I also fixed that - it stops the game
