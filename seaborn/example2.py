import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://jbencook.s3.amazonaws.com/data/dummy-sales-large.csv")

# Plot the histogram
sns.histplot(df, x="revenue")

plt.show()