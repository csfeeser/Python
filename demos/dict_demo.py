spiderman= {"Place of birth": "New York, New York", 
            "gender": "Male", 
            "height in cm": 177.8, 
            "weight in kg": 75.8, 
            "powers": ["Acrobatics", "Agility", "Spider Sense"], 
            "Alignment": "good",}

# change the value of spiderman's alignment to evil!
spiderman["Alignment"] = "EEEEEEVILLLLLL"

# print out one value from the dictionary
print("Spiderman is from", spiderman["Place of birth"])

# print out the changed value from the dictionary (see line 9)
print(f"Spider is a {spiderman['Alignment']} guy.")

# print the list of spiderman's powers
print("Spiderman's powers include:", spiderman["powers"])

# print one specific power from spiderman's list of powers
print("Spiderman's greatest power is his:", spiderman["powers"][-1])

# our data doesn't include spiderman's real name! The .get() method will
# return None if that key doesn't exist
print("Spiderman's real name is:", spiderman.get("real name"))

# let's add that key to our dictionary
spiderman["real name"] = "Peter Parker"

# this time this will print out spiderman's real name
print("Spiderman's real name is:", spiderman.get("real name"))
