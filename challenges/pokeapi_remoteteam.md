# SAVE A PICTURE... TEAM CHALLENGE!

### Before you begin, you'll need to install these three third-party modules. Be sure you have them.

    python3 -m pip install wget
    python3 -m pip install requests

## Objective
You will be assigned one of the challenges below. You will write a function that exactly fulfills the objective. **IMPORTANT**- this function is meant to be *imported* upon completion. **Test your code by creating a main() function that is called by:** 
    
    if __name__ == "__main__" 
    
The API we'll be using is https://pokeapi.co/

![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png)

#### FUNCTION 1:
- Write a function that pulls the API of a **user-selected Pokemon** from PokeAPI.
- **PASS/FAIL**- Whether or not your function returns a translated JSON result from something like https://pokeapi.co/api/v2/pokemon/bulbasaur/ <-- but the pokemon was selected by input!
- Your code MUST include the following:

```
import requests

def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    # code goes here!
    return pokedict # the value of pokedict is the translated JSON returned from a valid url concatenated with user input!
```


#### PLAYER 2:
- Write a function that slices through a PokeAPI dictionary and returns the value of "front_default" (it will be a URL to an image).
- Use PokeAPIs collapsible dictionaries/lists to make it easier on yourself!
- **PASS/FAIL**- Whether or not your function returns a string that looks something like "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
- Your code MUST include the following:

```
def api_slice(json2python):
    poke_pic= json2python[]
    return poke_pic

```

#### PLAYER 3:
- Write a function that uses the wget module to download an image from a link.
- The URL you use should be inside a variable (another function will feed you the URL)
- This page shows you how: (https://likegeeks.com/downloading-files-using-python/#Using-wget)
- **PASS/FAIL**- whether or not your function downloads a pokemon PNG image to `home/student/mycode/` from a link like https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png
- Your code MUST include the following:

```
import wget

def wget_pic(imagelink):
    # code goes here!
    # image must be saved to /home/student/mycode

```

#### FINAL PRODUCT:

- When the functions from all three team members are combined, they should be able to be called by this script!

```
#!/usr/bin/python3
import requests
import wget

def main():
    wget_pic(api_slice(json_conv(api_pull())))

main()
```
    
