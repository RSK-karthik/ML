import pandas as pd
data = pd.read_csv('ODI_all_round.csv')
print(data)
data.fillna(0,inplace=True)
print(data)
x=list(data['bwa'])
maxval=max(x)
maxnorm=[]
from math import sqrt
x=list(data['bwa'])
maxval=max(x)
maxnorm=[]
l1norm=[]
l2norm=[]
s=sum(x)
sq=0
for i in x:
 maxnorm.append(i/maxval)
 l1norm.append(i/s)
 sq+=i*i
for i in x:
 l2norm.append(i/sqrt(sq))
print(maxnorm)
data['maxNorm_bwa']=maxnorm
data['l1Norm_bwa']=l1norm
data['l2Norm_bwa']=l2norm
print(data)