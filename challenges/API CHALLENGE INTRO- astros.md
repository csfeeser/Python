# Morning Warmup: ASTRONAUT TRACKER!

![Image description](https://media1.tenor.com/images/c2e16afc6bff5a5ec0f027f1cc209649/tenor.gif?itemid=15935992)

There has been a lot of activity with astronauts going up and down to the International Space Station! There is a public API that records all current people in space and what vessel they are on. Check it out at http://api.open-notify.org/astros.json

**Your challenge this morning is to do the following:**

1. Using the **requests** module, access the API from the link above and pull/translate the JSON!

    <details>
    <summary>Need help getting started?</summary>
    <br>

    ```python
    #!/usr/bin/python3

    import requests

    URL= "http://api.open-notify.org/astros.json"
    def main():
        # requests.get() sends GET request to the URL
        # .json() strips JSON off the response and translates into Python!
        resp= requests.get(URL).json()

    main()
    ```

    </details>

2. This API changes EVERY SINGLE TIME astronauts leave/arrive in space! Write a script that returns each astronaut and the craft that they are on, which should give the following output:
    
    ```
    People in Space: 10
    Sergey Prokopyev is on the ISS
    Dmitry Petelin is on the ISS
    Frank Rubio is on the ISS
    Fei Junlong is on the Shenzhou 15
    Deng Qingming is on the Shenzhou 15
    Zhang Lu is on the Shenzhou 15
    Stephen Bowen is on the ISS
    Warren Hoburg is on the ISS
    Sultan Alneyadi is on the ISS
    Andrey Fedyaev is on the ISS
    ```

    <details>
    <summary>Need help getting started?</summary>
    <br>

    ```python
    resp= requests.get(URL).json()

    # the API gives us a headcount of people in space
    print(resp["number"])

    # the value of the key "people" is a list of dictionaries, one dictionary per astronaut
    listofdicts= resp["people"]

    # loop over each dictionary, and print out the values of "name" and "craft" from each one
    for astrodict in listofdicts:
        print(astrodict["name"])
        print(astrodict["craft"])
    ```

    </details>


