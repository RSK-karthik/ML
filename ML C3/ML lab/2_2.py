from scipy.stats import zscore
import math
import pandas as pd
df=pd.read_csv("emmployees.csv")
# Get the number of rows and columns
nrows, ncolumns = df.shape
print("Number of rows: ", nrows)
print("Number of columns: ", ncolumns)
# Get the data type of each column
print("\nData type of each column: \n", df.dtypes)
# Get the summary statistics of each column
print("\nSummary statistics of each column: \n", df.describe())

# Count the number of missing values in each column
missing_values_count = df.isnull().sum()
print("Number of missing values in each column:\n", missing_values_count)

# Rename a specific column
df = df.rename(columns={'number_courses' : 'Number_of_Courses', 'time_study' : 'Time_Allocated'})
# Verify that the column has been renamed
print("Dataframe after renaming a specific column: \n", df.head())

import numpy as np
# Replace missing values of multiple numeric columns with their respective mean
numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
# Verify that the missing values have been replaced
print("Dataframe after replacing missing values with mean: \n", df.head())

# Get the current column order
current_column_order = df.columns
# Define the desired column order
new_column_order = ['Marks', 'Number_of_Courses', 'Time_Allocated']
# Change the order of columns
df = df[new_column_order]
# Verify that the order of columns has been changed
print("Dataframe with new column order: \n", df.head())