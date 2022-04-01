## FIZZBUZZ CHALLENGE!

![Image description](https://www.tutorialcup.com/wp-content/uploads/2020/06/FizzBuzz.png)

### This is a commonly used challenge to see if applicants actually know how to code! We'll add in some other requirements, however, to help review some of the content we've learned this week with Python.

#### Part 1

Start by running the following command:

`student@bchd:~$` `wget https://raw.githubusercontent.com/csfeeser/Python/master/challenges/numfile.txt`

Now write a script that does the following:

- Write a **function** that reads in `numfile.txt` (what you just downloaded). Convert the contents of the file into a **LIST**. Your function must **return the list.**

<details>
<summary>Gimme a hint! How do I read in a file?</summary>
<br>
Something like this would read in the file and convert its contents into a list:

```
with open("numfile.txt", "r") as nums:
   nums.readlines()
```
  
</details>

<details>
<summary>How do I return stuff from a function again?</summary>
<br>
Check out this example:
  
```
def add():
  x= 5
  y= 1
  return x + y
  
print(add()) # if we print out what's RETURNed by this function, it would be 6!
```
  
</details>

#### Part 2

- Loop across the new list returned by your function. Print out each element in the list; be sure the output is clean without a bunch of extra whitespaces.

<details>
<summary>How do I do this?</summary>
<br>
Go back and check out Lab 35. Read from Files!
</details>

#### Part 3

Edit your loop. It should still print out each element of the list, but only when certain conditions are met:
  - If the element is a multiple of 3, print "Fizz" instead of the number. 
  - If the element is a multiple of 5, print "Buzz" instead of the number. 
  - If the element is a multiple of both 3 AND 5, print "FizzBuzz" instead of the number.
  - If none of the above are true, just print the number.

<details>
<summary>Gimme a hint! How do I check for multiples of a number?</summary>
<br>
If a number is cleanly divisible by 3 (like 6, 9, 12, 15, etc.) then the following would be TRUE:
  
```
num % 3 == 0
```
  
If a number is cleanly divisible by 5 (like 10, 15, 20, 25) then the following would be TRUE:

```
num % 5 == 0
```
</details>

**SUPER BONUS**: Return how many *Fizz*es, *Buzz*es, and *FizzBuzz*es there are.

**MEGA BONUS**: Make this script as SHORT AS POSSIBLE!
