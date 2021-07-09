# Passing Values, Making Files!

<img src="https://images-na.ssl-images-amazon.com/images/I/61xxKWhzOtL._AC_UX569_.jpg" alt="drawing" width="200"/>

Below is a script in need of tweaking!
```python
#!/usr/bin/python3
import random

# data for use below
ship_name= "Bessie"
ship_type= "Intergalactic"
engines= "Dark Matter"
dark_matter_balls= 63
backup_engines= "Chemical"

# create a registration for our spaceship! Print out the following multi-line string with the appropriate data from above plugged in
# BONUS: Write this out to a file called ship_registration.txt instead of printing to screen!
"""
Intergalactic Ship Registration:

  name: DATA NEEDED
  type: DATA NEEDED
  
  engines:
  
    type: DATA NEEDED
      max capacity: DATA NEEDED
    backup: DATA NEEDED
"""

planet= random.choice(["Earth", "Luna Park", "Omicron Persei 8", "Cineplex 14"])

# Choose your level of difficulty for the section below:
  # OPTION 1: 
    # Print out "Good news, everyone! We have another mission to accomplish:" to your screen.
    # Print out the appropriate delivery address below. The planet will be randomly selected!

  # OPTION 2:
    # To a file called "order.txt", add "Good news, everyone! We have another mission to accomplish:"
    # Also to the file "order.txt", add the appropriate delivery address below. The planet will be randomly selected!

print("Good news, everyone! We have another mission to accomplish:")

# if the delivery is to Luna Park, print the following:
"""Delivery to Luna Park
Contents: Prizes for the claw crane
Delivery at: Luna Park, Moon"""

# if the delivery is to Cineplex 14, print the following:
"""Delivery to Cineplex 14
Contents: Popcorn
Delivery at: Cineplex 14"""

# if the delivery is to Omicron Persei 8, print the following:
"""Delivery to Omicron Persei 8
Contents: Candy hearts
Delivery at: Omicron Persei 8"""

# if not any of those destinations, the delivery is to Earth:
"""Delivery to Earth
Contents: R&R / Time Off
Delivery at: HQ"""
```
