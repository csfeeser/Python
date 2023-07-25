### JSON MODULE

Run the following command to download a JSON file:
`wget https://raw.githubusercontent.com/csfeeser/Python/master/TLG/devops/example.json`

Write code to open the file then use `import json` to convert the file's contents into a Python dictionary.

### URLS AND QUERIES

Using queries (`?date=2023-07-25`) is a means of returning specific data from an API. Check out [the documentation for the Game of Thrones API](https://anapioficeandfire.com/Documentation). Find the section titled "Constructing a request with pagination." Read up on the `pageSize` and `page` query parameters.
- Can you write a URL that returns characters #51-100? #200-251?

### RECOMMENDED GENERAL PRACTICE

Continue exploring different APIs and manipulating the data that is returned.
Good URLS to try:

| API Name                                 | API URL                                      | Data Type to Request           |
|------------------------------------------|----------------------------------------------|---------------------------------|
| Star Wars API                            | https://swapi.dev/api/people/1               | Neatly display the NAME, HEIGHT, and MASS of this character. Write code that counts up how many films they have been in!  |
| Simpsons Quotes API                     | https://thesimpsonsquoteapi.glitch.me/quotes | Print the quote and the name of the Simpsons character that is returned.                            |
| Pokemon API                               | https://pokeapi.co/api/v2/pokemon | Loop over and print the names of each Pokemon!                              |
| Game of Thrones API                   | https://anapioficeandfire.com/api/characters/583 | Print the NAME of the character, then loop over and display each of their ALIASES.                    |
| "What To Do If You're Bored" API    | https://www.boredapi.com/api/activity | Print the ACTIVITY and number of PARTICIPANTS the activity has. IF there is a suggested activity LINK, display that as well!                          |



