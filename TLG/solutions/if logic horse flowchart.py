#!/usr/bin/env python3

import os

horse= {
        1:{"q":"Are you a horse?",
           "yes": 2,
           "no": "last"},
        2:{"q":"How many legs do you walk on?",
           "two": "last",
           "four": 3},
        3:{"q":"Really?",
           "no": 4,
           "yes": 4},
        4:{"q":"Can you read and write?",
           "no": 5,
           "yes": "last"},
        5:{"q":"Liar, you're reading this.",
           "no": "last",
           "yes": "last"},
       }

os.system("clear")
question= 1

while question != "last":
    print(horse[question]["q"])
    for x in horse[question]:
        if x != "q":
           print(f" - {x}")
    answer= input("\n>").strip().lower()
    os.system("clear")
    if answer in horse[question]:
        question= horse[question][answer]
        if question == "last":
            print("You're not a horse.")
    else:
        print("That's not an acceptable answer.")
