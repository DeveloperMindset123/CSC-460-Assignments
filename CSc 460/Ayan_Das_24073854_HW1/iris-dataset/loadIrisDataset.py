import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('dataset-iris.csv')  # set the path to the iris dataset csv file

# Headers
headers = df.columns.tolist()

# Count of Data Object (Number of Rows)
count_of_data_objects = df.shape[0]

# Count of Data Categories (Unique Classes)
count_of_data_categories = df['class'].nunique()

# Count of Each Category
count_of_each_category = df['class'].value_counts()

# Series Data Types
series_data_types = df.dtypes

# Add new columns
df['Petal Ratio'] = df['petal length'] / df['petal width']
df['Sepal Ratio'] = df['sepal length'] / df['sepal width']

# Save the new DataFrame into a CSV file
df.to_csv('updated_dataset-iris.csv', index=False)

# Get descriptive statistics
descriptive_stats = df.groupby('class').agg(['mean', 'std', 'min', 'max'])

# Printing the information
print("Headers:", headers)  # lists out the column in the dataset
print("\nCount of Data Objects:", count_of_data_objects)
print("\nCount of Data Categories:", count_of_data_categories)
print("\nCount of Each Category:", count_of_each_category)
print("\nSeries Data Types:", series_data_types)
# Print the information
print("\nDescriptive Stats:\n", descriptive_stats)
print("\n Resulting Dataframe:", df.head())
