# SAVE & DISPLAY A PICTURE... TEAM CHALLENGE!

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
- Write a function that pulls the API of a user-selected Pokemon  from PokeAPI.
- example: https://pokeapi.co/api/v2/pokemon/bulbasaur/
- Have the function return that link.

#### TEAM 2:
- Write a function that slices through a PokeAPI page and returns the value of "front_default" (it will be a URL to an image).
- Use https://pokeapi.co/ to find it.
- Have the function return that URL!

#### TEAM 3:
- Write a function that uses the wget module to download an image from a link.
- The URL you use should be inside a variable (another function will feed you the URL)
- This page shows you how (https://likegeeks.com/downloading-files-using-python/#Using-wget)

#### TEAM 4:
- Write a function that takes an image link and opens it in a browser! (you'll need to use your virtual desktop to test!) 
- Hmm... didn't we already do that with another lab?...

#### TEAM 5:
- Write a function that uses the Turtle module. Use Turtle to open a local image file and display it (you'll need to use your virtual desktop to test!) 
- Hmm... didn't we already do that with another lab?...

<details><summary>Click here for the solution!</summary>

        #!/usr/bin/python3
        import requests
        import wget
        import turtle
        import webbrowser
        from os import remove
        
        def url():
            while True:
                try:
                    # Using the requests library, pull a Pokemon from the PokeAPI
                    choice= input("What Pokemon would you like a picture of? ")
                    if choice == "":
                        raise ValueError("Don't just hit enter, dummy!")
                    poke_api = requests.get('https://pokeapi.co/api/v2/pokemon/' + choice + '/')
                    poke_api = poke_api.json() # poke_api is the translated API
                    break
                except:
                    print("That is not a valid Pokemon.")
            return poke_api
        
        def get_pic():
            poke_api= url()
            poke_pic_url= poke_api['sprites']['front_default']
            wget.download(poke_pic_url, '/home/student/static/pokepic.gif')
            browser_pic(poke_pic_url)

        def browser_pic(url):
            webbrowser.open(url)
            input("Press ENTER to continue.")
        
        def show_pic():
            screen = turtle.Screen()
            screen.bgpic('/home/student/static/pokepic.gif')
            turtle.mainloop()

        def clean_house():
            try:
                remove('/home/student/static/pokepic.gif')
            except:
                pass

        clean_house()
        get_pic()
        show_pic()
</details>
