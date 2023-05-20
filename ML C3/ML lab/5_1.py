import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('employees.csv')
imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer = imputer.fit(df[['SALARY']])
df['SALARY'] = imputer.transform(df[['SALARY']])
print(df)
print()

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('employees.csv')
imputer = SimpleImputer(strategy='median', missing_values=np.nan)
imputer = imputer.fit(df[['SALARY']])
df['SALARY'] = imputer.transform(df[['SALARY']])
print(df)
print()

imputer = SimpleImputer(strategy='median', missing_values=np.nan)
imputer = imputer.fit(df[['SALARY']])
df['SALARY'] = imputer.transform(df[['SALARY']])
print(df)
print()

imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
imputer = imputer.fit(df[['SALARY']])
df['SALARY'] = imputer.transform(df[['SALARY']])
print(df)
print()

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('employees.csv')
imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
imputer = imputer.fit(df[['SALARY']])
df['SALARY'] = imputer.transform(df[['SALARY']])
print(df)
print()
