# keyboard-oriented game
# computer thinks of a secret number and player must guess number
# in order to keep it simple at first, do not worry about the random number generator initially
# do not try to solve the entire problem at once - build it up piece by piece

import random      #always do your imports before anything else

print()
print("Welcome to Secret Number")
print()
print("You have up to 10 guesses to get to the randomly chosen number between 1 and 100.")
print("You begin with 100 points and lose 10 points for each incorrect guess.")
print()
high_score = 0

while True:
    user_score = 100   # then declare environment variables; uppercase if constant
    secret_number = 55 #random.randrange(1, 101)   # this is called a literal bc I'm assigning a specific number // this is an integer variable whose value is 4
    # the FROM value is always inclusive and the TO value is always exclusive so you need to go one above
    print()
    print("The highscore for this session is: ", high_score)
    print()

    while True:
        guess = (input("Please enter your guess for the secret number:  "))  # the input function always returns a string UNLESS we add the int
        try:
            guess = int(guess)                                               # not checking for 1 - 100 range bc program still works BUT will make program robust so does not crash w alpha input
        except ValueError:
            print()
            print("Invalid input.  Please enter a number between 1 and 100")
            print()
            continue
                                                                             # if not an integer then exception handled here
        if guess == secret_number:                # comparison is ==      assignment is single =
            print()
            print("You guessed correctly!!!")               
            break
        """else:
            print("Incorrect. Try again.")                  # control C to break out of loop in the Terminal Window
                                                            # changed the structure here so that it breaks once number achieved
    """
        user_score -= 10                                    # this one line handles both ways the guess can be wrong
        if user_score == 0:
            print("You have used up all your points.")         
            break
        
        if guess < secret_number:                           
            print("Your guess is low. 10 point deduction.")
        else:
            print("Your guess is high. 10 point deduction.")

    print()
    print("The secret number is:  ", secret_number)         
    print("Your score is:  ", user_score)
    if user_score > high_score:
        high_score = user_score
        print("Congratulations! You have the new high score: ", high_score)
        print()
    play_again = input("Would you like to play again? yes or no  ")
    if play_again == "yes":
        continue
    break                                                # break always breaks back to the closest while or for loop                       

   

print()
print("Thank you for playing.  Goodbye.")
print()



# homework - add functionality to play again.  if player answers yes then goes again, if no, then game over
    # I haven't figured this out yet.  Do I need to define a function?
    # should I have a Game Class and then methods inside that to play the game?
    # methods would be maybe initiate and then replay?
    # is import pygame something I should do?  seems to be related to video graphics and audio
    # pyglet is a cross-platform library for python - for visually rich games/etc
    # Arcade - modern Python framework for crafting games w compelling graphics & sound

# should I be doing something with __init__() to initialize user_score to 100 at the beginning of each game?
# each game starts with 100 points for user - I think that all that would be in there now is the highscore but eventually maybe name and highscore and date?
# maintain a high score as well and tell the player if they achieved that / this is working but needs to work once I get the multiple game thing working

# I noticed that it let me make too many wrong choices so I also fixed that - it stops the game


# maybe we should be checking for entries that are not between 1 and 100.  If we do, should the program stay at the same position or start over?


# make the high_score work; get things initalized correctly; 