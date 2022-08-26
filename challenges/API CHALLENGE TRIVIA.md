# Trivia Game API Challenge!

<img src="https://cdn-learn.adafruit.com/assets/assets/000/078/097/medium800/lcds___displays_Screen_Shot_2019-07-11_at_5.55.22_PM.png" width="500"/>

The Open Trivia Database is a fun API that will return a number of trivia questions according to your specifications!
Visit the following page and choose the following:

https://opentdb.com/api_config.php

- Number of Questions: **at least 3**
- Select Category: **YOU CHOOSE!**
- Select Difficulty: **YOU CHOOSE!**
- Select Type: **YOU CHOOSE!**
- Select Encoding: **Default Encoding**

From the data returned, print out:
- The question
- The answers

Some code to get you started:

```python
#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "paste the trivia url here"

def main():
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    
if __name__ == "__main__":
    main()
```

### Not required, but fun:
- Randomize the order of the answers so the correct one isn't always first.
- Take input from the user accepting their answer... and tell them if they were correct!
