# JSON to Python Challenge- Part 2!

1. Yesterday we wrote a script that parsed a JSON object with the json module. We were able to return values from Stacy Townsend... but there are more people in this JSON file!

2. We're going to build a contact document using data from EVERYONE in the office.

3. Write a script that will:
- Import the challenge.json file and convert it into Python data
- Loop across the data and collect **name, email, phone,** and **address** from each person.
- Output those four pieces of information to look like this:
    
    Name: Chad Feeser
    Email: csfeeser@alta3.com
    Phone: +1 (222) 333-4444
    Address: 1600 Pennsylvania Avenue NW, Washington, DC 20500

**BONUS**: Have one additional line that lists each person's friends!
    
    Friends: Moe Howard, Larry Fine, Curly Joe DeRita
    
**TIP:** Use https://jsonformatter.org/json-pretty-print to make finding/slicing this information easier!

**NEED HELP GETTING STARTED?** Here is a completed script of what we were able to accomplish yesterday.

    `student@beachhead:~/pyapi$` `cd ~/pyapi/ && vim ~/pyapi/valentinechallenge2.py`


    #!/usr/bin/python3

    import json

    def main():
        with open("challenge.json", "r") as data:
            datastring = data.read()

        datadecoded = json.loads(datastring)

        # Name
        print(datadecoded[3]["name"])

        # Eye color
        print(datadecoded[3]["eyeColor"])

        # Favorite fruit
        print(datadecoded[3]["favoriteFruit"],"\n")

        print(f"Ah, {datadecoded[3]['name']}.")
        print(f"Eyes like a lime, citrus {datadecoded[3]['eyeColor']}.")
        print(f"Have a {datadecoded[3]['favoriteFruit']}.")

    main()
    
1. In case you didn't yesterday, this is how to create the JSON file we're parsing in this lab.

    `student@beachhead:~/pyapi$` `vim ~/pyapi/challenge.json`

    ```
    [
      {
        "_id": "60186e63371ab4ca0966ac39",
        "index": 0,
        "guid": "3a7e5060-df81-45e9-8423-7e6aff21ea35",
        "isActive": false,
        "balance": "$1,790.42",
        "picture": "http://placehold.it/32x32",
        "age": 37,
        "eyeColor": "brown",
        "name": "Iva Dyer",
        "gender": "female",
        "company": "DOGTOWN",
        "email": "ivadyer@dogtown.com",
        "phone": "+1 (989) 405-3876",
        "address": "636 Box Street, Frizzleburg, Idaho, 6649",
        "about": "Deserunt tempor veniam ut sint Lorem ut irure cupidatat exercitation nisi exercitation ad. Culpa consequat commodo sit dolore qui nulla fugiat. Quis amet voluptate laborum aliqua. Officia excepteur aliquip pariatur occaecat Lorem in consequat. Do non reprehenderit aliquip dolor.\r\n",
        "registered": "2016-12-12T10:31:44 +05:00",
        "latitude": -31.953242,
        "longitude": 45.710017,
        "tags": [
          "sunt",
          "minim",
          "dolore",
          "ullamco",
          "consectetur",
          "quis",
          "esse"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Livingston Underwood"
          },
          {
            "id": 1,
            "name": "Wolfe Kennedy"
          },
          {
            "id": 2,
            "name": "Briana Rosario"
          }
        ],
        "greeting": "Hello, Iva Dyer! You have 9 unread messages.",
        "favoriteFruit": "strawberry"
      },
      {
        "_id": "60186e63c3a37cbe7dea4ed4",
        "index": 1,
        "guid": "c729c4d3-1507-4582-a1af-79f4a888d4a1",
        "isActive": false,
        "balance": "$2,383.93",
        "picture": "http://placehold.it/32x32",
        "age": 30,
        "eyeColor": "green",
        "name": "Phyllis Barker",
        "gender": "female",
        "company": "ASSURITY",
        "email": "phyllisbarker@assurity.com",
        "phone": "+1 (884) 553-2072",
        "address": "160 Putnam Avenue, Harmon, Pennsylvania, 5086",
        "about": "Quis occaecat cillum esse cupidatat labore sunt commodo laborum voluptate velit. Officia fugiat minim laborum pariatur sint nostrud eu amet id. Ea in excepteur amet esse fugiat. Occaecat deserunt ipsum ad Lorem est anim minim eu qui dolor Lorem. Voluptate eiusmod dolore Lorem enim id. Officia reprehenderit culpa nostrud sint dolor consectetur.\r\n",
        "registered": "2019-08-26T09:51:02 +04:00",
        "latitude": 12.584119,
        "longitude": -135.819072,
        "tags": [
          "ad",
          "commodo",
          "magna",
          "laborum",
          "aliqua",
          "qui",
          "ut"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Juliet Frederick"
          },
          {
            "id": 1,
            "name": "Schmidt Henson"
          },
          {
            "id": 2,
            "name": "Mamie Walter"
          }
        ],
        "greeting": "Hello, Phyllis Barker! You have 9 unread messages.",
        "favoriteFruit": "apple"
      },
      {
        "_id": "60186e63650ed5d2e87e3fa2",
        "index": 2,
        "guid": "8b7b5a97-521a-4e8b-8077-be70d229debe",
        "isActive": true,
        "balance": "$3,768.07",
        "picture": "http://placehold.it/32x32",
        "age": 31,
        "eyeColor": "green",
        "name": "Walters Donovan",
        "gender": "male",
        "company": "FREAKIN",
        "email": "waltersdonovan@freakin.com",
        "phone": "+1 (871) 580-2298",
        "address": "260 Fay Court, Linwood, North Dakota, 1523",
        "about": "Amet enim magna nisi occaecat exercitation ullamco amet exercitation ad cillum aliquip. Id commodo sunt voluptate do est reprehenderit exercitation. Laboris laboris fugiat exercitation eiusmod incididunt veniam nisi aliquip do aliquip cupidatat excepteur. Id ut consectetur ullamco aute enim deserunt adipisicing quis esse qui. Enim culpa ad ad nisi. Aliqua cillum veniam tempor aliqua reprehenderit Lorem in culpa.\r\n",
        "registered": "2019-12-03T09:50:58 +05:00",
        "latitude": 2.911449,
        "longitude": -78.279087,
        "tags": [
          "duis",
          "dolore",
          "occaecat",
          "consectetur",
          "esse",
          "minim",
          "labore"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Blanchard Gamble"
          },
          {
            "id": 1,
            "name": "Geraldine Brooks"
          },
          {
            "id": 2,
            "name": "Pruitt Blackwell"
          }
        ],
        "greeting": "Hello, Walters Donovan! You have 8 unread messages.",
        "favoriteFruit": "apple"
      },
      {
        "_id": "60186e638e69ca5cdaf6e231",
        "index": 3,
        "guid": "b10c8dbd-aebe-427b-b442-e72d4287fa4f",
        "isActive": true,
        "balance": "$2,521.98",
        "picture": "http://placehold.it/32x32",
        "age": 32,
        "eyeColor": "green",
        "name": "Stacy Townsend",
        "gender": "female",
        "company": "UPLINX",
        "email": "stacytownsend@uplinx.com",
        "phone": "+1 (860) 456-3598",
        "address": "525 Bartlett Street, Wilmington, Minnesota, 8079",
        "about": "Incididunt magna elit irure ullamco aute ea ea Lorem pariatur ex commodo. Nulla eiusmod mollit dolore magna id minim nostrud aliqua culpa commodo irure. Voluptate esse eiusmod exercitation in fugiat pariatur ullamco aliquip minim laborum ex sit. Eu do adipisicing ut officia reprehenderit nulla labore dolore elit et officia non ullamco nisi.\r\n",
        "registered": "2014-11-17T11:41:10 +05:00",
        "latitude": 23.181604,
        "longitude": 53.024015,
        "tags": [
          "Lorem",
          "Lorem",
          "exercitation",
          "officia",
          "tempor",
          "ipsum",
          "consectetur"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Claire Chaney"
          },
          {
            "id": 1,
            "name": "Mia Wallace"
          },
          {
            "id": 2,
            "name": "Queen Dalton"
          }
        ],
        "greeting": "Hello, Stacy Townsend! You have 10 unread messages.",
        "favoriteFruit": "strawberry"
      },
      {
        "_id": "60186e6306387d0b5dfadbac",
        "index": 4,
        "guid": "11034615-36d5-4c8f-9d14-69fab6070132",
        "isActive": true,
        "balance": "$1,686.69",
        "picture": "http://placehold.it/32x32",
        "age": 38,
        "eyeColor": "brown",
        "name": "Rosella Whitley",
        "gender": "female",
        "company": "CENTREXIN",
        "email": "rosellawhitley@centrexin.com",
        "phone": "+1 (925) 433-3346",
        "address": "895 Harden Street, Tioga, Mississippi, 9301",
        "about": "Magna quis do Lorem duis ipsum dolor aute est. Quis ex aute nostrud reprehenderit non dolor dolore ipsum velit eu sint. Nostrud nulla laboris dolore enim irure voluptate deserunt magna tempor aliqua consectetur. Voluptate eu quis ullamco sunt fugiat quis irure velit mollit proident magna ut voluptate. Sunt proident et eu eiusmod do ipsum enim tempor labore in labore cillum exercitation.\r\n",
        "registered": "2018-04-19T04:24:45 +04:00",
        "latitude": 73.493129,
        "longitude": 78.385639,
        "tags": [
          "ad",
          "cillum",
          "aliquip",
          "et",
          "sit",
          "eu",
          "aliqua"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Yang Boyer"
          },
          {
            "id": 1,
            "name": "Stewart Mooney"
          },
          {
            "id": 2,
            "name": "Woodward Trujillo"
          }
        ],
        "greeting": "Hello, Rosella Whitley! You have 3 unread messages.",
        "favoriteFruit": "strawberry"
      }
    ]
    ```
