# Simpsons Slicing Challenge!


    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


1. For this challenge, attempt the following:

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


<details>
<summary>CHALLENGE SOLUTION</summary>
    
```python
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]

print(f"My {e}! The {g} do {n}!")
```
    
</details>


<details>
<summary>TRIAL SOLUTION</summary>
    
```python
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

e= trial[2]["goggles"]
g= trial[2]["eyes"]
n= trial[-1]

print(f"My {e}! The {g} do {n}!")
```
    
</details>

<details>
<summary>NIGHTMARE SOLUTION</summary>
    
```python
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

e= nightmare[0]["user"]["name"]["first"]
g= nightmare[0]["kumquat"]
n= nightmare[0]["d"]

print(f"My {e}! The {g} do {n}!")
```
    
</details>
