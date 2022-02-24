# Reading Data Files with Python

**In Lab 28, we read in a csv file using the csv module. We were able to handpick what parts of that data we wanted to use and assign to brand new files. How cool!**

This challenge is **COMPLETELY OPEN.** If you like, there are some specific suggestions below, but you're free to attempt anything you wish!

### Objective: Find a large data collection in .csv, .txt, .xls, etc. format, and using Python... do something cool† with it!

#### †**cool**- *adjective* (/ko͞ol/) fashionable, attractive, exciting.

There are lots of cool data sets out there, but Chad already has a bunch you can choose from if you want! Click the link below to see Chad's selection, and below that are instructions on how to download them.

[CHAD'S DATA SETS](https://github.com/csfeeser/Python/tree/master/data%20sets)

1. If you'd like to work with one of these data sets, open the file in GitHub. Then click the `View Raw` or `Raw` button.

0. Copy the url at the top. It should look something like this:

    `https://raw.githubusercontent.com/csfeeser[...]`

0. At the command line, go to the directory where you'd like to save the file. Then type `wget` and paste the URL you just copied.

    `student@bchd:~` `wget WHATEVERYOURURLWAS`
    
0. You're ready to open the file in a Python script and get cracking! If you need it, here's some starter code:

    ```python
    #!/usr/bin/env python3

    import csv

    with open("brett_comics.txt", "r") as comicfile:
    ```
    
 0. *DO SOMETHING COOL WITH THE FILE :)* Here are some ideas to get you started:
 
 - POKEMON: who has the highest attack rating?
 - ONE PIECE: which is the highest rated episode?
 - COMICS: how many comics feature Wolverine?
 - CARS: which car is most expensive?

## REQUIREMENTS:

- Your script must READ IN a file that contains data.
- Your script must OUTPUT information from the file in a readable/useful way.

<!--
# Reading Data Files with Python

**In Lab 28, we read in a csv file using the csv module. In Lab 38, we read in a massive .xls spreadsheet with 100 years of movies! In both examples, we were able to handpick what parts of that data we wanted to use and assign to brand new files. How cool!**

This challenge is **COMPLETELY OPEN.** If you like, there are some specific suggestions below, but you're free to attempt anything you wish!

### Objective: Find a large data collection in .csv, .txt, .xls, etc. format, and using either csvreader or Pandas... do something cool† with it!

#### †**cool**- *adjective* (/ko͞ol/) fashionable, attractive, exciting.

There are lots of cool data sets out there, but Chad already has a bunch you can choose from if you want! Click the link below to see Chad's selection, and below that are instructions on how to download them.

[CHAD'S DATA SETS](https://github.com/csfeeser/Python/tree/master/data%20sets)

1. If you'd like to work with one of these data sets, open the file in GitHub. Then click the `View Raw` or `Raw` button.

0. Copy the url at the top. It should look something like this:

    `https://raw.githubusercontent.com/csfeeser[...]`

0. At the command line, go to the directory where you'd like to save the file. Then type `wget` and paste the URL you just copied.

    `student@bchd:~` `wget WHATEVERYOURURLWAS`
    
0. You're ready to open the file in a Python script and get cracking! If you need it, here's some starter code:

    ```python
    #!/usr/bin/env python3

    import csv

    with open("brett_comics.txt", "r") as comicfile:
    ```
    
    ```python
    #!/usr/bin/env python3

    import pandas
    
    # data_file= filenamehere.xxx
    
    # Reading in a spreadsheet?
    # dataframeobj = pd.read_excel(excel_file)
    
    # Reading in a csv file?
    # dataframeobj = pd.read_csv(excel_file)
    ```
    
 0. *DO SOMETHING COOL WITH THE FILE :)* Here are some ideas to get you started:
 
 - POKEMON: who has the highest attack rating?
 - ONE PIECE: which is the highest rated episode?
 - COMICS: how many comics feature Wolverine?
 - CARS: which car is most expensive?

## REQUIREMENTS:

- Your script must READ IN a file that contains data.
- Your script must OUTPUT information from the file in a readable/useful way.
-->
