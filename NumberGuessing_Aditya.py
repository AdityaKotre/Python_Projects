#Import random module in python

import random

#Please enter the range of the numbers 
top_of_range = input("Please enter range of the numbers upto which you want to guess: ")


""" If range is entered by the user is a digit then it convert
    into integer and if it is not a digit it will show a text
    user to type a number next time.
"""

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type a larger than 0 number next time")
        quit()
else:
    print("Please type number next time")
    quit()

random_number = random.randint(0,top_of_range)   #Random number generation

guesses = 0

""" If guess is entered by the user is a digit then it convert
    into integer and if it is not a digit it will show a text
    user to type a number next time. 
"""

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess is above the number")
    else:
        print("Your guess below the number")

print("You got correct guess in", guesses, "guesses")
        

        
    
        
