# Day 1 Skills Review

### Today we covered the following Python skills:
- Creating and executing Python scripts
- Functions (built-in and custom)
- Object type and methods
- Lists and dictionaries
- Importing modules
- Reading in/writing to files
- For loops

### Your challenge is to incorporate some of these skills into a custom script of your making!

1. Put all your code inside of a main() function.

0. Use the data sample below. You can either:
    - **HARD:** paste this into your script as a list. You'll need to put a variable in front of it, something like "`data=`"
    - **HARDER:** paste this into a file named trivia.json. You'll need to use the json module to read this into Python!


    ```
    [
      {
        "category": "General Knowledge",
        "type": "multiple",
        "difficulty": "easy",
        "question": "What machine element is located in the center of fidget spinners?",
        "correct_answer": "Bearings",
        "incorrect_answers": [
          "Axles",
          "Gears",
          "Belts"
        ]
      }
    ]
    ```

0. **HARD:** From the data, print to the stdout (the screen) the following:
    - The question
    - All incorrect answers
    - The correct answer

   **HARDER:** Use a for loop to print out the incorrect answers.
   
   **HARDEST:** Print the question... but print the answers in a random order so the correct answer isn't always the last! *(hint: check out the random module)*
   
### WANT SOME MORE, EH?

4. Use the input() function to let the user try and guess the correct answer! Use the .capitalize() method to eliminate any user capitalization error.

<details>
  <summary>Click here to see a solution!!</summary>
    
    ```python
    #!/usr/bin/python3

    import json
    import random

    def hard(trivia):
        print("NO FOR LOOP")
        print(trivia[0]["question"])
        print(trivia[0]["correct_answer"])
        print(trivia[0]["incorrect_answers"][0])
        print(trivia[0]["incorrect_answers"][1])
        print(trivia[0]["incorrect_answers"][2])
        print()

    def harder(trivia):
        print("WITH FOR LOOP")
        print(trivia[0]["question"])
        print(trivia[0]["correct_answer"])
        for x in trivia[0]["incorrect_answers"]:
            print(x)
        print()

    def hardest(trivia):
        print("RANDOM ORDER")
        print(trivia[0]["question"])
        answers= trivia[0]["incorrect_answers"].copy()
        answers.append(trivia[0]["correct_answer"])
        random.shuffle(answers)
        for x in answers:
            print(x)

    def main():
        # OPTION #1- paste this into your script as a list
        data= [
          {
            "category": "General Knowledge",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What machine element is located in the center of fidget spinners?",
            "correct_answer": "Bearings",
            "incorrect_answers": [
              "Axles",
              "Gears",
              "Belts"
            ]
          }
        ]

        # OPTION 2- read in trivia.json and use json module
        with open("trivia.json","r") as jsonfile:
            data= json.load(jsonfile)

        # Print out the data to the screen. Here are the solutions separated into functions:
        hard(data)
        harder(data)
        hardest(data)

        choice= input("\nWhat is the correct answer?\n>").strip().capitalize()
        if choice == data[0]["correct_answer"]:
            print("Correct!")
        else:
            print(f"Wrong! The answer was {data[0]['correct_answer']}!")

    if __name__ == "__main__":
        main()
    ```
</details>
