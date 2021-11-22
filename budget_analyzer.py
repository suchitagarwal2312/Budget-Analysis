# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:02:08 2021

@author: vasu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("India_budget_2021.csv")
data.head()

#Let’s have a look at all the departments that are covered in this budget:

print(data)

#I can see a NaN value in this dataset, let’s remove the NaN values and continue with the task of financial budget analysis with Python

data.dropna()

#I can see that not all the departments that are covered in this dataset are the main departments, as some departments can be covered in the others category. 
#So let’s prepare the data by only selecting the main departments and putting all the other departments in the other category

data = data.iloc[[0,8,11,14,18,23,41,42,43],:]
row = {'Department /Ministry': 'OTHERS', 'Fund allotted(in ₹crores)': 592971.0800000001}
data = data.append(row, ignore_index = True)
print(data)

#Now let’s plot this data to have a look at the priorities of the government for the financial year:

data.plot.bar(x='Department /Ministry', y='Fund allotted(in ₹crores)')

#We can see that the finance department is getting the most of the share from the total budget of the government. 
#Now let’s plot this data into a donut plot to have a clear view of the distribution of funds among all the departments:


df = data["Fund allotted(in ₹crores)"]
labels = data["Department /Ministry"]
plt.figure(figsize=(7,7))
plt.pie(df, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, shadow =True)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Distribution of The Budget 2021 (Analyzed by Suchit)", fontsize=20)
plt.show()