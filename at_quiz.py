#!/usr/bin/python3
from questions import questions

print("""
        *--------------------------------*
        | Harry Potter: Sorting Hat Quiz |
        |   Which house will you be in?  |
        *--------------------------------*
""")

turns = 0
scores= {
         "gryffindor": 0,
         "hufflepuff": 0,
         "ravenclaw": 0,
         "slytherin": 0
         }

index = -1

while turns < 12:
    for quest in questions:
        index += 1
        turns += 1
        userinput = input(print(questions[index]["question"])).title()
        if userinput == "A":
            scores["gryffindor"] += 1
        elif userinput == "B":
            scores["hufflepuff"] += 1
        elif userinput == "C":
            scores["ravenclaw"] += 1
        elif userinput == "D":
            scores["slytherin"] += 1
        elif userinput == "Quit":
            exit()    

if turns == 12:
    print("Congrats! You made it to the end!!")
    print("house", max(scores, key=scores.get))
