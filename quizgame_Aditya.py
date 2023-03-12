#Welcome to the quiz game
print("Welocome to quiz game")

#Do you want to play this game?
playing = input("Do you want to play? ")

#Checking whether user want to play or not.
if playing.lower() != "yes":
    quit()

print("Ok! Let's start")

Score = 0
#Instructions
print("Instructions")
print("While giving the answer. Please, Write only answer. Do not use answer Sr. number")


#Questions 

#First question
print("Who was the first Prime Minister of India? " "A- Indira Gandhi",
      "B- Narendra Modi",
      "C - Jawaharlal Nehru",
       "D - Rajiv Gandhi")
answer = input("Please, Write your answer here: ")

if answer == "Jawaharlal Nehru":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Second question
print("What is the capital city of India? A: New Delhi B: Mumbai  C :Kolkata D :Chennai")
answer = input("Please, Write your answer here: ")

if answer == "New Delhi":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Third question
print("Which state is also known as the “Fruit Bowl” of India? A: Jammu and Kashmir B: Himachal Pradesh C: Assam D : Meghalaya")

answer = input("Please, Write your answer here: ")

if answer == "Himachal Pradesh":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Fourth question
print("Who is Sachin Tendulkar? A: Indian Hockey player B: Indian Cricketer C: Indian Kabaddi player D: Indian Marathon Runner")

answer = input("Please, Write your answer here: ")

if answer == "Indian Cricketer":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Fifth question
print("Who discovered India?  A: Vasco da Gama B: Christopher Columbus C: James Cook D: Willem Janszoon")
answer = input("Please, Write your answer here: ")

if answer == "Vasco da Gama":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Sixth question
print("Who is popularly known as the “Iron Man” of India? A: Lal Bahadur Shastri B: Sardar Vallabh Bhai Patel C: Mahatma Gandhi D: Dr. B.R Ambedkar")
answer = input("Please, Write your answer here: ")

if answer == "Sardar Vallabh Bhai Patel":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Seven question
print("Which is the national sport of India? A: Cricket B: Hockey C: Kabaddi D: Football")
answer = input("Please, Write your answer here: ")

if answer == "Hockey":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Question Eight
print("Who is the current President of India? A: Draupadi Murmu B: Ram Nath Kovind C: Pratibha Patil D: A. P. J. Abdul Kalam")
answer = input("Please, Write your answer here: ")

if answer == "Draupadi Murmu":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Question nine
print("Which place in India is also known as the “Land of Rising Sun”? A: Sikkim B: Arunachal Pradesh C: Karnataka D: Gujarat ")
answer = input("Please, Write your answer here: ")

if answer == "Arunachal Pradesh":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")


#Question Ten
print("Where is Taj Mahal located in India? A: Mumbai B: Agra C: Delhi E:Kolkata")
answer = input("Please, Write your answer here: ")

if answer == "Agra":
    print("Correct!")
    Score +=1
else:
    print("Incorrct!")

print("Your score is" +str(Score)+ ".")