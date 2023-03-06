# IMPORTING ----------------------------------------
import pandas as pd

# Reading CSV file
df = pd.read_csv('filename.csv')

# Reading Excel file
df = pd.read_excel('filename.xlsx')


# DATA INSPECTION ----------------------------------------
# Check first few rows of the data
df.head()

# Check last few rows of the data
df.tail()

# Check the data types of each column
df.dtypes

# Check the shape of the dataframe
df.shape

# Check the basic statistics of the dataframe
df.describe()


# DATA CLEANING ----------------------------------------
# Drop columns
df.drop('column_name', axis=1, inplace=True)

# Drop rows with NaN values
df.dropna(inplace=True)

# Fill NaN values with 0
df.fillna(0, inplace=True)

# Renaming columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Replacing values in a column
df['column_name'].replace('old_value', 'new_value', inplace=True)

# Removing duplicate rows
df.drop_duplicates(inplace=True)


# DATA MANIPULATION ----------------------------------------
# Selecting a single column
df['column_name']

# Selecting multiple columns
df[['column1', 'column2']]

# Filtering rows based on condition
df[df['column_name'] > 10]

# Sorting data
df.sort_values('column_name', ascending=False, inplace=True)

# Aggregating data
df.groupby('column_name').sum()


# DATA VISUALIZATION ----------------------------------------
import matplotlib.pyplot as plt

# Line plot
plt.plot(df['column_name'])

# Bar plot
plt.bar(df['column_name'])

# Scatter plot
plt.scatter(df['column1'], df['column2'])