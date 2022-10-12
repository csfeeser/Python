# NASA Astronomy Picture of the Day Challenge

![Image description](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/200px-NASA_logo.svg.png)

At the end of class yesterday you were tasked with interacting with one of NASA's APIs, the APOD (Astronomy Picture of the Day)!

**From [NASA.api.gov](https://api.nasa.gov/):**

*One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications.*

You can see this API by clicking here: [APOD API Demo](https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY)

There are two things about this API that separate it from others we've seen; it requires an API key to access and has an extensive chart of query parameters you may use!

### Query Parameters

|Parameter|Type|Default|Description|
|---|---|---|---|
|date|YYYY-MM-DD|today|The date of the APOD image to retrieve|
|hd|bool|False|Retrieve the URL for the high resolution image|
|api_key|string|DEMO_KEY|api.nasa.gov key for expanded usage|
|thumbs|bool|False|Return the URL of video thumbnail. If an APOD is not a video, this parameter is ignored.|

## YOUR CHALLENGE:

### Part 1
Write a script (or edit the script from the lab) so that it does the following:

1. Accepts input from the user in format of YYYY-MM-DD. This will be the date of the APOD you access!
    > FYI, the APOD API doesn't go earlier than Jun 16, 1995

0. Asks input from the user if they would like their image in High Definition or Standard Definition.

0. Concatenates the final API URL which includes:
    - Your own API key.
    - The date of the Astronomical Picture of the Day you'd like to access.
    - Final URL should look something like this: `https://api.nasa.gov/planetary/apod?date=1995-06-16&hd=True&api_key=HpUcwaRbDIZn0LYbfbFMcEMTPbiPSrokJVvBauK9`
    
0. Send a GET request to that address and from the translated JSON return the following:
    - Date of the picture
    - Title of the picture
    - The text describing what the picture is all about.

### Part 2

5. From the translated JSON, download the APOD image from the provided URL. You can use the `requests` library to do this! There are other libraries that work as well, such as `wget`. This page shows you how to use either: (https://likegeeks.com/downloading-files-using-python/#Using-wget)

> I recommend saving your picture to `/home/student/static` so that it can be viewed in the `Files` resource!

### Part 3

6. There are two ways that, depending on the date chosen by the user, that the results could go poorly. How can you write your script to accommodate these two possibilities?
    - not every "Picture of the Day" is a picture. Some are YouTube video links! `2022-01-25` for example returns a YouTube link.
    - not every "Picture of the Day" has an HD version of the image; sometimes only SD is available.



