<img src="https://www.brightful.me/content/images/2020/08/shutterstock_686118184.jpg" alt="drawing" width="500"/>

## WARMUP! Write a Flask API that does the following:
  
1. **Make the landing page ("/") return an HTML form.**
   - The form should ask a trivia question of your choosing.
   - The answer should be POSTed to another path.

2. **Depending on the answer POSTed from the form, do the following:**
   - If the answer is correct, redirect your user to the "/correct" route!
   - If the answer is wrong, return them to the form to try again.
   
3. **You will definitely need to import the following:**

    ```python
    from flask import Flask
    from flask import redirect
    from flask import request
    from flask import render_template
    ```
