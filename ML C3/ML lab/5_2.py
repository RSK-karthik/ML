import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('employees.csv')
hot_encoded_data = pd.get_dummies(df,columns=['JOB_ID'])
print(hot_encoded_data)