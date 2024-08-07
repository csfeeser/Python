# Final Project- FLASK API!

<img src="https://github.com/user-attachments/assets/5415c02e-1632-4f71-a971-005278994605" width="400" alt="flask haha">

> I refuse to apologize for niche video game references.

The objective of this project is to function as proof of basic proficiency with Flask and the ability to access RESTful APIs. Code will be graded on a pass / fail basis on the following criteria:
- Does the code include the required features?
- Does the code work?


### Procedure

This project must include (at least) **two (2)** scripts. One called **alta3research-flask01.py** and a second called **alta3research-requests02.py**

1. Your script **alta3research-flask01.py** should demonstrate proficiency with the `flask` library. Ensure your application has:
    - at least two endpoints
    - at least one of your endpoints should return JSON
    - has **ONE** additional feature from the following list:
        - one endpoint returns HTML that uses jinja2 logic
        - requires a `session` value be present in order to get a response
        - writes to/reads from a cookie
        - reads from/writes to a sqlite3 database

2. Your script **alta3research-requests02.py** should demonstrate proficiency with the `requests` HTTP library. This script should:
    - send a GET request to your Flask API; it should target the endpoint that returns JSON.
    - take the returned JSON and "normalize" it into a format that is easy for users to understand. 
    - [Click here for a guide on how to do this!](https://github.com/csfeeser/Python/blob/master/pyapi/flask_JSON_demo_API.md)
