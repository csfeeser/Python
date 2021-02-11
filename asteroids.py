#!/usr/bin/env python3
  
import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL

    startdate= "start_date=" + input("Choose a start date (YYYY-MM-DD) ")
    enddate= "&end_date=" + input("Choose an end date (YYYY-MM-DD) ")
    mykey = '&api_key=g2dpPgvaIy7V4gdXO8cTKmMMJP2EEwR3RNYb6aQ0' ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey
    print(neourl)

    neodata = (requests.get(neourl)).json()

    sizes= []
    asteroid_distance= []
    asteroid_names= []
    danger_count= 0

    print(f"Total Asteroids in Range: {neodata['element_count']}")
    for date in neodata["near_earth_objects"].keys():
        for aster in neodata["near_earth_objects"][date]:
            sizes.append(aster["estimated_diameter"]["kilometers"]["estimated_diameter_max"])
            asteroid_names.append(aster["name"])
            asteroid_distance.append(aster["close_approach_data"][0]["miss_distance"]["lunar"])
            if aster["is_potentially_hazardous_asteroid"]:
                danger_count += 1

    print(f"Largest Asteroid (kilometers): {max(sizes)}")
    print(f"Closest Asteroid (lunar): {max(asteroid_distance)}")
    print(f"Number of potentially hazardous asteroids: {danger_count}")
    input("Press ENTER to see a list of all asteroids.")
    print(asteroid_names)

if __name__ == "__main__":
    main()
