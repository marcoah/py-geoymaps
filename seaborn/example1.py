import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set()

np.random.seed(33)
normal_data_a = np.random.normal(size = 500, loc = 100, scale = 10)
normal_data_b = np.random.normal(size = 700, loc = 75, scale = 5)

df_normal_a = pd.DataFrame(data = normal_data_a, columns=['score']).assign(group = 'A')
df_normal_b = pd.DataFrame(data = normal_data_b, columns=['score']).assign(group = 'B')

score_data = pd.concat([df_normal_a, df_normal_b], ignore_index=True)

print(score_data)

sns.histplot(data=score_data, x='score')

plt.show()