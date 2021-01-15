import random


def hangman(word):
    wordlist = [word]
    #word = random.choice(
        #open("C:\\Users\\Debora\\PycharmProjects\\hangman\\resources\\word-list.txt").readlines()).rstrip("\n")

    wrong_guesses = 0
    guessed_letters = []
    stages = ["",
              "__________      ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    # letters - letters is a list containing each character in the variable word.
    letters = list(word)

    board = ["__"] * len(word)
    win = False
    print("\n***********************")
    print(" Welcome to Hangman!!!!")
    print("***********************\n")


    while wrong_guesses < len(stages) - 1:
        # Print a blank space
        print("\n")
        # Collect player guess and save it in the variable guess
        guess = input("Guess a letter: ").lower().strip()
        guessed = guessed_letters.append(guess)
        print(f"Guessed letters: {guessed}")
        # enumerate letters so that if there are multiple instances of a letter, they may all be found
        for ind, item in enumerate(letters):
            if item == guess:
                board[ind] = item
        if guess in letters:
            print(f"Letter {guess.upper()} was found!")
            # If player guessed correctly we get the index of the first occurrence of a character
            cind = letters.index(guess)
            # Use the index to replace the underscore in the board list with the letter
            # board[cind] = guess
            # replace the letter guessed with a dollar sign
            letters[cind] = '$'
        else:
            print(f"Letter {guess.upper()} is not on the board!")
            # if player guess is incorrect we increment the variable wrong_guesses by 1.
            wrong_guesses += 1
            # You call the join method on a space and pass it to a variable board which prints out the board
        print((" ".join(board)))
        e = wrong_guesses + 1
        print("\n".join(stages[0: e]))
        # Check if there are any more underscores left
        if "__" not in board:
            print("Congrats, you guessed the word! You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("Sorry, you ran out of tries. The word was {}.".format(word))


hangman("book")
