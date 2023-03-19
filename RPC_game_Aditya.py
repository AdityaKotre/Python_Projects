#Import random library
import random 

user_wins =0
computer_wins =0

options = ["rock","paper","scissor"]     # Creating 'options' list of elements 


""" Using while loop asking user for his pick
    If user want to quit, then he need to type 'Q'
    And if user input is not present in option then
    it will ask untill the correct pick
"""

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)              #Random number creation by random function
    # rock:0 paper:1 scissors: 2            
    computer_pick = options[random_number]           # Computer pick
    print("Computer picked", computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissor':
        print("You Won!")
        user_wins += 1
    
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You Won!")
        user_wins += 1
    
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("You Won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins +=1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Thanks You, Good Bye")
