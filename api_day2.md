### Warmup Activity: Song Lyric API with Python's Requests Module!

<img src="https://project-static-assets.s3.amazonaws.com/APISpreadsheets/APIMemes/WhoIsJason.jpeg" alt="Who Is Jason Meme" width="300"/>

**Objective**:  
Finish the Python script below. As written, it queries the user for a band name and a song. The script then builds a URL and sends a GET request to a song lyrics API to search it up. But that's not everything we want it to do!

**YOUR TASK**: Check if the response is successful (`status_code` is `200`) and if so the script will print the song lyrics. If the response is not `200`, display `Lyrics not found!` instead.

### Starter Code

```python
import requests

def main():
    # Get user input for band and song (with defaults)
    band = input("Enter the band name (default: 'Beatles'): ") or "Beatles"
    song = input("Enter the song title (default: 'Let it Be'): ") or "Let it Be"

    # Construct the URL
    url = f"https://api.lyrics.ovh/v1/{band}/{song}".replace(" ", "%20")
    print(url)

    # Send GET request
    response = requests.get(url)

if __name__ == "__main__":
    main()
```

---

### Attributes/Methods for the `requests.Response` Object

| Attribute/Method | Description |
| ---------------- | ----------- |
| `.status_code`   | The HTTP status code of the response (e.g., `200` for success). |
| `.json()`        | Parses the response as JSON and returns a dictionary. Useful when the response is JSON-formatted data. |
| `.text`          | Returns the response content as a string (useful if JSON is not available). |
| `.headers`       | Returns the headers from the response. |
| `.reason`        | Textual reason for the status code (e.g., "OK" for `200`). |
| `.ok`            | Boolean value, `True` if `status_code` is 200-299. |
| `.raise_for_status()` | Raises an error if the status code indicates a failure. |

---

### Your Task

1. Check if the response has a `200` status code.
2. If `200`, parse the response to get the lyrics and print them.
3. If not `200`, print `"Lyrics not found!"`.

---

<details>
<summary>Hints</summary>

- Use `response.status_code` to check if the request was successful.
- Use `response.json()` to parse the response data and access the lyrics.

</details>

---

<details>
<summary>Solution</summary>

```python
import requests

def main():
    # Get user input for band and song (with defaults)
    band = input("Enter the band name (default: 'Beatles'): ") or "Beatles"
    song = input("Enter the song title (default: 'Let it Be'): ") or "Let it Be"

    # Construct the URL
    url = f"https://api.lyrics.ovh/v1/{band}/{song}".replace(" ", "%20")
    print("Requesting lyrics from:", url)

    # Send GET request
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        lyrics = response.json().get("lyrics")
        print("\nLyrics:\n", lyrics)
    else:
        print("Lyrics not found!")

if __name__ == "__main__":
    main()
```

</details>
