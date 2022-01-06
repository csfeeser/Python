# Function Arguments

1. Create a new directory for us to work in.

    `student@bchd:~$` `mkdir -p ~/mycode/func_practice && cd ~/mycode/func_practice`

0. Create a new file and put the following inside. This will 

    `student@bchd:~/mycode/func_practice$` `vim func1.py`

    ```python
    def greet(name, msg):
        """This function takes two values and prints
        them out in the order they are given."""
        print(f"Hello {name}, {msg}")

    greet("Monica", "good morning!")
    ```

0. Save and quit with `:wq`. Then execute the script.

    `student@bchd:~/mycode/func_practice$` `python3 func1.py`

    ```
    Hello Monica, good morning!
    ```

0. Create a new file and put the following inside.

    `student@bchd:~/mycode/func_practice$` `vim func2.py`

    ```python
    def greet(name, msg):
        print(f"Hello {name}, {msg}")

          # these arguments are out of order! We'll get a silly result
    greet("good morning!","Monica")
    ```

0. Save and quit with `:wq`. Then execute the script.

    `student@bchd:~/mycode/func_practice$` `python3 func2.py`

    ```
    Hello good morning!, Monica
    ```

0. Create a new file and put the following inside.

    `student@bchd:~/mycode/func_practice$` `vim func3.py`

    ```python
    def greet(name, msg):
        print(f"Hello {name}, {msg}")

          # we only provided one argument instead of two!
    greet("Monica")
    ```

0. Save and quit with `:wq`. Then execute the script.

    `student@bchd:~/mycode/func_practice$` `python3 func3.py`

    ```
    Traceback (most recent call last):
      File "demo.py", line 6, in <module>
        greet("Monica")
    TypeError: greet() missing 1 required positional argument: 'msg'
    ```

0. Create a new file and put the following inside.

    `student@bchd:~/mycode/func_practice$` `vim func4.py`

    ```python
    def greet(msg, name="Slappy"):
        """This sets a default value for name, 
        if it's not provided"""
        print(f"Hello {name}, {msg}")

          # we did not provide a value for name, but that's ok
    greet("how's it going?")
    ```

0. Save and quit with `:wq`. Then execute the script.

    `student@bchd:~/mycode/func_practice$` `python3 func4.py`

    ```
    Hello Slappy, how's it going?
    ```

0. Create a new file and put the following inside.

    `student@bchd:~/mycode/func_practice$` `vim func5.py`

    ```python
    def greet(msg, name="Slappy"):
        print(f"Hello {name}, {msg}")

    # here we are using the keywords "msg" and "name" to identify our arguments
    # it doesn't matter what order the arguments are presented. This will work.
    greet(msg="my name is Inigo Montoya. Prepare to die.", name="six-fingered man")
    ```

0. Save and quit with `:wq`. Then execute the script.

    `student@bchd:~/mycode/func_practice$` `python3 func5.py`

    ```
    Hello six-fingered man, my name is Inigo Montoya. Prepare to die.
    ```
