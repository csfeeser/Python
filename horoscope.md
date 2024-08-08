# Chad's Temporary Horoscope API Documentation

## Base URL

`https://aux1-00e0c795-7986-4a2c-8053-bdc270b1e23a.live.alta3.com`

> This link will expire at the end of the training week.

## Endpoints

### Get Horoscope for a Specific Sign

#### Endpoint

`GET /horoscope/<sign>`

#### Description

Retrieves the horoscope data for the specified zodiac sign.

#### Parameters

- `sign` (string): The zodiac sign for which you want to retrieve the horoscope. It should be one of the following:
  - aries
  - taurus
  - gemini
  - cancer
  - leo
  - virgo
  - libra
  - scorpio
  - sagittarius
  - capricorn
  - aquarius
  - pisces

#### Example Request

```bash
GET /horoscope/aries
```

#### Example Response

```json
{
    "prediction": "Today is a day for new beginnings. Take a bold step forward.",
    "lucky_color": "Red",
    "lucky_number": 9,
    "mood": "Energetic"
}
```

#### Error Response

If an invalid zodiac sign is provided, the API will return a 404 status code with an error message.

```json
{
    "error": "Invalid horoscope sign"
}
```

## Usage Examples

### Curl

```bash
curl https://aux1-00e0c795-7986-4a2c-8053-bdc270b1e23a.live.alta3.com/horoscope/aries
```

### Python (requests library)

```python
import requests

response = requests.get('https://aux1-00e0c795-7986-4a2c-8053-bdc270b1e23a.live.alta3.com/horoscope/aries')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
```

### JavaScript (Fetch API)

```javascript
fetch('https://aux1-00e0c795-7986-4a2c-8053-bdc270b1e23a.live.alta3.com/horoscope/aries')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

## Notes

- Ensure the Flask server is running at `https://aux1-00e0c795-7986-4a2c-8053-bdc270b1e23a.live.alta3.com` before making requests to the API.
- The API supports only the predefined zodiac signs. Requests with invalid signs will return a 404 error.

This documentation is now updated with the new base URL, allowing users to access the Horoscope API at the specified address.

<details>
<summary>Click here to see the code that made this API!</summary>

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Sample predictions for each sign
horoscope_data = {
    "aries": {
        "prediction": "Today is a day for new beginnings. Take a bold step forward.",
        "lucky_color": "Red",
        "lucky_number": 9,
        "mood": "Energetic"
    },
    "taurus": {
        "prediction": "Patience will bring you rewards. Stay steady and calm.",
        "lucky_color": "Green",
        "lucky_number": 6,
        "mood": "Calm"
    },
    "gemini": {
        "prediction": "Communication is key today. Reach out to an old friend.",
        "lucky_color": "Yellow",
        "lucky_number": 5,
        "mood": "Talkative"
    },
    "cancer": {
        "prediction": "Your intuition is strong. Trust your gut feelings.",
        "lucky_color": "Silver",
        "lucky_number": 2,
        "mood": "Intuitive"
    },
    "leo": {
        "prediction": "A day to shine. Embrace your creativity and lead the way.",
        "lucky_color": "Gold",
        "lucky_number": 1,
        "mood": "Confident"
    },
    "virgo": {
        "prediction": "Organization will bring you peace. Tidy up your space.",
        "lucky_color": "Brown",
        "lucky_number": 7,
        "mood": "Productive"
    },
    "libra": {
        "prediction": "Balance is essential. Seek harmony in your relationships.",
        "lucky_color": "Pink",
        "lucky_number": 4,
        "mood": "Balanced"
    },
    "scorpio": {
        "prediction": "Passion drives you today. Focus on what you love.",
        "lucky_color": "Black",
        "lucky_number": 8,
        "mood": "Passionate"
    },
    "sagittarius": {
        "prediction": "Adventure awaits. Be open to new experiences.",
        "lucky_color": "Purple",
        "lucky_number": 3,
        "mood": "Adventurous"
    },
    "capricorn": {
        "prediction": "Hard work pays off. Keep pushing towards your goals.",
        "lucky_color": "Brown",
        "lucky_number": 10,
        "mood": "Determined"
    },
    "aquarius": {
        "prediction": "Innovation is your strength. Think outside the box.",
        "lucky_color": "Blue",
        "lucky_number": 11,
        "mood": "Innovative"
    },
    "pisces": {
        "prediction": "Dreams are powerful. Pay attention to your night visions.",
        "lucky_color": "Sea Green",
        "lucky_number": 12,
        "mood": "Dreamy"
    }
}


@app.route('/horoscope/<sign>', methods=['GET'])
def get_horoscope(sign):
    sign = sign.lower()
    if sign in horoscope_data:
        return jsonify(horoscope_data[sign])
    else:
        return jsonify({"error": "Invalid horoscope sign"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)
```

</details>
