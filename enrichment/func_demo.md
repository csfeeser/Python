0. `student@bchd:~$` `mkdir -p ~/mycode/func_practice && cd ~/mycode/func_practice`

0. `student@bchd:~/mycode/func_practice$` `vim func1.py`

    ```
    def greet(name, msg):
        print(f"Hello {name}, {msg}")

    greet("Monica", "good morning!")
    ```

0. `student@bchd:~/mycode/func_practice$` `python3 func1.py`

    ```
    Hello Monica, good morning!
    ```

0. `student@bchd:~/mycode/func_practice$` `vim func2.py`

    ```
    def greet(name, msg):
        print(f"Hello {name}, {msg}")

    greet("good morning!","Monica")
    ```

0. `student@bchd:~/mycode/func_practice$` `python3 func2.py`

    ```
    Hello good morning!, Monica
    ```

0. `student@bchd:~/mycode/func_practice$` `vim func3.py`

    ```
    def greet(name, msg):
        print(f"Hello {name}, {msg}")

    greet("Monica")
    ```

0. `student@bchd:~/mycode/func_practice$` `python3 func3.py`

    ```
    Traceback (most recent call last):
      File "demo.py", line 6, in <module>
        greet("Monica")
    TypeError: greet() missing 1 required positional argument: 'msg'
    ```

0. `student@bchd:~/mycode/func_practice$` `vim func4.py`

    ```
    def greet(msg, name="Slappy"):
        """This sets a default value for name, 
        if it's not provided"""
        print(f"Hello {name}, {msg}")

    greet("how's it going?")
    ```

0. `student@bchd:~/mycode/func_practice$` `python3 func4.py`

    ```
    Hello Slappy, how's it going?
    ```

0. `student@bchd:~/mycode/func_practice$` `vim func5.py`

    ```
    def greet(msg, name="Slappy"):
        print(f"Hello {name}, {msg}")

    greet(msg="my name is Inigo Montoya. Prepare to die.", name="six-fingered man")
    ```

0. `student@bchd:~/mycode/func_practice$` `python3 func5.py`

    ```
    Hello six-fingered man, my name is Inigo Montoya. Prepare to die.
    ```
