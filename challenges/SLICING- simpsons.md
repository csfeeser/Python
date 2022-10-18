# Simpsons Slicing Challenge!

Behold! A series of increasingly difficult nested lists/dictionaries!

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

1. Get started by downloading a starter version of this script!

    `student@bchd:~$` `wget https://raw.githubusercontent.com/csfeeser/Python/master/downloads/simpsonslice.py`

0. Open the file to edit it and solve the challenge described below:

    `student@bchd:~$` `vim simpsonslice.py`
    
0. For your morning challenge, attempt the following:

    - From the *challenge* list, pull the strings *eyes, goggles,* and *nothing* and create a print function that returns this output:
        ```
        My eyes! The goggles do nothing!
        ```
    - From the *trial* list, pull the strings *eyes, goggles,* and *nothing* and create a print function that returns this output:
        ```
        My eyes! The goggles do nothing!
        ```
    - From the *nightmare* list, pull the strings *eyes, goggles,* and *nothing* and create a print function that returns this output:
        ```
        My eyes! The goggles do nothing!
        ```
0. You're not allowed to edit any of the lists :)

0. When your script runs, it should output the following:

    ```
    My eyes! The goggles do nothing!
    My eyes! The goggles do nothing!
    My eyes! The goggles do nothing!
    ```
![Image description](https://github.com/csfeeser/Python/blob/master/eyes.jpg?raw=true)

<!--
## SOLUTION

```
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

a= challenge[2][1]
b= challenge[2][0]
c= challenge[3]

print(f"My {a}! The {b} do {c}!")


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

a= trial[2]["goggles"]
b= trial[2]["eyes"]
c= trial[-1]

print(f"My {a}! The {b} do {c}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print(f"My {a}! The {b} do {c}!")
```
