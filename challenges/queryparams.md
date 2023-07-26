# Query Parameter Warmup!

Below is a table of query parameters that can be added on to a GET request of NASA's APOD (Astronomy Picture of the Day) API!

| Parameter   | Type        | Default   | Description                                                                                   |
|-------------|-------------|-----------|-----------------------------------------------------------------------------------------------|
| date        | YYYY-MM-DD  | today     | The date of the APOD image to retrieve                                                        |
| start_date  | YYYY-MM-DD  | none      | The start of a date range, when requesting date for a range of dates. Cannot be used with date.|
| end_date    | YYYY-MM-DD  | today     | The end of the date range, when used with start_date.                                         |
| count       | int         | none      | If this is specified then count randomly chosen images will be returned. Cannot be used with date or start_date and end_date.                                                                                     |
| thumbs      | bool        | False     | Return the URL of video thumbnail. If an APOD is not a video, this parameter is ignored.      |
| api_key     | string      | DEMO_KEY  | api.nasa.gov key for expanded usage                                                           |

Reminder of how query params work:

`BASEURL` + `?` + `key=value` + `&` + `key=value` + `&` + `key=value` ...

Example:

`https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2021-09-21`

### OBJECTIVES:

Rewrite the above URL to meet all the criteria below. TEST that your URL works by trying it in your browser!

Start with this URL and add additional query parameters to meet the criteria. You MUST include the `api_key` query param!: `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`

- return the date of your birthday in 2020!
- return a range of pictures from 7/17/23 to 7/21/23
- return a single random date
