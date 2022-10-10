import pandas as pd

df = pd.read_csv('./data/data.csv')

print(df)

# Below are quick example
# Using DataFrame.mean() method to get column average
df2 = df["Pulse"].mean()
print(df2)

# Using DataFrame.mean() to get entire column mean
df2 = df.mean()
print(df2)

# Using multiple columns mean using DataFrame.mean()
df2 = df[["Pulse","Calories"]].mean()
print(df2)

# Average of each column using DataFrame.mean()
df2 = df.mean(axis=0)
print(df2)

# Find the mean including NaN values using DataFrame.mean()
df2 = df.mean(axis = 0, skipna = False)
print(df2)

# Using DataFrame.describe() method
df2 = df.describe()
print(df2)