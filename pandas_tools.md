## Pandas Tools SO FAR:

| Code                                  | Description                                                     |
|---------------------------------------|-----------------------------------------------------------------|
| `pd.read_excel(FILENAME, sheet_name=0, index_col=0)`     | Reads an Excel file into a pandas DataFrame, specifying the sheet and index column. |
| `pd.concat([DF1, DF2], ignore_index=True, sort=False)` | Concatenates multiple DataFrames vertically, ignoring the original indices. |
| `df.head()`                            | Displays the first few rows of the DataFrame.                   |
| `df.shape`                             | Returns the dimensions (number of rows and columns) of the DataFrame. |
| `df.to_excel("filename.xlsx")`          | Writes the DataFrame to an Excel file.                           |
| `df.to_json("filename.json")`           | Writes the DataFrame to a JSON file.                             |
| `df.to_csv("filename.csv")`             | Writes the DataFrame to a CSV file.                              |
| `df.drop_duplicates(inplace=True)`      | Removes duplicate rows from the DataFrame in-place.              |
| `df.sort_values(["Gross Earnings"], ascending=False)` | Sorts the DataFrame by the 'Gross Earnings' column in descending order. |
| `df[[COLUMN1, COLUMN2]].sum()`          | Calculates the sum of values in specific columns of the DataFrame. |
| `df.groupby("COLUMN").sum()`            | Groups the DataFrame by a specific column and calculates the sum for each group. |
