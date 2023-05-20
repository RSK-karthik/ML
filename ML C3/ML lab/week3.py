import pandas as pd
df=pd.read_csv('employees.csv')
#print(df)
#1
#print(df[df['DEPARTMENT_ID'].isnull()])

#2
#df2 = df.dropna(how='all').dropna(how='all', axis=1)
#print(df2)
#print(df2.loc[:, df2.isnull().any()])

#3
#print(df2[df2.isnull().any(axis=1)])

#4
#print(df.isna().any())

#5
#print(df.isna().sum())

#6
print(df.isna().sum().idxmax())

#7
#print(df.isna().sum().sum())

#8
df.isnull().sum(axis=1)

#9
#print(df2[df2.isnull().any(axis=1)])

#ten
data.apply(lambda x:x is null().sum(),axis=1)

#11
# Count the number of missing values in each row
missing_count = df.isna().sum(axis=1)
# Find the index of the row with the largest number of missing data
max_missing_row_index = missing_count.idxmax()
# Print the row with the largest number of missing data
print(df.loc[max_missing_row_index])

#12
data.dropna(axis=0, inplace=True)