#!/usr/bin/env python3
"""Author: Thomas Stratton || This program is to implement a randomization of quizzes."""
"""Credit: James Peterson  || https://github.com/dragoonbeaga """

import random

class Player:
    def __init__(self):
        self.score= 0
    def win(self):
        self.score += 25
    def get_score(self):
        return self.score

class Question:                         #this is a Class. allows me to point to questions inside of list
    def __init__(self, prompt, answer): #this initiates the class.  (sets what the Class can be called,
        self.prompt = prompt            #defines this variable       #prompt refers to first ?variable? in a list(0),
        self.answer = answer            #    "                       #answer refers to second ?variable? in a list(2))

def run_quiz_Net(questions):                #runs the quiz that is turned on.
    global correct
   # correct = 0
    for question in questions:
        print(f"\nPlayer 1 GO!")
        answer = input(f"{question.prompt}\n:")
        if answer == question.answer:
            player1.win()
        else:
            try:
                player2
                print(f"\nWRONG! Player 2, HERE'S YOUR CHANCE!")
                answer = input(f"{question.prompt}\n:")
                if answer == question.answer:
                    player2.win()
                else:
                    print("NEITHER PLAYERS WIN!")
            except:
                pass

    score_Net()

def run_quiz_Linux(questions):                #runs the quiz that is turned on.
    global correct
    correct = 0
    for question in questions:
        answer = input(f"{question.prompt}\n:")
        if answer == question.answer:
            correct += 25
    score_Linux()

def run_quiz_Python(questions):                #runs the quiz that is turned on.
    global correct
    correct = 0
    for question in questions:
        answer = input(f"{question.prompt}\n:")
        if answer == question.answer:
            correct += 25
    score_Python()

def run_quiz_AWSCP(questions):                    #runs the quiz that is turned on.
    global correct
    correct = 0
    for question in questions:
        answer = input(f"{question.prompt}\n:")
        if answer == question.answer:
            correct += 25
    score_AWS()

def Quiz_Net():                                   #defines the quiz that is created and places questions in a list.
    question_prompts = [
    "\n1. In the OSI Model what is Layer 6?\n(a) Network Layer\n(b) Transport Layer\n(c) Presentation Layer\n(d) Session Layer",

    "\n2. What is the protocol that uses Port 25 to send mail between hosts on the internet?\n"
        "(a) TCP\n(b) SFTP\n(c) SMTP\n(d) FTP",

    "\n3. What is File Hashing?\n(a) Uses an algorithm to see if files are blank\n(b) Uses an algorithm to see if files have been changed\n"
        "(c) To ensure the punctuation is correct in the files\n(d) To ensure files are properly encrypted",

    "\n4. Which IP Address is a valid private address?\n(a) 192.168.1.1\n(b) 164.92.1.23\n(c) 127.0.0.1\n(d) 255.255.255.255"]

    global questions                             #holds the answers to the quiz in a list.
    questions = [Question(question_prompts[0],"c"),Question(question_prompts[1],"c"),
                 Question(question_prompts[2],"b"),Question(question_prompts[3],"a")]

def Quiz_Linux():
    question_prompts = [
    "\n1. What specifically emphasizes the initial operating system deployment?\n(a) Build Automation\n(b) Kill all\n(c) umask\n(d) GRUB",

    "\n2. What command identifies who you are currently logged in as?\n(a) whoami\n(b) who\n(c) grep\n(d) ls -al",

    "\n3. What is Top?\n(a) looks up all files\n(b) Display and manage the top processes\n(c) Takes you to the top of page\n(d) Closes file ",

    "\n4. Who is the creator of Linux?\n(a) Jeff Bezos\n(b) Richard Stallman\n(c) Linus Torvald\n(d) Bill Gates"]

    global questions
    questions = [Question(question_prompts[0], "a"), Question(question_prompts[1], "a"),
                 Question(question_prompts[2], "b"), Question(question_prompts[3], "c")]

def Quiz_Python():
    question_prompts = [
    "\n1. What are the mutable built-ins in Python?\n(a) Strings,Tuples,Numbers\n(b) List,Sets,Dictionaries\n(c) Functions,Sets,Dictionaries"
        "\n(d) Strings,Lists,Classes",

    "\n2. What is the output of the following statement? 'Hello World'[::-1]\n(a) 'Hello World'\n(b) 'World Hello'\n(c) 'dlroW olleH'"                "\n(d)olleh dlroW",

    "\n3. What does Break do in Python Code?\n(a) Brings you to the top\n(b) Terminates loop immediately\n(c) Creates integers\n(d) Pauses",

    "\n4. Suppose list1 = [3,4,5,2,1,0], what is list1 after list1.pop(1)?\n(a) list1=[3,4,5,2,1]\n(b) list1=[3,4,5,2,0]"                              "\n(c) list1=[3,5,2,1,0]\n(d) list1=[3,4,5,2]"]

    global questions
    questions = [Question(question_prompts[0], "b"), Question(question_prompts[1], "c"),
                 Question(question_prompts[2], "b"), Question(question_prompts[3], "c")]

def Quiz_AWSCP():
    question_prompts = [
    "\n1. What is Amazon Route 53?\n(a) A web browser\n(b) A cost effective way to store files on the cloud\n(c) Query data in S3 using SQL"
        "\n(d) Highly available and scalable cloud Domain Name System web service",

    "\n2. What is AWS Snowball?\n(a) A service that transports large amounts of data to and from the cloud\n(b) Packed snow\n(c) A big truck"
        "\n(d) Runs code without thinking about servers",

    "\n3. What service provides low cost highly durable archive storage in the cloud?\n(a) Amazon EC2\n(b) Amazon Glacier\n(c) IAM\n(d) VPC",

    "\n4. What service provides a global content delivery network?\n(a) Amazon EBS\n(b) Amazon CloudFront\n(c) Amazon Neptune\n(d) EC2"]

    global questions
    questions = [Question(question_prompts[0], "d"), Question(question_prompts[1], "a"),
                 Question(question_prompts[2], "b"), Question(question_prompts[3], "b")]

def quiz_list():                               #defines the list of quizzes available in the program.

    global quizlist
    quizlist = ["CompTIA Net+", "CompTIA Linux+", "Python", "AWS Cloud Practitioner"]

def quiz_choice():                             #defines the randomization of the quiz_list.

    random_num= 1  # random.randint(1,4)  
    if random_num == 1:
        Quiz_Net()
        run_quiz_Net(questions)
    elif random_num == 2:
        Quiz_Linux()
        run_quiz_Linux(questions)
    elif random_num == 3:
        Quiz_Python()
        run_quiz_Python(questions)
    elif random_num == 4:
        Quiz_AWSCP()
        run_quiz_AWSCP(questions)

def your_name():                               #defines the input of the user and asks for confirmation of the input.

   # print("Before we begin,")

   # global name
   # name = str(input("What is your name?: "))

   while True:
       num= input("How many players will be playing today? ")

       global player1
       global player2

       if num == "1":
           player1= Player()
           player2= " "
           del player2
           break
       elif num == "2":
           player1= Player()
           player2= Player()
           break

       else:
           print("Not the right number of players!")

   you_sure()

def you_sure():

    try:
        player2
        sure = str(input(f"Two players, then? (y or n): "))
    except:
        sure = str(input(f"One player? (y or n): "))

    if sure.lower() == "y":
        quiz_list()
        quiz_choice()
    else:
        your_name()

def score_Net():                                #defines the scoring metrics for each question scored overall.

    if not player2:
        score = correct
        if(score == 25 or score== 0):
            print(f"Oh No! {score}%! You did not do so well {name}, Would you like to try again?")
            repeat = str(input("y or n: "))
            if repeat.lower() == "y":
                run_quiz_Net(questions)
            else:
                quitter()
        elif score == 50:
            print(f"{score}%! Your getting better {name}, Would you like to try again?")
            repeat = str(input("y or n: "))
            if repeat.lower() == "y":
                run_quiz_Net(questions)
            else:
                quitter()
        elif score == 75:
            print(f"{score}% You passed {name}! But you can do better! Try again?")
            repeat = str(input("y or n: "))
            if repeat.lower() == "y":
                run_quiz_Net(questions)
            else:
                quitter()
        else:
            print(f"{score}%! You aced it, You really know your stuff!! Would you like to try another Quiz?")
            other = str(input("y or n: "))
            if other.lower() == "y":
                quiz_choice()
            else:
                print(f"Have a great day {name}! Please play again soon.")
    print("TIME TO DECLARE THE WINNER!")
    try:
        if player2 and player1.get_score() > player2.get_score():
                    print("Player 1 WINS!")
        elif player2 and player1.get_score() == player2.get_score():
                    print("It's a DRAW!")
        elif player2 and player1.get_score() < player2.get_score():
                    print("Player 2 WINS!")
    except:
        pass

def score_Linux():

    score = correct
    if(score == 25 or score== 0):
        print(f"Oh No! {score}% You did not do so well {name}, Would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Linux(questions)
        else:
            quitter()
    elif score == 50:
        print(f"{score}%! Your getting better {name}, Would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Linux(questions)
        else:
            quitter()
    elif score == 75:
        print(f"{score}% You passed {name}! But you can do better! Try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Linux(questions)
        else:
            quitter()
    else:
        print(f"{score}%! You aced it, You really know your stuff! Would you like to try another quiz?")
        other = str(input("y or n: "))
        if other.lower() == "y":
            quiz_choice()
        else:
            print(f"Have a great day {name}! Please play again soon.")

def score_Python():

    score = correct
    if(score == 25 or score== 0):
        print(f"Oh No! {score}% You did not do so well {name}, Would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Python(questions)
        else:
            quitter()
    elif score == 50:
        print(f"{score}%! Your getting better {name}, Would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Python(questions)
        else:
            quitter()
    elif score == 75:
        print(f"{score}% You passed {name}! But you can do better! Try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_Python(questions)
        else:
            quitter()
    else:
        print(f"{score}%! You aced it, You really know your stuff! Would you like to try another quiz?")
        other = str(input("y or n: "))
        if other.lower() == "y":
            quiz_choice()
        else:
            print(f"Have a great day {name}! Please play again soon.")

def score_AWS():

    score = correct
    if(score == 25 or score== 0):
        print(f"Oh No! {score}% You did not do so well {name}, Would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_AWSCP(questions)
        else:
            quitter()
    elif score == 50:
        print(f"{score}%! Your getting better {name}, Would you like to try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_AWSCP(questions)
        else:
            quitter()
    elif score == 75:
        print(f"{score}% You passed {name}! But you can do better! Try again?")
        repeat = str(input("y or n: "))
        if repeat.lower() == "y":
            run_quiz_AWSCP(questions)
        else:
            quitter()
    else:
        print(f"{score}%! You aced it, You really know your stuff! Would you like to try another quiz?")
        other = str(input("y or n: "))
        if other.lower() == "y":
            quiz_choice()
        else:
            print(f"Have a great day {name}! Please play again soon.")

def quitter():                                    #defines the parameters on how to exit or continue to another quiz.

    print(f"{name}, I can't believe you are quitting!")
    print(f"Goodbye and hope you enjoyed your learning experience {name}!\nUnless, You would like to try your hand at another quiz!")
    other = str(input("y or n: "))
    if other.lower() == "y":
        quiz_choice()
    else:
        print(f"Have a great day {name}! Please play again soon.")

intro = "Welcome to the Technology P.L.A.N !"
print(intro.upper())

your_name()
~                                      
