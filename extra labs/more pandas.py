# pandas dataframes with Excel, csv, json, HTML and beyond

### Lab Objective

The objective of this lab is to learn how to work with datasets commonly encountered by network engineers. Vendors often will supply data in formats such as Excel (xls and xlsx), csv, json, and plain-text. The Python library `pandas` makes it easy to transform data into a common format (dataframes), which can than be exported to whatever format is required. Other reasons for using dataframes include data analysis, plotting and graphing, moving data to machine learning tools (scikit-learn), or possibly moving data across RESTful API interfaces.

The pandas library tools for reading and writing data between in-memory data structures and different formats include Excel, as well as CSV and text files, SQL databases, and the fast HDF5 format.

Read about the Pandas project here:  

https://pandas.pydata.org/

The data types pandas can read and write to can be found here: 
 
https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

### Procedure

0. Open a new terminal

0. Create a new directory to work in.

    `student@beachhead:~$` `mkdir -p ~/pyapi/pandas/`

0. Move into that directory.

    `student@beachhead:~$` `cd ~/pyapi/pandas/`

0. Ensure pandas is installed along with `xlrd`, and `openpyxl`, which are optional dependencies for working with MS Excel.

    `student@beachhead:~/pyapi/pandas$` `python3 -m pip install pandas xlrd openpyxl`

0. Download the Excel data set we'll be using for this lab. The set itself spans 3 sheets, and contains movie data. You may want to download this dataset on your local laptop, and check it out in Excel.

    `student@beachhead:~/pyapi/pandas$` `wget https://static.alta3.com/files/movies.xls`

0. Create a new script, `pandabear01.py`

    `student@beachhead:~/pyapi/pandas$` `vim pandabear01.py`

0. Create the following solution:

    ```python
    #!/usr/bin/python3

    import pandas as pd
    
    def main():
        # define the name of our xls file
        excel_file = 'movies.xls'

        # create a DataFrame (DF) object. EASY!
        # because we did not specify a sheet
        # only the first sheet was read into the DF
        movies = pd.read_excel(excel_file)

        # show the first five rows of our DF
        # DF has 5 rows and 25 columns (indexed by integer)
        print(movies.head())

        # Choose the first column "Title" as
        # index (index=0)
        movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
        # DF has 5 rows and 24 columns (indexed by title)
        print(movies_sheet1.head())

        # grab the next 2 sheets as well
        movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
        # DF has 5 rows and 24 columns (indexed by title)
        print(movies_sheet2.head())

        movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
        # DF has 5 rows and 24 columns (indexed by title)
        print(movies_sheet3.head())

        # combine all DFs into a single DF called movies
        movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

        # number of rows and columns (5042, 24)
        print(movies.shape)

        # sort DataFrame based on Gross Earnings
        sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

        # Data is sorted by values in a column
        # display the top 10 movies by Gross Earnings.
        # passing the 10 values to head returns the top 10 not the default 5
        print(sorted_by_gross.head(10))

    if __name__ == "__main__":
        main()
    ```

0. Save and exit.

0. Run your script.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear01.py`
    
0. Let's try combining multiple data sources, CSV and JSON, into a single data frame, then exporting to a few formats, including Excel. Start by downloading a CSV dataset. 

    `student@beachhead:~/pyapi/pandas$` `wget https://static.alta3.com/files/ciscodata.csv`

0. Now, download a JSON dataset.

    `student@beachhead:~/pyapi/pandas$` `wget https://static.alta3.com/files/ciscodata2.json`

0. Display both datasets. Both have valuable data, but they're in mixed formats. First, display the CSV data.

    `student@beachhead:~/pyapi/pandas$` `cat ciscodata.csv`

0. Display the json.

    `student@beachhead:~/pyapi/pandas$` `cat ciscodata2.json`

0. Great. Now write a script that will take those data sets, and combine them into a single dataframe.

0. Create a new script, `pandabear02.py`

    `student@beachhead:~/pyapi/pandas$` `vim pandabear02.py`

0. Create the following script:

    ```python
    #!/usr/bin/python3
    
    import pandas as pd
    
    def main():
        ciscocsv = pd.read_csv("ciscodata.csv")
        ciscojson = pd.read_json("ciscodata2.json")
        
        # display first 5 entries of the ciscocsv dataframe
        print(ciscocsv.head())

        # display first 5 entries of the ciscojson dataframe            
        print(ciscojson.head())
        
        ciscodf = pd.concat([ciscocsv, ciscojson])
        # uncomment the line below to "fix" the index issue
        # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)
        
        print(ciscodf)
        
    if __name__ == "__main__":
        main()
    ```

0. Save and exit.

0. Execute your code.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear02.py`

0. Before you go any further, study the results. Notice how the indexes are repeated? There is a fix for this, which is described here: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html under, "Ignoring indexes on the concatenation axis".

0. Let's rewrite that script. This time, we'll fix the indexing issue, and export our data a few different ways. To export to Excel, you'll need to install `xlwt` with `pip`. Failure to do so will remind you that you need to install `xlwt`.

    `student@beachhead:~/pyapi/pandas$` `python3 -m pip install xlwt`

0. Create a new script, `pandabear03.py`

    `student@beachhead:~/pyapi/pandas$` `vim pandabear03.py`

0. Write the following script:

    ```python
    #!/usr/bin/python3
    
    import pandas as pd
    
    def main():
        # create a dataframe ciscocsv
        ciscocsv = pd.read_csv("ciscodata.csv")
        # create a dataframe ciscojson
        ciscojson = pd.read_json("ciscodata2.json")

        # The line below concats and reapplies the index value
        ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

        ## print to the screen the re-indexed dataframe
        print(ciscodf)
        
        ## print a blankline
        print()

        ## export to json
        ciscodf.to_json("combined_ciscodata.json")

        ## export to csv
        ciscodf.to_csv("combined_ciscodata.csv")
        
        ## export to Excel
        ciscodf.to_excel("combined_ciscodata.xls")
        
        ## create a python dictionary
        x = ciscodf.to_dict()
        print(x)
        
    if __name__ == "__main__":
        main()
    ```

0. Save and exit.

0. Execute your code.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear03.py`

0. Study the output. First the `combined_ciscodata.json` file.

    `student@beachhead:~/pyapi/pandas$` `cat combined_ciscodata.json`
    
0. Now `combined_ciscodata.csv`

    `student@beachhead:~/pyapi/pandas$` `cat combined_ciscodata.csv`
    
0. Let the XLS file sit for now.

0. There's a few problems. The JSON data that was produced now has the index numbers included in it, as does the CSV data. Let's see if we can write an improved script that fixes this.

0. Create a new script, `pandabear04.py`

    `student@beachhead:~/pyapi/pandas$` `vim pandabear04.py`

0. Write the following script:

    ```python
    #!/usr/bin/python3
    
    import pandas as pd
    
    def main():
        # create a dataframe ciscocsv
        ciscocsv = pd.read_csv("ciscodata.csv")
        # create a dataframe ciscojson
        ciscojson = pd.read_json("ciscodata2.json")

        # The line below concats and reapplies the index value
        ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)
        
        ## export to json
        ## do not include index number
        ciscodf.to_json("combined_ciscodata.json", orient="records")

        ## export to csv
        ## do not include index number
        ciscodf.to_csv("combined_ciscodata.csv", index=False)
        
        ## export to Excel
        ## do not include index number to xls
        ciscodf.to_excel("combined_ciscodata.xls", index=False)
        ## do not include index number to xlsx
        ciscodf.to_excel("combined_ciscodata.xlsx", index=False)
        
        ## create a python dictionary
        ## do not include index number
        x = ciscodf.to_dict(orient='records')
        print(x)
        
    if __name__ == "__main__":
        main()
    ```

0. Save and exit.

0. Execute your code.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear04.py`

0. Study the output which no longer includes the index values. First the `combined_ciscodata.json` file.

    `student@beachhead:~/pyapi/pandas$` `cat combined_ciscodata.json`
    
0. Now `combined_ciscodata.csv` Notice, no more index values.

    `student@beachhead:~/pyapi/pandas$` `cat combined_ciscodata.csv`

0. Download the new dataset, `corporateNetworkLog.csv`. This dataset is a reflection of data useage across a corporate network from 2006 through 2017. The data is arranged, `Date,Consumption,YouTube,Netflix,YouTube+Netflix`. `Date` is given via YYYY-MM-DD. All other values given are in terrabytes. The value `Consumption`, is the sum of total network traffic for a small corporate centre. The values `YouTube` and `Netflix` are the portion of `Consuption` consumed by either service. The value `YouTube+Netflix` is simply the sum of `YouTube` and `Netflix` for that date.

    `student@beachhead:~/pyapi/pandas$` `wget https://static.alta3.com/courses/pyna/netTraffic.csv`

0. Originally developed for financial time series such as daily stock market prices, the robust and flexible data structures in pandas can be applied to time series data in any domain, including business, science, engineering, public health, and many others. With these tools you can easily organize, transform, analyze, and visualize your data at any level of granularity — examining details during specific time periods of interest, and zooming out to explore variations on different time scales, such as monthly or annual aggregations, recurring patterns, and long-term trends... such as how much time employees are spending streaming movies.

    > A time series really could be any data set where the values are measured at different points in time. Many time series are uniformly spaced at a specific frequency, for example, hourly weather measurements, daily counts of web site visits, or cell sites currently up or down. Time series can also be irregularly spaced and sporadic, for example, timestamped data in a computer system’s event log or a history of 911 emergency calls. Pandas time series tools apply equally well to either type of time series.

0. With pandas, we can answer the following questions:
    - **When is network consumption typically highest and lowest?**
    - **How do streaming services vary with seasons of the year?**
    - **What are the long-term trends in network usage, YouTube, and Netflix?**
    - **How do YouTube and Netflix compare with network consumption, and how has this ratio changed over time?**
    
0. To begin, create a new script:

    `student@beachhead:~/pyapi/pandas$` `vim pandabear05.py`

0. Create the following script:

    ```python
    #!/usr/bin/python3
    """Russell Zachary Feeser || Alta3 Research
    In pandas, a single point in time is represented as a Timestamp. We can use the to_datetime() function to create Timestamps from strings in a wide variety of date/time formats. Let’s import pandas and convert a few dates and times to Timestamps.
    """

    import pandas as pd
    
    def main():
        """run-time code"""
        # to_datetime() automatically infers a date/time format based on the input
        # the ambiguous date '7/8/1952' is assumed to be month/day/year and is interpreted as July 8, 1952
        print(pd.to_datetime('2018-01-15 3:45pm'))
        # 2018-01-15 15:45:00

        # Alternatively, we can use the dayfirst parameter to tell pandas to interpret the date as August 7, 1952.
        print(pd.to_datetime('7/8/1952'))
        # 1952-07-08 00:00:00

        print(pd.to_datetime('7/8/1952', dayfirst=True))
        # 1952-08-07 00:00:00

        # Supply a list or array of strings as input to to_datetime() and it
        # returns a sequence of date/time values in a DatetimeIndex object, which is the core data structure that powers much of pandas time series functionality
        print(pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995']))
        # DatetimeIndex(['2018-01-05', '1952-07-08', '1995-10-10'], dtype='datetime64[ns]', freq=None)
        # In the DatetimeIndex above, the data type datetime64[ns] indicates that the underlying data is stored as 64-bit integers, in units of nanoseconds (ns)
        # This data structure allows pandas to compactly store large sequences of date/time values and efficiently perform vectorized operations using NumPy datetime64 arrays.

        # Dealing with a sequence of strings all in the same date/time format, we can explicitly specify it with the format parameter
        # For very large data sets, this can greatly speed up the performance of to_datetime() compared to the default behavior
        # Any of the format codes from the strftime() and strptime() functions in Python’s built-in datetime module can be used.
        print(pd.to_datetime(['2/25/10', '8/6/17', '12/15/12'], format='%m/%d/%y'))
        # DatetimeIndex(['2010-02-25', '2017-08-06', '2012-12-15'], dtype='datetime64[ns]', freq=None)


    if __name__ == "__main__":
        main()
    ```

0. Save and exit with `:wq`

0. Try running your script.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear05.py`

0. Now that we know a bit more about pandas and dates, lets creating a time series DataFrame. To do this, we use the read_csv() function to read the data into a DataFrame.

    `student@beachhead:~/pyapi/pandas$` `vim pandabear06.py`

0. Create the following script that will work with our new dataset.

    ```python
    #!/usr/bin/python3
    """Russell Zachary Feeser | Alta3 Research
    Creating a DataFrame from a timeseries dataset and working with methods to display various network usage.
    """
    
    import pandas

    def main():
        opsd_daily = pd.read_csv('netTraffic.csv') # this opens the csv dataset
        
        opsd_daily.shape
        # (4383, 5)  # our data has 4383 rows covering January 1, 2006 through December 31, 2017
        
        print("\nLook at the first three rows")
        opsd_daily.head(3)
        
        print("\nLook at the last three rows")
        opsd_daily.tail(3)

        # check out the data types of each column
        opsd_daily.dtypes

        # set the date as the DataFrame’s index
        opsd_daily = opsd_daily.set_index('Date')

        print("\nLook at the first three rows after date has been set as the primary index")
        opsd_daily.head(3)
        
        print("\nLook at the last three rows after date has been set as the primary index")
        opsd_daily.tail(3)

        # display all of the index values (this is a lot of data)
        input("\nPress ENTER to look at all of the index values associated with the dataset (dates)")
        opsd_daily.index

        # consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
        opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)
        
        # add some additional columns to our data
        # Add columns with year, month, and weekday name
        opsd_daily['Year'] = opsd_daily.index.year
        opsd_daily['Month'] = opsd_daily.index.month
        # required to 'pull' the day name (ex. Monday, Tuesday, happy days...)
        opsd_daily['Weekday Name'] = opsd_daily.index.day_name()
        
        # display a random sampling of 5 rows
        input("\nPress ENTER to look at a random sampling from 5 rows after adding the Year, Month and Weeday Name columns")
        print(opsd_daily.sample(5, random_state=0))
        

    if __name__ == "__main__":
        main()
    ```

0. Save and exit.

0. Try running your script.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear06.py`

0. Now that we can easily create a pandas DataFrame with an index using DatetimeIndex, we can use all of pandas’ powerful time-based indexing to wrangle and analyze our data. One of the most powerful and convenient features of pandas time series is time-based indexing — using dates and times to intuitively organize and access our data. Create a new script.

    `student@beachhead:~/pyapi/pandas$` `vim pandabear07.py`

0. Create the following script:

    ```python
    #!/usr/bin/python3
    """Russell Zachary Feeser | Alta3 Research
    Learning to work with Time-based indexing in pandas
    """

    import pandas

    def main():
        """run-time code"""
        # consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
        opsd_daily = pandas.read_csv('netTraffic.csv', index_col=0, parse_dates=True)

        # add some additional columns to our data
        # Add columns with year, month, and weekday name
        opsd_daily['Year'] = opsd_daily.index.year
        opsd_daily['Month'] = opsd_daily.index.month
        # required to 'pull' the day name (ex. Monday, Tuesday, happy days...)
        opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

        # select data for a single day using a string such as '2017-08-10'
        input("\nPress ENTER to see the data for 2017-08-10")
        print(opsd_daily.loc['2017-08-10'])

        # select a slice of days, '2014-01-20':'2014-01-22'
        # Note that the slice is inclusive of both endpoints
        input("\nPress ENTER to see the data slice from 2014-01-20 to 2014-01-22")
        print(opsd_daily.loc['2014-01-20':'2014-01-22'])

        # partial-string indexing select all date/times which partially match a given string
        # select the entire year 2006 with opsd_daily.loc['2006']
        # select the entire month of February 2012 with opsd_daily.loc['2012-02']
        input("\nPress ENTER to see the data slice for 2012-02")
        print(opsd_daily.loc['2012-02'])

    if __name__ == "__main__":
        main()
    ```

0. Save and exit

0. Run the new script.

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear07.py`

0. With pandas, and a second library, matplotlib, we can easily visualize our time series data. First, install matplotlib.

    `student@beachhead:~/pyapi/pandas$` `python3 -m pip install matplotlib`

0. Now install seaborn. Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. Read about the project here: https://pypi.org/project/seaborn/

    `student@beachhead:~/pyapi/pandas$` `python3 -m pip install seaborn`

0. Create a new script.

    `student@beachhead:~/pyapi/pandas$` `vim pandabear08.py`

0. Create the following script:

    ```python
    #!/usr/bin/python3
    """Russell Zachary Feeser | Alta3 Research
    Learning to work with Time-based indexing in pandas
    """

    import pandas as pd

    import matplotlib
    matplotlib.use('Agg') # required to generate images without a window appearing

    # does not appear to be necessary
    #import matplotlib.pyplot as plt

    import seaborn as sns

    def main():
        """run-time code"""
        # consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
        opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)

        # add some additional columns to our data
        # Add columns with year, month, and weekday name
        opsd_daily['Year'] = opsd_daily.index.year
        opsd_daily['Month'] = opsd_daily.index.month
        # required to 'pull' the day name (ex. Monday, Tuesday, happy days...)
        opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

        # Use seaborn style defaults and set the default figure size
        sns.set(rc={'figure.figsize':(11, 4)})


        ### LINE PLOT - create a line plot of the full time series of daily network consumption, using the DataFrame’s plot() method.
        netlineplot = opsd_daily['Consumption'].plot(linewidth=0.5)

        # save out this figure
        fig = netlineplot.get_figure()
        fig.savefig("/home/student/static/linePlot.png")



        ### DOT PLOT - plot the data as dots instead, and also look at the YouTube and Netflix time series
        cols_plot = ['Consumption', 'YouTube', 'Netflix']
        axes = opsd_daily[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)

        for ax in axes:
            ax.set_ylabel('Daily Totals (TBs)')
            
            # save out this figure
            fig = ax.get_figure()
            fig.savefig(f"/home/student/static/dotPlot.png")

    if __name__ == "__main__":
        main()
    ```

0. Save and exit.

0. Try running your code:

    `student@beachhead:~/pyapi/pandas$` `python3 pandabear08.py`

0. The graphs were saved out to the `~/static/` folder. Files in this folder can be viewed by clicking on the icon that is 3-sheets of paper in the upper right hand corner, and then selecting your instance of `nginx`. By using this method, you should see two files, `linePlot.png` and `dotPlot.png`. Try interacting (clicking) on both.

0. Looks like some interesting patterns are emerging! The data suggests that there may be some seasonality, and weekly changes in network consumption corresponding with weekdays and weekends.




<!--

0.  Let’s plot the time series in a single year to investigate further. Create a new script:

0. Create the following script:

    ```python
    #!/usr/bin/python3
    """Russell Zachary Feeser | Alta3 Research
    Learning to work with Time-based indexing in pandas
    """
ax = opsd_daily.loc['2017', 'Consumption'].plot()
ax.set_ylabel('Daily Consumption (GWh)');
time-series-pandas_40_0.png
Now we can clearly see the weekly oscillations. Another interesting feature that becomes apparent at this level of granularity is the drastic decrease in electricity consumption in early January and late December, during the holidays.

Let’s zoom in further and look at just January and February.

ax = opsd_daily.loc['2017-01':'2017-02', 'Consumption'].plot(marker='o', linestyle='-')
ax.set_ylabel('Daily Consumption (GWh)');
time-series-pandas_42_0.png
As we suspected, consumption is highest on weekdays and lowest on weekends.

Customizing time series plots
To better visualize the weekly seasonality in electricity consumption in the plot above, it would be nice to have vertical gridlines on a weekly time scale (instead of on the first day of each month). We can customize our plot with matplotlib.dates, so let’s import that module.

import matplotlib.dates as mdates
Because date/time ticks are handled a bit differently in matplotlib.dates compared with the DataFrame’s plot() method, let’s create the plot directly in matplotlib. Then we use mdates.WeekdayLocator() and mdates.MONDAY to set the x-axis ticks to the first Monday of each week. We also use mdates.DateFormatter() to improve the formatting of the tick labels, using the format codes we saw earlier.

fig, ax = plt.subplots()
ax.plot(opsd_daily.loc['2017-01':'2017-02', 'Consumption'], marker='o', linestyle='-')
ax.set_ylabel('Daily Consumption (GWh)')
ax.set_title('Jan-Feb 2017 Electricity Consumption')
# Set x-axis major ticks to weekly interval, on Mondays
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MONDAY))
# Format x-tick labels as 3-letter month name and day number
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'));
time-series-pandas_46_0.png
Now we have vertical gridlines and nicely formatted tick labels on each Monday, so we can easily tell which days are weekdays and weekends.

There are many other ways to visualize time series, depending on what patterns you’re trying to explore — scatter plots, heatmaps, histograms, and so on. We’ll see other visualization examples in the following sections, including visualizations of time series data that has been transformed in some way, such as aggregated or smoothed data.

Seasonality
Next, let’s further explore the seasonality of our data with box plots, using seaborn’s boxplot() function to group the data by different time periods and display the distributions for each group. We’ll first group the data by month, to visualize yearly seasonality.

fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
sns.boxplot(data=opsd_daily, x='Month', y=name, ax=ax)
ax.set_ylabel('GWh')
ax.set_title(name)
# Remove the automatic x-axis label from all but the bottom subplot
if ax != axes[-1]:
    ax.set_xlabel('')
time-series-pandas_48_0.png
These box plots confirm the yearly seasonality that we saw in earlier plots and provide some additional insights:
* Although electricity consumption is generally higher in winter and lower in summer, the median and lower two quartiles are lower in December and January compared to November and February, likely due to businesses being closed over the holidays. We saw this in the time series for the year 2017, and the box plot confirms that this is consistent pattern throughout the years.
* While solar and wind power production both exhibit a yearly seasonality, the wind power distributions have many more outliers, reflecting the effects of occasional extreme wind speeds associated with storms and other transient weather conditions.

Next, let’s group the electricity consumption time series by day of the week, to explore weekly seasonality.

sns.boxplot(data=opsd_daily, x='Weekday Name', y='Consumption');
time-series-pandas_50_0.png
As expected, electricity consumption is significantly higher on weekdays than on weekends. The low outliers on weekdays are presumably during holidays.

This section has provided a brief introduction to time series seasonality. As we will see later, applying a rolling window to the data can also help to visualize seasonality on different time scales. Other techniques for analyzing seasonality include autocorrelation plots, which plot the correlation coefficients of the time series with itself at different time lags.

Time series with strong seasonality can often be well represented with models that decompose the signal into seasonality and a long-term trend, and these models can be used to forecast future values of the time series. A simple example of such a model is classical seasonal decomposition, as demonstrated in this tutorial. A more sophisticated example is as Facebook’s Prophet model, which uses curve fitting to decompose the time series, taking into account seasonality on multiple time scales, holiday effects, abrupt changepoints, and long-term trends, as demonstrated in this tutorial.

Frequencies
When the data points of a time series are uniformly spaced in time (e.g., hourly, daily, monthly, etc.), the time series can be associated with a frequency in pandas. For example, let’s use the date_range() function to create a sequence of uniformly spaced dates from 1998-03-10 through 1998-03-15 at daily frequency.

pd.date_range('1998-03-10', '1998-03-15', freq='D')
DatetimeIndex(['1998-03-10', '1998-03-11', '1998-03-12', '1998-03-13',
'1998-03-14', '1998-03-15'],
dtype='datetime64[ns]', freq='D')
The resulting DatetimeIndex has an attribute freq with a value of 'D', indicating daily frequency. Available frequencies in pandas include hourly ('H'), calendar daily ('D'), business daily ('B'), weekly ('W'), monthly ('M'), quarterly ('Q'), annual ('A'), and many others. Frequencies can also be specified as multiples of any of the base frequencies, for example '5D' for every five days.

As another example, let’s create a date range at hourly frequency, specifying the start date and number of periods, instead of the start date and end date.

pd.date_range('2004-09-20', periods=8, freq='H')
DatetimeIndex(['2004-09-20 00:00:00', '2004-09-20 01:00:00',
'2004-09-20 02:00:00', '2004-09-20 03:00:00',
'2004-09-20 04:00:00', '2004-09-20 05:00:00',
'2004-09-20 06:00:00', '2004-09-20 07:00:00'],
dtype='datetime64[ns]', freq='H')
Now let’s take another look at the DatetimeIndex of our opsd_daily time series.

opsd_daily.index
DatetimeIndex(['2006-01-01', '2006-01-02', '2006-01-03', '2006-01-04',
'2006-01-05', '2006-01-06', '2006-01-07', '2006-01-08',
'2006-01-09', '2006-01-10',
...
'2017-12-22', '2017-12-23', '2017-12-24', '2017-12-25',
'2017-12-26', '2017-12-27', '2017-12-28', '2017-12-29',
'2017-12-30', '2017-12-31'],
dtype='datetime64[ns]', name='Date', length=4383, freq=None)
We can see that it has no frequency (freq=None). This makes sense, since the index was created from a sequence of dates in our CSV file, without explicitly specifying any frequency for the time series.

If we know that our data should be at a specific frequency, we can use the DataFrame’s asfreq() method to assign a frequency. If any date/times are missing in the data, new rows will be added for those date/times, which are either empty (NaN), or filled according to a specified data filling method such as forward filling or interpolation.

To see how this works, let’s create a new DataFrame which contains only the Consumption data for Feb 3, 6, and 8, 2013.

# To select an arbitrary sequence of date/time values from a pandas time series,
# we need to use a DatetimeIndex, rather than simply a list of date/time strings
times_sample = pd.to_datetime(['2013-02-03', '2013-02-06', '2013-02-08'])
# Select the specified dates and just the Consumption column
consum_sample = opsd_daily.loc[times_sample, ['Consumption']].copy()
consum_sample
Consumption
2013-02-03	1109.639
2013-02-06	1451.449
2013-02-08	1433.098
Now we use the asfreq() method to convert the DataFrame to daily frequency, with a column for unfilled data, and a column for forward filled data.

# Convert the data to daily frequency, without filling any missings
consum_freq = consum_sample.asfreq('D')
# Create a column with missings forward filled
consum_freq['Consumption - Forward Fill'] = consum_sample.asfreq('D', method='ffill')
consum_freq
Consumption	Consumption – Forward Fill
2013-02-03	1109.639	1109.639
2013-02-04	NaN	1109.639
2013-02-05	NaN	1109.639
2013-02-06	1451.449	1451.449
2013-02-07	NaN	1451.449
2013-02-08	1433.098	1433.098
In the Consumption column, we have the original data, with a value of NaN for any date that was missing in our consum_sample DataFrame. In the Consumption - Forward Fill column, the missings have been forward filled, meaning that the last value repeats through the missing rows until the next non-missing value occurs.

If you’re doing any time series analysis which requires uniformly spaced data without any missings, you’ll want to use asfreq() to convert your time series to the specified frequency and fill any missings with an appropriate method.

Resampling
It is often useful to resample our time series data to a lower or higher frequency. Resampling to a lower frequency (downsampling) usually involves an aggregation operation — for example, computing monthly sales totals from daily data. The daily OPSD data we’re working with in this tutorial was downsampled from the original hourly time series. Resampling to a higher frequency (upsampling) is less common and often involves interpolation or other data filling method — for example, interpolating hourly weather data to 10 minute intervals for input to a scientific model.

We will focus here on downsampling, exploring how it can help us analyze our OPSD data on various time scales. We use the DataFrame’s resample() method, which splits the DatetimeIndex into time bins and groups the data by time bin. The resample() method returns a Resampler object, similar to a pandas GroupBy object. We can then apply an aggregation method such as mean(), median(), sum(), etc., to the data group for each time bin.

For example, let’s resample the data to a weekly mean time series.

# Specify the data columns we want to include (i.e. exclude Year, Month, Weekday Name)
data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
# Resample to weekly frequency, aggregating with mean
opsd_weekly_mean = opsd_daily[data_columns].resample('W').mean()
opsd_weekly_mean.head(3)
Consumption	Wind	Solar	Wind+Solar
Date				
2006-01-01	1069.184000	NaN	NaN	NaN
2006-01-08	1381.300143	NaN	NaN	NaN
2006-01-15	1486.730286	NaN	NaN	NaN
The first row above, labelled 2006-01-01, contains the mean of all the data contained in the time bin 2006-01-01 through 2006-01-07. The second row, labelled 2006-01-08, contains the mean data for the 2006-01-08 through 2006-01-14 time bin, and so on. By default, each row of the downsampled time series is labelled with the right edge of the time bin.

By construction, our weekly time series has 1/7 as many data points as the daily time series. We can confirm this by comparing the number of rows of the two DataFrames.

print(opsd_daily.shape[0])
print(opsd_weekly_mean.shape[0])
4383
627
Let’s plot the daily and weekly Solar time series together over a single six-month period to compare them.

# Start and end of the date range to extract
start, end = '2017-01', '2017-06'
# Plot daily and weekly resampled time series together
fig, ax = plt.subplots()
ax.plot(opsd_daily.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.set_ylabel('Solar Production (GWh)')
ax.legend();
time-series-pandas_66_0.png
We can see that the weekly mean time series is smoother than the daily time series because higher frequency variability has been averaged out in the resampling.

Now let’s resample the data to monthly frequency, aggregating with sum totals instead of the mean. Unlike aggregating with mean(), which sets the output to NaN for any period with all missing data, the default behavior of sum() will return output of 0 as the sum of missing data. We use the min_count parameter to change this behavior.

# Compute the monthly sums, setting the value to NaN for any month which has
# fewer than 28 days of data
opsd_monthly = opsd_daily[data_columns].resample('M').sum(min_count=28)
opsd_monthly.head(3)
Consumption	Wind	Solar	Wind+Solar
Date				
2006-01-31	45304.704	NaN	NaN	NaN
2006-02-28	41078.993	NaN	NaN	NaN
2006-03-31	43978.124	NaN	NaN	NaN
You might notice that the monthly resampled data is labelled with the end of each month (the right bin edge), whereas the weekly resampled data is labelled with the left bin edge. By default, resampled data is labelled with the right bin edge for monthly, quarterly, and annual frequencies, and with the left bin edge for all other frequencies. This behavior and various other options can be adjusted using the parameters listed in the resample() documentation.

Now let’s explore the monthly time series by plotting the electricity consumption as a line plot, and the wind and solar power production together as a stacked area plot.

fig, ax = plt.subplots()
ax.plot(opsd_monthly['Consumption'], color='black', label='Consumption')
opsd_monthly[['Wind', 'Solar']].plot.area(ax=ax, linewidth=0)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_ylabel('Monthly Total (GWh)');
time-series-pandas_70_0.png
At this monthly time scale, we can clearly see the yearly seasonality in each time series, and it is also evident that electricity consumption has been fairly stable over time, while wind power production has been growing steadily, with wind + solar power comprising an increasing share of the electricity consumed.

Let’s explore this further by resampling to annual frequency and computing the ratio of Wind+Solar to Consumption for each year.

# Compute the annual sums, setting the value to NaN for any year which has
# fewer than 360 days of data
opsd_annual = opsd_daily[data_columns].resample('A').sum(min_count=360)
# The default index of the resampled DataFrame is the last day of each year,
# ('2006-12-31', '2007-12-31', etc.) so to make life easier, set the index
# to the year component
opsd_annual = opsd_annual.set_index(opsd_annual.index.year)
opsd_annual.index.name = 'Year'
# Compute the ratio of Wind+Solar to Consumption
opsd_annual['Wind+Solar/Consumption'] = opsd_annual['Wind+Solar'] / opsd_annual['Consumption']
opsd_annual.tail(3)
Consumption	Wind	Solar	Wind+Solar	Wind+Solar/Consumption
Year					
2015	505264.56300	77468.994	34907.138	112376.132	0.222410
2016	505927.35400	77008.126	34562.824	111570.950	0.220528
2017	504736.36939	102667.365	35882.643	138550.008	0.274500
Finally, let’s plot the wind + solar share of annual electricity consumption as a bar chart.

# Plot from 2012 onwards, because there is no solar production data in earlier years
ax = opsd_annual.loc[2012:, 'Wind+Solar/Consumption'].plot.bar(color='C0')
ax.set_ylabel('Fraction')
ax.set_ylim(0, 0.3)
ax.set_title('Wind + Solar Share of Annual Electricity Consumption')
plt.xticks(rotation=0);
time-series-pandas_74_0.png
We can see that wind + solar production as a share of annual electricity consumption has been increasing from about 15% in 2012 to about 27% in 2017.

Rolling windows
Rolling window operations are another important transformation for time series data. Similar to downsampling, rolling windows split the data into time windows and and the data in each window is aggregated with a function such as mean(), median(), sum(), etc. However, unlike downsampling, where the time bins do not overlap and the output is at a lower frequency than the input, rolling windows overlap and “roll” along at the same frequency as the data, so the transformed time series is at the same frequency as the original time series.

By default, all data points within a window are equally weighted in the aggregation, but this can be changed by specifying window types such as Gaussian, triangular, and others. We’ll stick with the standard equally weighted window here.

Let’s use the rolling() method to compute the 7-day rolling mean of our daily data. We use the center=True argument to label each window at its midpoint, so the rolling windows are:

2006-01-01 to 2006-01-07 — labelled as 2006-01-04
2006-01-02 to 2006-01-08 — labelled as 2006-01-05
2006-01-03 to 2006-01-09 — labelled as 2006-01-06
and so on…
# Compute the centered 7-day rolling mean
opsd_7d = opsd_daily[data_columns].rolling(7, center=True).mean()
opsd_7d.head(10)
Consumption	Wind	Solar	Wind+Solar
Date				
2006-01-01	NaN	NaN	NaN	NaN
2006-01-02	NaN	NaN	NaN	NaN
2006-01-03	NaN	NaN	NaN	NaN
2006-01-04	1361.471429	NaN	NaN	NaN
2006-01-05	1381.300143	NaN	NaN	NaN
2006-01-06	1402.557571	NaN	NaN	NaN
2006-01-07	1421.754429	NaN	NaN	NaN
2006-01-08	1438.891429	NaN	NaN	NaN
2006-01-09	1449.769857	NaN	NaN	NaN
2006-01-10	1469.994857	NaN	NaN	NaN
We can see that the first non-missing rolling mean value is on 2006-01-04, because this is the midpoint of the first rolling window.

To visualize the differences between rolling mean and resampling, let’s update our earlier plot of January-June 2017 solar power production to include the 7-day rolling mean along with the weekly mean resampled time series and the original daily data.

# Start and end of the date range to extract
start, end = '2017-01', '2017-06'
# Plot daily, weekly resampled, and 7-day rolling mean time series together
fig, ax = plt.subplots()
ax.plot(opsd_daily.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.plot(opsd_7d.loc[start:end, 'Solar'],
marker='.', linestyle='-', label='7-d Rolling Mean')
ax.set_ylabel('Solar Production (GWh)')
ax.legend();
time-series-pandas_78_0.png
We can see that data points in the rolling mean time series have the same spacing as the daily data, but the curve is smoother because higher frequency variability has been averaged out. In the rolling mean time series, the peaks and troughs tend to align closely with the peaks and troughs of the daily time series. In contrast, the peaks and troughs in the weekly resampled time series are less closely aligned with the daily time series, since the resampled time series is at a coarser granularity.

Trends
Time series data often exhibit some slow, gradual variability in addition to higher frequency variability such as seasonality and noise. An easy way to visualize these trends is with rolling means at different time scales.

A rolling mean tends to smooth a time series by averaging out variations at frequencies much higher than the window size and averaging out any seasonality on a time scale equal to the window size. This allows lower-frequency variations in the data to be explored. Since our electricity consumption time series has weekly and yearly seasonality, let’s look at rolling means on those two time scales.

We’ve already computed 7-day rolling means, so now let’s compute the 365-day rolling mean of our OPSD data.

# The min_periods=360 argument accounts for a few isolated missing days in the
# wind and solar production time series
opsd_365d = opsd_daily[data_columns].rolling(window=365, center=True, min_periods=360).mean()
Let’s plot the 7-day and 365-day rolling mean electricity consumption, along with the daily time series.

# Plot daily, 7-day rolling mean, and 365-day rolling mean time series
fig, ax = plt.subplots()
ax.plot(opsd_daily['Consumption'], marker='.', markersize=2, color='0.6',
linestyle='None', label='Daily')
ax.plot(opsd_7d['Consumption'], linewidth=2, label='7-d Rolling Mean')
ax.plot(opsd_365d['Consumption'], color='0.2', linewidth=3,
label='Trend (365-d Rolling Mean)')
# Set x-ticks to yearly interval and add legend and labels
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Consumption (GWh)')
ax.set_title('Trends in Electricity Consumption');
time-series-pandas_82_0.png
We can see that the 7-day rolling mean has smoothed out all the weekly seasonality, while preserving the yearly seasonality. The 7-day rolling mean reveals that while electricity consumption is typically higher in winter and lower in summer, there is a dramatic decrease for a few weeks every winter at the end of December and beginning of January, during the holidays.

Looking at the 365-day rolling mean time series, we can see that the long-term trend in electricity consumption is pretty flat, with a couple of periods of anomalously low consumption around 2009 and 2012-2013.

Now let’s look at trends in wind and solar production.

# Plot 365-day rolling mean time series of wind and solar power
fig, ax = plt.subplots()
for nm in ['Wind', 'Solar', 'Wind+Solar']:
    ax.plot(opsd_365d[nm], label=nm)
    # Set x-ticks to yearly interval, adjust y-axis limits, add legend and labels
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.set_ylim(0, 400)
    ax.legend()
    ax.set_ylabel('Production (GWh)')
    ax.set_title('Trends in Electricity Production (365-d Rolling Means)');
time-series-pandas_84_0.png
We can see a small increasing trend in solar power production and a large increasing trend in wind power production, as Germany continues to expand its capacity in those sectors.

Summary and further reading
We’ve learned how to wrangle, analyze, and visualize our time series data in pandas using techniques such as time-based indexing, resampling, and rolling windows. Applying these techniques to our OPSD data set, we’ve gained insights on seasonality, trends, and other interesting features of electricity consumption and production in Germany.

Other potentially useful topics we haven’t covered include time zone handling and time shifts. If you’d like to learn more about working with time series data in pandas, you can check out this section of the Python Data Science Handbook, this blog post, and of course the official documentation. If you’re interested in forecasting and machine learning with time series data, we’ll be covering those topics in a future blog post, so stay tuned!

-->

0. If you're tracking your code in GitHub, issue the following commands:
    - `cd ~/pyapi`
    - `git add *`
    - `git commit -m "working with pandas"`
    - `git push origin master`
