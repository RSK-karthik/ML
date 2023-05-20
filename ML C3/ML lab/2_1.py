from scipy.stats import zscore
import math
import pandas as pd
df = pd.read_csv("employees.csv")
column = df["SALARY"]
meanSalary = df["SALARY"].mean()
df.fillna(meanSalary, inplace=True)
# min-max normalization
new_min, new_max = [int(x) for x in input("Enter the new min and new max value for minmax nomralization: ").split()]
min_max_normalized_values = ((column - column.min()) / (column.max() - column.min())) * (new_max - new_min) + new_min
# Z-score normalization
z_score_normalized_values = zscore(list(df["SALARY"]))
# decimal normalization
n = math.ceil(math.log(column.max(), 10))
decimal_normalized_values = column / 10**n
print("\nMin-Max Normalized Values:\n", min_max_normalized_values)
print("\nZ-Score Normalized Values:\n", z_score_normalized_values)
print("\nDecimal Normalized Values:\n", decimal_normalized_values)
# print(column.min(), column.max())
