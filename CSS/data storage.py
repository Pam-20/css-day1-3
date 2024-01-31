# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:42 2024
@author: Pamela
"""

"""
storing data in python
1. List
2. Dictionaries
3. Data Frames - specific to pandas
"""



fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]
fruit_sizes = {'fruits': fruits, 'sizes': size_nm}
import pandas as pd
df = pd.DataFrame(fruit_sizes)
print(df['fruits'])
print(df['sizes'])
print(df['sizes'].min())
print(df['sizes'].mean())
print(df.describe())
print(df[1:3])
prices = [10.00, 12.50, 16.00, 23.00, 7.00]
df['prices'] = prices
df.drop(columns=["sizes"], inplace=True)