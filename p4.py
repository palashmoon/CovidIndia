import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel('statewise_testing.xlsx')
print ('######### first analysis#####')
print(df.head())

print ('######### Second analysis#####')
print(df.shape)
print ('######### Third analysis#####')
print(df.info())
print ('######### Fourth analysis#####')
print(df.describe())
a=list(df['State'])
b=list(df['Date'])
c=list(df['Total Samples'])
d=list(df['Negetive'])
e=list(df['Positive'])
plt.plot(b,a,"bo")
plt.show()
plt.plot(b,e,"bo")
plt.show()
plt.plot(b,d,"g^")
plt.show()
plt.plot(b,c,"bo")
plt.show()

