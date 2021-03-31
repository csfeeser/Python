# FLOWCHART CHALLENGE

**Objective:** Choose one of the flowcharts below. Write a script that allows a user to type in input to answer the questions posed by the flowchart. Have the user's answers direct to the next question and so on until the "conclusion" is reached! *For the sake of the challenge, you may not alter the question/answer structure of the flowchart you choose.*

**DESIGN CHALLENGE**- Place all your questions, answers, and paths inside ONE dictionary!

**BONUS 1-** Your script includes a *Press q to quit* feature which can be used at any time.

**BONUS 2-** Your script controls for human error and repeats the question if the wrong answer is entered.

#### Example Output:
    Basic Engineering!
    ==================
    Does it move?
    > No.
    Should it?
    > Yes.
    Spray some WD-40 on it.

Same script, different result:

    Basic Engineering!
    ==================
    Does it move?
    > Yes.
    Should it?
    > No.
    Wrap it up in duct tape!
    
#### "Are You A Horse?" Flowchart
!["Are You A Horse?" Flowchart](https://github.com/csfeeser/images/blob/master/12-Am-I-a-horse-flowchart.jpg?raw=true)

#### "Are You Hungry?" Flowchart
!["Are You Hungry?" Flowchart](https://github.com/csfeeser/images/blob/master/5-Are-you-hungry-flowchart.jpg?raw=true)

#### "Do You Have A Problem?" Flowchart
!["Do You Have A Problem?" Flowchart](https://github.com/csfeeser/images/blob/master/ayzp0gvl4ehx.jpg?raw=true)

#### "Should You Eat That Bacon?" Flowchart
!["Should You Eat That Bacon?" Flowchart](https://github.com/csfeeser/images/blob/master/should-you-eat-that-bacon-flow-chart-should-you-eat-2740115.png?raw=true)

#### "Should You Eat a Donut?" Flowchart
!["Should You Eat a Donut?" Flowchart](https://github.com/csfeeser/images/blob/master/tumblr_ov54satrIC1s7f9xxo1_1280.jpg?raw=true)

<details><summary>This last flowchart contains profanity. If that doesn't bother you, click here to view.</summary>
	
#### "US Army Problem Solving" Flowchart
!["US Army Problem Solving" Flowchart](https://github.com/csfeeser/images/blob/master/17f461b0a5b48b3f84b00acb6794acbe.jpg?raw=true)

</details>

<!-- 
```python
#!/usr/bin/env python3

def q1():
    print("Does the damn thing work?")
    ans= input("YES or NO")

    if ans == "yes":
        print("DON'T FUCK WITH IT.")
        print("NO PROBLEM.")

    elif ans == "no":
        q2()


def q2():
    print("DID YOU FUCK WITH IT?")
    ans= input("YES or NO")

    if ans == "yes":
        print("YOU DUMB SHIT.")
        q3()

    elif ans == "no":
        q4()

def q3():
    print("DOES ANYONE KNOW?")
    ans= input("YES or NO")

    if ans == "yes":
        print("YOU POOR BASTARD.")
        q5()

    elif ans == "no":
        print("HIDE IT.")
        print("NO PROBLEM.")

def q4():
    print("WILL YOU CATCH HELL?")
    ans= input("YES or NO")

    if ans == "yes":
        print("YOU POOR BASTARD.")
        q5()

    elif ans == "no":
        print("SHIT-CAN IT.")
        print("NO PROBLEM.")

def q5():

    while True:
        print("CAN YOU BLAME SOMEONE ELSE?")
        ans= input("YES or NO")

        if ans == "yes":
            print("NO PROBLEM")
            break

        else:
            print("YOU POOR BASTARD.")

if __name__ == "__main__":
    q1()
```
-->


<!-- 
bank= {
"q1":{"question":"Does the damn thing work?",
      "YES":"DON'T MESS WITH IT.\nNO PROBLEM.", 
      "NO":"q2"},

"q2":{"question":"DID YOU MESS WITH IT?",
      "YES":"q3",
      "NO":"q4"},

"q3":{"question":"YOU MORON.\nDOES ANYONE KNOW?",
      "YES":"q5",
      "NO":"HIDE IT.\nNO PROBLEM"},

"q4":{"question":"WILL YOU GET IN TROUBLE?",
      "YES":"q5",
      "NO":"TOSS IT.\nNO PROBLEM"},

"q5":{"question":"YOU POOR SON OF A GUN.\nCAN YOU BLAME SOMEONE ELSE?",
      "YES":"NO PROBLEM",
      "NO":"q5"}
      } 

start= "q1"
answer= ""

while answer != "Q":
    answer= input(bank[start]["question"]).upper()
    result= bank[start][answer]
    if result in bank.keys():
        start= result
    else:
        print(bank[start][answer])
        break
-->
