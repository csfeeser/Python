# Reading CSV with Python

## In Lab 28, we read in a csv file using the csv module-- with it, we were able to handpick what parts of that data we wanted to use and assign to brand new files. How cool!

This challenge is **COMPLETELY OPEN.** If you like, there are some specific suggestions below, but you're free to attempt anything you wish!

0. If you'd like to work with a collection of comic data, use the command below:

    `student@bchd:~$` `cd ~/mycode && curl https://raw.githubusercontent.com/csfeeser/Python/master/brett_comics.txt > brett_comics.txt`

0. If you'd like to work with data about Pokemon, use the command below:

    `student@bchd:~$` `cd ~/mycode && curl https://raw.githubusercontent.com/csfeeser/Python/master/pokedex.txt > pokedex.txt`

0. If you'd like to work with data regarding 2020 NFL plays, use the command below:

    `student@bchd:~$` `cd ~/mycode && curl http://nflsavant.com/pbp_data.php?year=2020 > nfl2020.txt`
    
0. Use the code below to get you started:

    ```python
    #!/usr/bin/env python3

    import csv

    with open("brett_comics.txt", "r") as comicfile:
    ```
    
 0. *DO SOMETHING COOL WITH THE FILE :)* Here are some ideas to get you started:
 
 - How many of these comics feature Wolverine?
 - Return a list of comics based on the author
 - Create a more readable version of this file for human readability.

## REQUIREMENTS:

- Your script must READ IN a file that contains data.
- Your script must OUTPUT a file using the data you read in.
