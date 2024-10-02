"""
=========================
TITLE
=========================

DESC
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic)

titanic_mean = titanic["Age"].mean()

print(titanic_mean)