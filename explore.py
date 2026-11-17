# Reflection Questions
# 1. A Boolean filter is a method of selecting data using logic only if certain conditions are met. 
# 2. The single bracket revenue extracts a column as a pandas series object, while the double brackets extract as a pandas DataFrame object
# 3. Pandas can be scaled to a much larger degree than Excel, either that or pandas can be used to make repeatable scripts

#---Exercise 1---
import pandas as pd; df = pd.read_csv('data/retail_sales.csv')

print.head()
print.shape()
print.columns.tolist()
print.dtypes

#---Exercise 2---
south = df[df['region'] == 'South']

print(len(south))
print((south.head))

#---Exercise 3---
df.sort_values('revenue', ascending=False).head(5)
print(sort.values)

#---Exercise 4---
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())

#---Exercise 5---
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

#---Exercise 6---
print(df['region'].unique())
print(df['region'].value_counts())

#---Exercise 7---
df_subset = df[['region', 'product', 'revenue']]
print(df_subset.shape)

#---Exercise 8---
df.to_csv('data/explored.csv', index=False)
