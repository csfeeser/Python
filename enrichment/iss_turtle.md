# Lecture - APIs and JSON Decode

### Lab Objective

**The objective of this lab is to place more emphasis on the importance of the import statement in Python, as well as gain exposure to JSON and continue to learn how web APIs work.**

This time we'll determine the current location of the international space station (ISS) via an API, and visualize that information for the user. The data sets used in this lab are very much accurate and in real-time.

*Note: This is a demonstration that requires a GUI. As such, it will be performed by the instructor. If you would like to try this exercise, you need install Python and a Python IDE (such as PyCharm or Visual Studio) on your local machine.*

### Procedure

1. This ISS orbits the Earth every hour and a half. Wow. That's fast. To tell where it is at any given moment, visit this link: http://api.open-notify.org/iss-now.json

0. Create a place to work, such as **isslocation/**
<!--

0. Turtle (graphics) requires a package be installed to Ubuntu (if you miss this step, your script will complain about lacking `python3-tk`

    `student@bchd:~$` `sudo apt install python3-tk`

0. Now you need to call the same webservice from Python. Open a new command window. Let's stay in the habit of organizing our work. For now, make `/home/student/mycode/iss02/` directory.

    `student@bchd:~$` `mkdir ~/mycode/iss02/`

0. Move to the `/home/student/mycode/iss` directory.

    `student@bchd:~$` `cd ~/mycode/iss02/`

0. Open vim.

    `student@bchd:~/mycode/iss02$` `vim /home/student/mycode/iss02/iss_tracking.py`

-->

3. Create the script, `iss_tracking.py`:

    ```python
    #!/usr/bin/python3
    
    import urllib.request
    import json
    
    ## Trace the ISS - earth-orbital space station
    eoss = 'http://api.open-notify.org/iss-now.json'

    ## Call the webserv
    trackiss = urllib.request.urlopen(eoss)

    ## put into file object
    ztrack = trackiss.read()

    ## JSON 2 Python data structure
    result = json.loads(ztrack.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(result)
    input('\nISS data retrieved & converted. Press any key to continue')

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('\nLatitude: ', lat)
    print('Longitude: ', lon)
    ```

0. Run the code. It should display the current location of the ISS.

0. It would be more useful if we were able to show the location of the space station on a map. First we'll need a map. We can get one from https://static.alta3.com/images/python/iss_map.gif

<!--
    `student@bchd:~/mycode/iss02$` `wget https://static.alta3.com/images/python/iss_map.gif -O iss_map.gif`
-->

6. The map should be in the same directory as the script `iss_tracking.py`

0. The map is centered at 0,0 which is what we need.

0. We can place a `turtle` on our map to represent the ISS. What's a turtle? Check out this link to learn more about the turtle graphic module (which ships with Python3 install):

    - https://docs.python.org/3.3/library/turtle.html?highlight=turtle#module-turtle

0. Add the following line to the top of your code.

    ```python
    import turtle
    ```

0. Next we need to set the screen size to match the image, which is 720 x 360. Add the following code to the *bottom* of your code.

    ```python
    screen = turtle.Screen() # create a screen object
    screen.setup(720, 360) # set the resolution
    ```

0. You want to be able to send the turtle to a particular latitude and longitude. To make this easy, set the screen to match the coordinates we are using. Add the following code to the bottom of your program.

    ```python
    screen.setworldcoordinates(-180,-90,180,90)
    ```

0. Add our map to the screen.

    ```python
    screen.bgpic('iss_map.gif')
    ```
0. Now to create an ISS sprite for turtle to use to depict the ISS. First, we'll download a tiny ISS icon to use. We can download one from https://static.alta3.com/images/python/spriteiss.gif

<!--
    `student@bchd:~/mycode/iss02$` `wget https://static.alta3.com/images/python/spriteiss.gif -O spriteiss.gif`
-->


14. Add the following lines to the bottom of your code to register our tiny ISS, and place it on the screen.

    ```
    screen.register_shape('spriteiss.gif')
    iss = turtle.Turtle()
    iss.shape('spriteiss.gif')
    iss.setheading(90)
    ```

0. The ISS starts off in the center of the map, but now let's move it to the correct location on the map. Note, typically you report "Latitude, Longitude", but these are actually (x,y) screen coordinates. So they need to be 'reversed'.

    ```python    
    lon = round(float(lon))
    lat = round(float(lat))
    iss.penup()
    iss.goto(lon, lat)
    turtle.mainloop()
    ```

0. At this time, your code should look like the following.

    ```python
    #!/usr/bin/python3
    
    # standard library imports
    import turtle
    import urllib.request
    import json
    
    ## Trace the ISS - earth-orbital space station
    eoss = 'http://api.open-notify.org/iss-now.json'

    ## Call the webserv
    trackiss = urllib.request.urlopen(eoss)

    ## put into file object
    ztrack = trackiss.read()

    ## JSON 2 Python data structure
    result = json.loads(ztrack.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(result)
    input('\nISS data retrieved & converted. Press the ENTER key to continue')

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('\nLatitude: ', lat)
    print('Longitude: ', lon)

    screen = turtle.Screen() # create a screen object
    screen.setup(720, 360) # set the resolution

    screen.setworldcoordinates(-180,-90,180,90)

    screen.bgpic('iss_map.gif')

    screen.register_shape('spriteiss.gif')
    iss = turtle.Turtle()
    iss.shape('spriteiss.gif')
    iss.setheading(90)

    lon = round(float(lon))
    lat = round(float(lat))

    iss.penup()
    iss.goto(lon, lat)
    turtle.mainloop() # <-- this line should ALWAYS
      # be at the bottom of your script. It prevents the graphic from closing!!!
    ```

0. Test your program by running it. Wait a few seconds, then run it again to see where the ISS has moved to.

0. Pretty cool. Plot a point on our map to represent our city. Replace your code so it looks like the following. Notice that the code has been cleaned up a bit, but otherwise doing the same thing:

    ```python
    #!/usr/bin/python3

    # standard library imports
    import turtle
    import urllib.request
    import json

    ## Trace the ISS - earth-orbital space station
    EOSS = 'http://api.open-notify.org/iss-now.json'

    def main():
        ## Call the webserv
        trackiss = urllib.request.urlopen(EOSS)

        ## put into file object
        ztrack = trackiss.read()

        ## JSON 2 Python data structure
        result = json.loads(ztrack.decode('utf-8'))

        ## display our Pythonic data
        print("\n\nConverted Python data")
        print(result)
        input('\nISS data retrieved & converted. Press any key to continue')

        location = result['iss_position']
        lat = location['latitude']
        lon = location['longitude']
        print('\nLatitude: ', lat)
        print('Longitude: ', lon)

        screen = turtle.Screen()  # create a screen object
        screen.setup(720, 360)  # set the resolution

        screen.setworldcoordinates(-180,-90,180,90)

        screen.bgpic('iss_map.gif')

        ## My location
        yellowlat = 47.6
        yellowlon = -122.3
        mylocation = turtle.Turtle()
        mylocation.penup()
        mylocation.color('yellow')
        mylocation.goto(yellowlon, yellowlat)
        mylocation.dot(5)
        mylocation.hideturtle()

        ## ISS Sprite
        screen.register_shape('spriteiss.gif')
        iss = turtle.Turtle()
        iss.shape('spriteiss.gif')
        iss.setheading(90)

        lon = round(float(lon))
        lat = round(float(lat))
        iss.penup()
        iss.goto(lon, lat)
        turtle.mainloop()

    if __name__ == "__main__":
        main()
    ```

0. Great. Let's create a final version that uses the requests library. In addition, we've added some functions to increase the overall re-usability of the code. Otherwise the code is still doing the same thing:

    ```python
    """Alta3 Research | RZFeeser
       Visualizing tracking the ISS with open API data"""
    
    #!/usr/bin/python3

    # python3 -m pip install requests
    import requests

    # standard library imports
    import turtle

    ## Trace the ISS - earth-orbital space station
    EOSS = 'http://api.open-notify.org/iss-now.json'


    # define a location on the map with a dot
    def mapdot(yellowlat, yellowlon):
        mylocation = turtle.Turtle()
        mylocation.penup()
        mylocation.color('yellow')
        mylocation.goto(yellowlon, yellowlat)
        mylocation.dot(5)
        mylocation.hideturtle()
        return mylocation

    # determine where the ISS is
    def location():
        ## Call the webserv
        trackiss = requests.get(EOSS)

        # was a legal response code returned?
        if trackiss.status_code == 200:
            ## put into file object
            result = trackiss.json()
            ## determine latitude and longitude
            location = result.get('iss_position')  # preference for using the dict.get() method over key recall with []
            lat = location.get('latitude')
            lon = location.get('longitude')
            return (lat, lon)
        else:
            return None  # return None if the location cannot be determined


    def main():
        loc = location()

        # stop execution of main if we cannot track the ISS
        if not loc:
            print("Unable to track ISS")
            return

        ## display our Pythonic data
        print("\n\nConverted Python data")
        print(loc)
        input('\nISS data retrieved & converted. Press any key to continue')
        lat,lon = loc
        print('\nLatitude: ', lat)
        print('Longitude: ', lon)

        ## prep the screen
        screen = turtle.Screen()  # create a screen object
        screen.setup(720, 360)  # set the resolution
        screen.setworldcoordinates(-180, -90, 180, 90) # describe the resolution as 2x as long as it is tall
        screen.bgpic('iss_map.gif')  # set the background image

        ## place a yellow dot at the location of the city we are currently in
        mapdot(47.6, -122.3)  # place got at this lat and lon

        ## Position the ISS Sprite
        screen.register_shape('spriteiss.gif')
        iss = turtle.Turtle()
        iss.shape('spriteiss.gif')
        iss.setheading(90)

        lon = round(float(lon))
        lat = round(float(lat))
        iss.penup()
        iss.goto(lon, lat)
        turtle.mainloop()

    # call the main function
    if __name__ == "__main__":
        main()
    ```

0. If you're tracking your code within an SCM, issue the following commands:
    - `cd ~/mycode/`
    - `git add *`
    - `git commit -m "ISS location lecture"`
    - `git push origin`


<!--

0. Now time to figure out the next time the ISS will be overhead. Copy and paste the following into a new browser tab:

    - http://api.open-notify.org/iss-pass.json *this will result in an error message*.

0. This API web service requires that we pass inputs. Inputs are passed via the URL we use to access the API resource. It's actually rather easy.

    - Inputs are added after a `?`
    - Inputs are separated with a `&`

0. The URL for Seattle, WA would be http://api.open-notify.org/iss-pass.json?lat=47.6&lon=-122.3. Edit the `lat` and `lon` values if you wish to reveal when the ISS will be overhead some other place. The JSON results back will look something like the following:

    ```
    *** EXAMPLE ***
    {
      "message": "success",
      "request": {
        "altitude": 100,
        "datetime": 1527395287,
        "latitude": 47.6,
        "longitude": -122.3,
        "passes": 5
      },
      "response": [
        {
          "duration": 641,
          "risetime": 1527406615
        },
        {
          "duration": 602,
          "risetime": 1527412410
        },
        {
          "duration": 261,
          "risetime": 1527418311
        },
        {
          "duration": 570,
          "risetime": 1527472536
        }
      ]
    }
    ```

0. What you're looking at are multiple passover times. These are given in standard time format. If you haven't yet studied `time`, no big deal. You're looking at a 'standard time format.' It's also called Epoch time, Unix time, POSIX time, or UNIX Epoch time. It's all the same thing and is just a system for describing a point in time, which is defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970. It's easy to convert to human time... if you're a computer. Try some manual conversions of your `risetime` over here: https://www.epochconverter.com/

0. Now we'll call the webservice from Python. Add the following code to the bottom of your script.

    ```python
        passiss = 'http://api.open-notify.org/iss-pass.json'
        passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
        response = urllib.request.urlopen(passiss)
        result = json.loads(response.read().decode('utf-8'))

        ## print(result) ## uncomment to see the downloaded result
    ```

0. The next line will get the first pass over time from the result.

    ```
    over = result['response'][1]['risetime']
    ```   

0. The time is given as a Unix timestamp so we'll need the Python time module so we can print it in a readable form and convert it to local time. To do this we'll need the time module. Add the following comment to the top of your script with your other import statements.

    ```python
        import time
    ```

0. Let's get Turtle to write the passover time by the yellow dot representing our location. The time.ctime() function will convert time so that it is readable. Add the following to the bottom of your script.

    ```python
        style = ('Arial', 6, 'bold')
        mylocation.write(time.ctime(over), font=style)
    ```

0. One last step. **Move** the line `turtle.mainloop()` to the very bottom of your script (CUT and PASTE). This is the line that prevents your map from closing as soon as it opens.

0. Save the program when you're done as `/home/student/mycode/iss02/iss_tracking.py`

0. Make sure your program works. If it doesn't, debug!

0. Set permissions to execute on your program.

0. Run the program.

0. Run the program a few times to ensure it runs.

0. **CODE CUSTOMIZATION 01** - Rewrite this program to call one or more functions. Call those functions so the program still runs. Ask the instructor for help in deciding how to arrange your function(s).

0. **CODE CUSTOMIZATION 02** - Prompt the user for their Latitude and Longitude. Use that to plot their location on the map along with when the ISS will pass over next.

0. **CODE CUSTOMIZATION 03** - Allow the user to reload the map by pressing a key (your choice). Alternatively, import the time library and `time.sleep(5)` within an infinite loop to reload the map every 5 seconds.

-->
