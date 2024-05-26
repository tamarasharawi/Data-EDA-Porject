import requests
import pandas as pd

# Use the correct raw GitHub URL
download_url = "https://raw.githubusercontent.com/light-and-salt/World-Bank-Data-by-Indicators/master/education/education-raw-2021.csv"

target_csv_path = "education-raw-2021.csv"

response = requests.get(download_url)
response.raise_for_status()  # Check that the request was successful

with open(target_csv_path, "wb") as f:
    f.write(response.content)

df = pd.read_csv(target_csv_path, on_bad_lines='skip' , skiprows=3)
pd.set_option("display.max_columns", None) 
#check coulnm 
print(df.columns)

print(df.info())

n = 31758  # Starting row (Python zero-indexed, for pandas read_csv, it's treated as 1-indexed here)
m = 31760 # Ending row, inclusive

# Calculate the rows to skip
skip = list(range(1, n))  # Skip rows from the start up to n-1, adjusting for pandas' 1-indexing in this context

# Calculate the number of rows to read
num_rows = m - n + 1

# Read the specific rows
df_specific_rows = pd.read_csv(target_csv_path, skiprows=skip, nrows=num_rows)

#print(df_specific_rows)

copyDF = df_specific_rows.copy()  

print(copyDF.info())