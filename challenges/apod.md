# NASA Astronomy Picture of the Day Challenge

![Image description](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/200px-NASA_logo.svg.png)

**From [NASA.api.gov](https://api.nasa.gov/):**

*One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. In addition, if the concept_tags parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery.*

You can see this API by clicking here: [APOD API Demo](https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY)

This API provides a text description and link to a gorgeous picture from the Hubble telescope!

### Query Parameters

|Parameter|Type|Default|Description|
|---|---|---|---|
|date|YYYY-MM-DD|today|The date of the APOD image to retrieve|
|hd|bool|False|Retrieve the URL for the high resolution image|
|api_key|string|DEMO_KEY|api.nasa.gov key for expanded usage|

## YOUR CHALLENGE:

Write a script that does the following:

0. Accepts input from the user in format of YYYY-MM-DD. This will be the date of the APOD you access!
    > FYI, the APOD API doesn't go earlier than Jun 16, 1995

0. Asks input from the user if they would like their image in High Definition or Standard Definition.

0. Concatenates the API URL which includes:
    - Your own API key.
    - The date of the Astronomical Picture of the Day you'd like to access.
    - Final URL should look something like this: `https://api.nasa.gov/planetary/apod?date=1995-06-16&api_key=HpUcwaRbDIZn0LYbfbFMcEMTPbiPSrokJVvBauK9`
    
0. Uses the `requests` library to return and translate JSON.

0. From the translated JSON, return the following:
    - Date of the picture
    - Title of the picture
    - The text describing what the picture is all about.
    
0. From the translated JSON, use the wget library (or another library if you prefer) to download EITHER the HD image or the SD image depending on the user's input from earlier. This page shows you how to use wget: (https://likegeeks.com/downloading-files-using-python/#Using-wget)

0. Back up to GitHub (including the picture you downloaded), then access the picture on GitHub to bask in its cosmological beauty.

