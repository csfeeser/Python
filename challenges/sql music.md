## Python, Databases, and Pandas... oh my!

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--juXh8LB2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/dd6fwk650pg5f3f48aea.jpg" alt="drawing" width="400"/>


Go to `Lab 22. Learning SQLite3`. There you'll find lots of copy/pasteable code for creating/reading/updating/deleting values in a sqlite3 database!

Use the code and adapt it to do the following:

- name your database file `challenge.db`
- create a table inside the file named `thursday`. It should have the following columns:
    - ID (primary key, integer, not null)
    - band (text, not null)
    - hometown (text, not null)
    - year (int, not null)
- insert the following data into those columns:

    ```
    [
      {
        "id": 1,
        "band": "The Beatles",
        "hometown": "Liverpool, England",
        "year": 1960
      },
      {
        "id": 2,
        "band": "Guns and Roses",
        "hometown": "Los Angeles, USA",
        "year": 1985
      },
      {
        "id": 3,
        "band": "Agnee",
        "hometown": "Pune, India",
        "year": 2007
      }
    ]
    ```

- SELECT all the data you created and, using a for loop, print each database row to the screen.

**BONUS**

Read in the sqlite3 database you've created as a Pandas DataFrame! Check out this source on how to do it:

https://datacarpentry.org/python-ecology-lesson/09-working-with-sql/index.html

**SOLUTION**
```
#!/usr/bin/env python3

import sqlite3
from os.path import exists
import pandas as pd

# check if challenge.db is absent at the start of the script
absent= True

if exists("challenge.db"):
    absent= False

conn = sqlite3.connect('challenge.db')

conn.execute('''CREATE TABLE IF NOT EXISTS thursday
 (id        INT  PRIMARY KEY  NOT NULL,
  band      TEXT              NOT NULL,
  hometown  TEXT              NOT NULL,
  year      INT               NOT NULL);''')

# if absent == True, then this data will need to be added
if absent:
    conn.execute("INSERT INTO thursday (id,band,hometown,year) VALUES (1,'The Beatles','Liverpool, England',1960)")
    conn.execute("INSERT INTO thursday (id,band,hometown,year) VALUES (2,'Guns and Roses','Los Angeles, USA',1985)")
    conn.execute("INSERT INTO thursday (id,band,hometown,year) VALUES (3,'Agnee','Pune, India',2007)")
    conn.commit()

cursor = conn.execute("SELECT * from thursday")
for row in cursor:
    print(row)

# BONUS

df = pd.read_sql_query("SELECT * from thursday", conn)

print(df)

conn.close()
```
