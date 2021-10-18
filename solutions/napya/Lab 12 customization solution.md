```
#!/usr/bin/python3
  
import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    print("Choose a date (YYYY-MM-DD)")
    date= input(">")
    if date:
        date= "&date=" + date

    # make a call to NASAAPI with our key
    apod = requests.get(NASAAPI + nasacreds + date + "&thumbs=True").json()

    # ternary operator
    url= 'thumbnail_url' if apod['media_type'] == 'video' else 'url'

    print(f"""
Title: {apod['title']}
Date: {apod['date']}
Explanation: {apod['explanation']}
URL: {apod[url]}""")


if __name__ == "__main__":
    main()
```
