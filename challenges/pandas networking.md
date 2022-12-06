## Morning Challenge!

Clone the following git repo.

`cd && git clone https://github.com/csfeeser/downloads.git`

Now move into that directory.

`cd ~/downloads`

Check out the spreadsheet inside.

`ls ~/downloads`

```
switches.xlsx
```

<img src="https://github.com/csfeeser/images/blob/master/switches.png?raw=true" width="200"/>

#### OBJECTIVE

**Automate reading in the spreadsheet with switch data and passing it along to further parts of your code (configuring/maintenance/etc.)**

Write a script using the `pandas` module. Aim to achieve as many of the following as you can! No worries if you don't get them all.

- read in the `switches.xlsx` file as a dataframe (`pd.read_excel`)
- sort the switches by driver type (`sort_values`)
- convert your dataframe to a list with the `to_dict(orient='records')` method.
- write a for loop over the returned list. See if you can create this output:

```
The driver of switch 3.3.3.3 is arista eos
The driver of switch 6.6.6.6 is arista eos
The driver of switch 7.7.7.7 is arista eos
The driver of switch 1.1.1.1 is cisco ios
The driver of switch 5.5.5.5 is cisco ios
The driver of switch 2.2.2.2 is cisco nxos
The driver of switch 4.4.4.4 is juniper junos
```

**Here's an example of a for loop over a similar object:**

```
heroes= [{"name": "Batman", "power":"money"},
         {"name": "Wonder Woman", "power": "the lasso of truth"},
         {"name":"Superman", "power":"...everything"}
        ]

for hero in heroes:
    print(f"The hero {hero['name']} has {hero['power']} as their power.")
```
