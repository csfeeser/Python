# Trivia Game API Challenge!

<img src="https://cdn-learn.adafruit.com/assets/assets/000/078/097/medium800/lcds___displays_Screen_Shot_2019-07-11_at_5.55.22_PM.png" width="500"/>

The Open Trivia Database is a fun API that will return a number of trivia questions in JSON format according to your specifications!
Visit the following page and choose the following:

https://opentdb.com/api_config.php

- Number of Questions: **at least 3**
- Select Category: **YOU CHOOSE!**
- Select Difficulty: **YOU CHOOSE!**
- Select Type: **YOU CHOOSE!**
- Select Encoding: **Default Encoding**

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

### GOALS:

The following are in levels of increasing challenge! Tackle as many as you prefer!

**Level 1**- 
- From the data returned, print out:
  - The question(s)
  - The answers
- Use the [html.unescape()](https://docs.python.org/3/library/html.html#html.unescape) function to convert pesky HTML characters into normal (Unicode) characters!
 
**Level 2**-
- Randomize the order of the answers so the correct one isn't always first.
- Take input from the user accepting their answer... and tell them if they were correct!
- Ensure your code can handle multiple choice AND/OR true/false questions!

**Level 3**-
- Take input from the user that builds a URL that returns the quantity/type of questions they want!
- If it helps, here is a dictionary that breaks down the number associated with each category:

```python
categories= {
9:  "General Knowledge", 
10: "Entertainment- Books", 
11: "Entertainment- Film", 
12: "Entertainment- Music", 
13: "Entertainment- Musicals & Theater", 
14: "Entertainment- Television", 
15: "Entertainment- Video Games", 
16: "Entertainment- Board Games", 
17: "Science- Nature", 
18: "Science- Computers", 
19: "Science- Mathematics", 
20: "Mythology", 
21: "Sports", 
22: "Geography", 
23: "History", 
24: "Politics", 
25: "Art", 
26: "Celebrities", 
27: "Animals", 
28: "Vehicles", 
29: "Entertainment- Comics", 
30: "Science- Gadgets", 
31: "Entertainment- - Japanese Anime & Manga", 
32: "Entertainment- - Cartoon Animations"
}
```
