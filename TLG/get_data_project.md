# Reading Data into Python

This challenge is **COMPLETELY OPEN.** If you like, there are some specific suggestions below, but you're free to attempt anything you wish!

### Objective: Find a large data collection in any format; API, .csv, .txt, .xls, etc. and using Python... do something cool† with it!

#### †**cool**- *adjective* (/ko͞ol/) fashionable, attractive, exciting.

### OPTION 1- APIs

Some of these APIs require an API key to access, some don't! If you need help accessing an API, let Chad know!

- https://fantasy.premierleague.com/api/bootstrap-static/
- https://api.nasa.gov/
- https://www.census.gov/data/developers/guidance/api-user-guide.What_is_the_API.html
- https://www.alphavantage.co/documentation/
- https://magicthegathering.io/
- https://pokeapi.co/
- https://anapioficeandfire.com/
- https://www.dnd5eapi.co/
- https://statsapi.web.nhl.com/api/v1/teams
- https://opentdb.com/api_config.php
- https://openweathermap.org/api
- https://polygon.io/docs/stocks/getting-started
- https://covid19api.com/
- https://www.boredapi.com/

### OPTION 2- Files

Looking to work with files? There are lots of cool data sets out there, but Chad already has a bunch you can choose from if you want! Click the link below to see Chad's selection, and below that are instructions on how to download them.

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
    
**Some ideas for what to do with this data:**
 
 - POKEMON: who has the highest attack rating?
 - ONE PIECE: which is the highest rated episode?
 - COMICS: how many comics feature Wolverine?
 - CARS: which car is most expensive?

## REQUIREMENTS:

- Your script must READ IN data.
- Your script must OUTPUT information from the file in a readable/useful way.
