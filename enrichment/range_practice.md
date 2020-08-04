## ENRICHMENT: Range()
### Let's get some more practice in using `range()`!



#### PART 1

        range(x, y, z)

        x= number you begin counting from
        y= number you count UP (or down) just short of... this number will not be included in the range!
        z= the increment you'll move by- 1 goes up by one, -2 goes down by two.

1. Observe this output!

        0 1 2 3 4 5 6 7 8 9

2. Use this for loop and replace the `?` with whatever parameters are needed to provide the correct numbers!

        for x in range(?):
            print(x, end= " ")

#### PART 2

3. Using another for loop, generate a list of all the even numbers between 4 and 30 (including 30)!

#### PART 3

4. Write a script that will output ALL 99 LINES of the song *99 Bottles of Beer on the Wall*! If you're unfamiliar with the song, here's what the output would look like:

        99 bottles of beer on the wall!
        99 bottles of beer on the wall! 99 bottles of beer! You take one down, pass it around!
        98 bottles of beer on the wall!
        98 bottles of beer on the wall! 98 bottles of beer! You take one down, pass it around!
        97 bottles of beer on the wall!
        97 bottles of beer on the wall! 97 bottles of beer! You take one down, pass it around!
        [...and so on...]
        
**HINT:** you will need to use `range()` as well as a `for loop` to pull this off.

**EXTRA CREDIT 01:** include an `input()` in your script that allows the user to dictate how many bottles of beer you're counting down from!

**EXTRA CREDIT 02:** don't let the user count down from more than 100 bottles of beer.
        
