### Warmup Activity: Favorite Quotes API with Python's Requests Module!

<img src="https://project-static-assets.s3.amazonaws.com/APISpreadsheets/APIMemes/DragonForChristmas.jpeg" alt="Quote Meme" width="300"/>

**Objective**:  
Take the starter Python script below- it interacts with a simple "Fav Quotes" API that Chad spun up. As written, the starter code sends a `GET` request to retrieve all current quotes, displaying them to the user.  

**YOUR TASK**: 
- Add code that uses the `requests` library to send a `POST` request with a new quote.
- Check if the `POST` request is successful ([status code `201`](https://httpstatusdogs.com/201-created)), and if so print `"Quote added successfully!"`
- Otherwise, print `"Failed to add quote!"` with the error message.
- You can see the API in your browser [by clicking here!](https://aux1-7db214f2-7074-4400-abe0-2a5559030ea9.live.alta3.com/quotes)

---

### API Documentation

Use this to help figure out how you can POST to this API!

**Base URL**:  
```
https://aux1-7db214f2-7074-4400-abe0-2a5559030ea9.live.alta3.com/quotes
```

**Endpoints**:

1. **GET /quotes**
   - **Description**: Returns a JSON object containing all saved quotes.
   - **Response Format**:
     ```json
     {
       "quotes": [
         {"name": "Author", "quote": "This is a sample quote."}
       ]
     }
     ```
   - **Expected Status**: `200 OK`

2. **POST /quotes**
   - **Description**: Adds a new quote to the API.
   - **Request Body** (JSON):
     ```json
     {
       "name": "Author's Name",
       "quote": "The quote text here."
     }
     ```
   - **Response**:
     - **Success**: Returns `{"message": "Quote added successfully"}` with status code `201 Created`.
     - **Error**: If a quote by the same name exists, returns `{"error": "A quote by this name already exists"}` with status code `409 Conflict`.

---

### Starter Code

```python
import requests
from pprint import pprint

def main():
    # API URL
    url = "https://aux1-7db214f2-7074-4400-abe0-2a5559030ea9.live.alta3.com/quotes"

    # Send GET request to retrieve all quotes
    response = requests.get(url)
    
    # Check if the GET request was successful
    if response.status_code == 200:
        quotes = response.json().get("quotes", [])
        print("Current quotes in the API:")
        pprint(quotes)

    else:
        print("Failed to retrieve quotes!")

    # TODO: Add code to send a POST request with a new quote

if __name__ == "__main__":
    main()
```

---

<details>
<summary>Hints</summary>

- Use `requests.post()` to send data to the API.
- Set the JSON data in the `data` parameter of `requests.post()` with `{"name": "Author", "quote": "New quote text"}`.
- Check `response.status_code` to confirm if the `POST` was successful.

</details>

---

<details>
<summary>(A) Solution</summary>

```python
import requests
from pprint import pprint

def main():
    # API URL
    url = "https://aux1-7db214f2-7074-4400-abe0-2a5559030ea9.live.alta3.com/quotes"

    # Send GET request to retrieve all quotes
    response = requests.get(url)

    # Check if the GET request was successful
    if response.status_code == 200:
        quotes = response.json().get("quotes", [])
        print("Current quotes in the API:")
        pprint(quotes)
    else:
        print("Failed to retrieve quotes!")

    # Gather user input for a new quote
    name = input("\nWho said your quote?\n>")
    quote = input("\nWhat is the quote?\n>")

    # Construct POST data
    post_data = {
        "name": name,
        "quote": quote
    }

    # Send POST request to add a new quote
    post_response = requests.post(url, json=post_data)

    # Check if the POST request was successful
    if post_response.status_code == 201:
        print("Quote added successfully!")
    else:
        error_message = post_response.json().get("error", "Unknown error occurred!")
        print(f"Failed to add quote: {error_message}")

if __name__ == "__main__":
    main()
```

</details>
