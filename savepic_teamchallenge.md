# SAVE A PICTURE... TEAM CHALLENGE!

### Before you begin, you'll need to install these three third-party modules. Be sure you have them.

    python3 -m pip install wget
    sudo apt install python3-tk
    python3 -m pip install requests

## Objective
You and your teammates will each choose one of the challenges below. Each of you will write a function that exactly fulfills the objective. By combining your code, you'll be able to access an API, pull an image URL from it, download the image to your local machine, and display it in two different ways!

The API we'll be using is https://pokeapi.co/

![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png)

#### TEAM 1:
- Write a function that pulls the API of a user-selected Pokemon from PokeAPI.
- example: https://pokeapi.co/api/v2/pokemon/bulbasaur/
- Your code MUST include the following:

```
def api_pull():
# code goes here!
    return url # the value of url must be a valid url concatenated with user input!
```

#### TEAM 2:
- Write a function that slices through a PokeAPI page and returns the value of "front_default" (it will be a URL to an image).
- Use https://pokeapi.co/ to find it.
- Your code MUST include the following:

```
import requests
def api_slice(url):
    # code goes here!
    return poke_pic # the value of poke_pic must be the URL of the "front_default" image!

api_slice(https://pokeapi.co/api/v2/pokemon/bulbasaur/) # this is a temporary link
```

#### TEAM 3:
- Write a function that uses the wget module to download an image from a link.
- The URL you use should be inside a variable (another function will feed you the URL)
- This page shows you how (https://likegeeks.com/downloading-files-using-python/#Using-wget)
- Your code MUST include the following:

```
import wget
def wget_pic(imagelink):
    # code goes here!
    # image must be saved to /home/student/mycode
```
