print("Welcom to my star wars quiz game!")

playing = input("Would you like to play? Type yes to begin or no to quit: ").lower()

if playing != "yes":
    quit()

print("Ok lets play!")
score = 0

answer = input("Where was Luke Sky Walker born? ")
if answer.lower() == "polis massa": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

answer = input("What planet did Luke grow up on? ")
if answer.lower() == "tatooine": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

answer = input("Who was Luke's mentor? ")
if answer.lower() == "obi-wan kenobi": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

answer = input("What is Luke's sisters name? ")
if answer.lower() == "leia": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

answer = input("Who is Luke's father? ")
if answer.lower() == "anakin skywalker": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

answer = input("What is the name of the ship Han Solo owns? ")
if answer.lower() == "millenium falcon": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

answer = input("Who was the first Captain of the Millenium Falcon? ")
if answer.lower() == "lando calrissian": 
    print("Correct")
    score += 1
else: 
    print("Incorrect!") 

print("You got: " + str((score / 7) * 100) + "%")
print("Thank you for playing!")
