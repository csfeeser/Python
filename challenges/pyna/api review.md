# Trivia Game API Review!

<img src="https://cdn-learn.adafruit.com/assets/assets/000/078/097/medium800/lcds___displays_Screen_Shot_2019-07-11_at_5.55.22_PM.png" width="500"/>

The Open Trivia Database is a fun API that will return a number of trivia questions according to your specifications!
Visit the following page and choose the following:

https://opentdb.com/api_config.php

- Number of Questions: **Maximum of 3... it will be easier if you choose 1**
- Select Category: **YOU CHOOSE!**
- Select Difficulty: **YOU CHOOSE!**
- Select Type: **Multiple Choice**
- Select Encoding: **Default Encoding**

From the data returned, print out:
- The question
- Each possible answer (both correct and incorrect)

Some code to get you started:

```python
#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
from pprint import pprint

URL= "paste the trivia url here"

def main():
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    pprint(data)
    
if __name__ == "__main__":
    main()
```

### Some helpful code:

- if you `import pprint`, you can `pprint.pprint(data)` to return the JSON in a much more readable format.
- if you `import random`, you can `random.shuffle(listname)` to randomize the order of items in a list.
- `data["results"]` will return the list of question dictionar(ies). `data["results"][0]` will return the first question dictionary.
- `listA.append("stringB")` <-- this will add "stringB" to a list named "listA"
- If you're using Chrome, this [JSON formatter extension](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en) can make reading JSON in your browser a LOT easier!
### Not required, but fun:
- Randomize the order of the answers so the correct one isn't always first.
- Take input from the user accepting their answer... and tell them if they were correct!
- Yuck, some strings have weird characters in them, like this: `What&#039;s the famous line Vaas says in &quot;Far Cry 3&quot;?`
    - to fix this, if you `import html` you can use the `html.unescape(weirdstring)` function to fix those HTML characters.
