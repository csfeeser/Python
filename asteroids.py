#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = "api_key=" + nasacreds.strip("\n")
    startdate = "start_date=2019-11-11"
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
    neodata = neowrequest.json()

    asteroid_sizes= {}
    asteroid_names= []
    danger_count= 0
    print(f"Total Asteroids in Range: {neodata['element_count']}")
    for date in neodata["near_earth_objects"].keys():
        for aster in neodata["near_earth_objects"][date]:
            asteroid_sizes[aster["name"]]= aster["estimated_diameter"]["meters"]["estimated_diameter_max"]
            asteroid_names.append(aster["name"])
            if aster["is_potentially_hazardous_asteroid"]:
                danger_count += 1

    print(f"Largest Asteroid (meters): {max(asteroid_sizes)}")
    print(f"Number of potentially hazardous asteroids: {danger_count}")
    input("Press ENTER to see a list of all asteroids.")
    print(asteroid_names)

if __name__ == "__main__":
    main()
