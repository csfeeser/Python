### CLASSES/CLASS INHERITANCE

Suggested activities:
- Review labs 56. Creating Classes & 57. Inheritance.
    - Add more cheater classes!
- Review Chad's demo in [creating RPG hero classes](https://github.com/csfeeser/pythondemos/tree/main/7-24)
    - Add more classes!
    - Convert classes into your own preferred theme (SciFi, Western, Zombie Horror, etc.)
 
### STANDARD vs. THIRD PARTY MODULES

In *Lab 20. Standard vs. Third Party Libraries and Open APIs* of the API lab deck, you saw that there are two ways to access APIs with Python; via the standard library and the requests library.
Suggested activities:
- Create a version of your data project that uses the standard library (urllib.request/json) instead of the requests module.

### RECOMMENDED GENERAL PRACTICE

Continue making changes to your data project! There is likely a great deal more information being sent from your chosen API that you aren't taking advantage of yet.
Explore different APIs; slice the lists/dictionaries returned!
Good URLS to try:

| API Name                                 | API URL                                      | Data Type to Request           |
|------------------------------------------|----------------------------------------------|---------------------------------|
| Star Wars API                            | https://swapi.dev/api/people/1               | Neatly display the NAME, HEIGHT, and MASS of this character. Write code that counts up how many films they have been in!  |
| Simpsons Quotes API                     | https://thesimpsonsquoteapi.glitch.me/quotes | Print the quote and the name of the Simpsons character that is returned.                            |
| Pokemon API                               | https://pokeapi.co/api/v2/pokemon | Loop over and print the names of each Pokemon!                              |
| Game of Thrones API                   | https://anapioficeandfire.com/api/characters/583 | Print the NAME of the character, then loop over and display each of their ALIASES.                    |
| "What To Do If You're Bored" API    | https://www.boredapi.com/api/activity | Print the ACTIVITY and number of PARTICIPANTS the activity has. IF there is a suggested activity LINK, display that as well!                          |
