import pandas as pd

def convert_currency(value):
    if 'M' in value:
        return float(value.replace('M', '').replace('$', '')) * 1e6
    elif 'K' in value:
        return float(value.replace('K', '').replace('$', '')) * 1e3
    else:
        return float(value.replace('$', ''))

# Load the data from the JSON file
df = pd.read_json('movies.json')

# Clean and convert data to appropriate formats
df['weekendGross'] = df['weekendGross'].apply(convert_currency)
df['totalGross'] = df['totalGross'].apply(convert_currency)
df['weeksReleased'] = df['weeksReleased'].astype(int)
df['rating'] = df['rating'].str.extract('(\d+\.\d+|\d+)').astype(float)

# Perform descriptive summary on the numerical series
print("Descriptive Summary:")
print(df.describe())

# Filter out the titles with total gross greater than $40M
highGrossingMoviesDf = df[df['totalGross'] > 40000000]
print("\nTitles with Total Gross greater than $40M:")
print(highGrossingMoviesDf[['title']])


