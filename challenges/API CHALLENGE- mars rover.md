# MORNING CHALLENGE: NASA API LOOPING

Begin by copying this code into your environment.

    #!/usr/bin/python3

    import requests
    
    def main():
 

    if __name__ == "__main__":
        main()

Here is the demo API that you are accessing: https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY
You will probably find this site helpful to make sense of the output: https://jsonformatter.org/json-pretty-print

### YOUR CHALLENGE:

**Hard:** Return all the links to a Mars Rover photo in your API response.

*Example*:

    http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000ML0044631240305221E03_DXXX.jpg
    http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000MR0044631230503683E01_DXXX.jpg
    http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000ML0044631230305220E02_DXXX.jpg
    ...

**Harder:** Return every link to a Mars Rover photo in this API ALONG WITH the name of the Rover that took it and the date it was taken.

*Example*:

    ROVER: Curiosity
    DATE: 2015-05-30
    http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000ML0044631240305221E03_DXXX.jpg
    
    ROVER: Curiosity
    DATE: 2015-05-30 
    http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000MR0044631230503683E01_DXXX.jpg
    
    ROVER: Curiosity
    DATE: 2015-05-30 
    http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000ML0044631230305220E02_DXXX.jpg
    ...

**Hardest:** Same as above... but allow the user to type in WHICH CAMERA from Curiosity‡ they'd like their pictures to come from.
> ‡ this is the only rover returned in this particular call

    all_cams= ["FHAZ","RHAZ","MAST","CHEMCAM","NAVCAM"]
