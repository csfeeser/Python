## DICTIONARY CHALLENGE

#### Write a script that does the following:

1. Choose a dictionary! [CLICK HERE](https://github.com/csfeeser/Python/blob/master/data%20sets/tlg_dicts.md)

0. Paste your dictionary into your new Python file.

0. Write a script that does the following- **YOU CANNOT EDIT THE DICTIONARY DIRECTLY!**

    - Adds another key/value pair to the dictionary
      > example: "fav_food": "chimichangas"

    - Using a *method* from Lab 19. Python Dictionaries, **print** a list of all the **keys** in your dictionary.

    - Ask your user for input. Have them choose one of those keys you just printed. Save their selection as the variable `choice`.

    - Use the variable `choice` to access your dictionary and return the appropriate value.

  EXAMPLE OUTPUT:
  ```
  >> python3 dictchallenge.py
  
  ["Real Name", "Base", "fav_food"]
  
  Choose a key:
  > fav_food
  
  Deadpool's fav_food is: chimichangas
  ```

## BONUS:

Dummy-proof your code! If the user types in something wacky, try to accommodate for that!

## SUPER BONUS:

Loop over your list of keys-- display them in a numeric list. Allow the user to type in a number to select the correct key.
