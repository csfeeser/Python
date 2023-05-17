## Warming up with PANDAS!

<img src="https://miro.medium.com/max/1400/1*Q55X1gfHjKi1knx96UVdZQ.png" alt="drawing" width="200"/>

- Start by creating a new directory for yourself in ~/mycode. You can name it whatever you want, but if you're not sure try this:

    `mkdir -p ~/mycode/challenge`

- `cd` into your directory.

    `cd ~/mycode/challenge`

- Download a CSV file with some fun data!

    `wget https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/annualcheeseconsumed.txt`

### NOTE: if you want to be extra fancy with the solutions you make, use markdown cells to indicate which part of your code solves each part!
#### Part 1

This data contained the average pounds of cheese consumed per American from 1970 to 2017!

-  Create a dataframe from this data!

    <details>
    <summary>HINT</summary>

    ```python
    df = pd.read_csv('annualcheeseconsumed.txt')
    ```

    </summary>

#### Part 2

- Set the index to be the YEAR!
    
    <details>
    <summary>HINT</summary>

    ```python
    df.set_index('Year', inplace=True)
    ```

    </summary>

#### Part 3

- Reduce the number of columns to just the YEAR and cheddar, swiss, and muenster.

    <details>
    <summary>HINT</summary>

    ```python
    df = df[['Cheddar', 'Swiss', 'Muenster']]
    ```

    </summary>

#### Part 4

- Sort the data so that the dates go from MOST recent to LEAST recent.

    <details>
    <summary>HINT</summary>

    ```python    
    df = df.sort_index(ascending=False)
    ```

    </summary>

#### Part 5

- What is the MEAN of all the **cheddar** consumed across all the years in this dataframe?

    <details>
    <summary>HINT</summary>

    ```python
    mean_cheddar = df.loc['Cheddar'].mean()
    print(f"Average cheddar consumed from 1970 to 2017: {mean_cheddar} pounds")
    ```

    </summary>


