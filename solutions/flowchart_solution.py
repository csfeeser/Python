quiz= {
"1":{
    "question": "Aye you a horse?",
    "yes": "2",
    "no":"end"
    },
"2":{
    "question": "Do you walk on four legs?",
    "yes": "3",
    "no": "end"
    },
"3":{
    "question": "Really?",
    "yes": "4",
    "no": "end"
    },
"4":{
    "question": "Can you read and write?",
    "yes": "end",
    "no": "5"
    },
"5":{
    "question": "Liar, you're reading this.",
    "yes": "end",
    "no": "end"
    },
"end":{
    "question": "You're not a horse.",
    }
}

start= "1"

while start != "end":
    print(quiz[start]["question"])
    answer= input(">").lower().strip()
    if answer in ["yes","no"]:
        start = quiz[start][answer]
    else:
        print("Please choose yes or no.")

print("You're not a horse.")
