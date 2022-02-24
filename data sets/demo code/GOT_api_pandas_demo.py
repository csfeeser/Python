#!/usr/bin/env python3
"""API JSON to Pandas Dataframe Demo"""

import requests
import pandas as pd

def main():
    """data conversion from GOT API"""

    # use requests to fetch JSON and convert to Python dictionary
    url= "https://anapioficeandfire.com/api/characters?page=5&pageSize=50"
    r= requests.get(url).json()

    # there are a ZILLION ways to use pandas to manipulate data
    # json_normalize() will "Normalize semi-structured JSON data into a flat table."
    # this is creating a pandas dataframe out of our converted JSON
    df = pd.json_normalize(r)

    # there are 16 columns; let's drop all columns but 3
    df.drop(df.columns.difference(['name','aliases','playedBy']), 1, inplace=True)

    # print off the top 20 lines of the dataframe
    print(df.head(20))

if __name__ == "__main__":
    main()
