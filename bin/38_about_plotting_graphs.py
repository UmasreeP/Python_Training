"""
Seaborn: Plotting Graphs
"""

print("Get data from Iris.csv file")
print("-"*20)
# ---------------

import pandas as pd
iris_data_df = pd.read_csv("Iris.csv")
print(iris_data_df)

print("#"*40, end="\n\n")
###########################

print("Columns in Iris.csv")
print("-"*20)
# ---------------

print(iris_data_df.columns)
# ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm',
#        'Species']

print("#"*40, end="\n\n")
###########################

print("Plotting Violinplot")
print("-"*20)
# ---------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.violinplot(data=iris_data_df, x='Species', y='SepalLengthCm')

plt.show()

print("#"*40, end="\n\n")
###########################


print("Plotting lineplot")
print("-"*20)
# ---------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(data=iris_data_df, x='Species', y='SepalLengthCm')

plt.show()

print("#"*40, end="\n\n")
###########################

print("Plotting scatterplot")
print("-"*20)
# ---------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.scatterplot(data=iris_data_df, x='Species', y='SepalLengthCm')

plt.show()

print("#"*40, end="\n\n")
###########################