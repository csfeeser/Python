## Thursday Warmup!

<img src="https://http.dog/404.jpg" width="300"/>


We learned about Python "IF LOGIC" the other day, and I can't wait to see the projects you folks made! As a warmup this morning, please copy the following code to your IDE of choice:

```python3
#!/usr/bin/env python3

import random

def apigrabber():
    status_codes= [200, 302, 307, 401, 403, 404, 418, 502]
    x= random.choice(status_codes)
    
    return x
    
def main():
    # all of your code will be written in the main function!
    apigrabber()
    
main()
```

### BACKGROUND:

Let's pretend that the function `apigrabber()` is fetching data for us from an online source (a RESTful API). We can tell whether the response we get back from the API is good or not by its **HTTP response**. Even if you've never worked with APIs before, you've surely gotten a `404` error on a website, right? A `404` response most likely means you typed in the wrong address, like *facebool.com* or *gooogle.com*.

[Click here for an adorable guide to HTTP Status Codes!](https://http.dog/)

### OBJECTIVE:

Add code to the `main` function. If the `apigrabber` returns any status code... 
- in the 200's, print the phrase "OK!"
- in the 300's, print the phrase "Redirecting!"
- in the 400's, print the phrase "You done screwed up, son!"
- in the 500's, print the phrase "We done screwed up, son!"

