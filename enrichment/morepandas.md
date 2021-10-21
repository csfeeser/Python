## Additional Pandas Exercise

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html

1. Be sure to have the necessary modules installed:

    `student@bchd:$` `python3 -m pip install pandas xlrd openpyxl`
    
0. Let's grab a truly TREMENDOUS chunk of data- all flights in the United States over the course of seven days. Download that .csv file now!

    `student@bchd:$` `wget https://static.alta3.com/files/airline_flights.csv`
    
0. This dataset is too large to work with alone, but we can use code to answer some questions. Create a new script, `pandaflight.py`

    `student@bchd:$` `vim pandaflight.py`
    
    ```python
    #!/usr/bin/python3

    import pandas as pd

    def main():
        flightcsv = pd.read_csv("airline_flights.csv")

        # organize data by origin and destination airport
        flightcsv_tofrom = flightcsv.groupby(['ORG_AIR', 'DEST_AIR']).size()
        print("Number of flights from original airport to destination airport:")
        print(flightcsv_tofrom)

        # Display the number of flights between Huston (IAH)
        # and Atlanta (ATL) in both directions
        print("\nFlight from ATL to IAH and IAH to ATL")
        print(flightcsv_tofrom.loc[[("ATL", "IAH"), ("IAH", "ATL")]])

    if __name__ == "__main__":
        main()
    ```
