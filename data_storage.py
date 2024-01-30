# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:35 2024

@author: DeogratiusM
"""
"""
sroring data in python

1. Lists
2. Dictionaries
3. Data Frames
"""
import pandas as pd


file = pd.read_csv("country_data.csv")

print(file)

"""
Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""
age = [30,25,29,46,22]
print(age)
"""
[30, 25, 29, 46, 22]
"""
print(age[0])
"""
30
"""

print(age[1])
"""
25
"""
print(min(age))
"""
22
"""
print(max(age))
"""
46
"""
print(len(age))
"""
5
"""
print(sum(age))

"""
152
"""

avg = sum(age)/len(age)

print(avg)

"""
30.4
"""

age.append(100)

print(age)

age.insert(0,100)

"""
[30, 25, 29, 46, 22, 100]
"""

print(age[0:3])
"""
[30, 25, 29]
"""
print(age[:-1])

"""
[30, 25, 29, 46, 22]

"""

#################################################################

"""
Dictionaries - key:value pairs
cat: "a cute animal"

"""

mammals = {"cat":"a cute animal", 
           "lion":"king of the jungle", 
           "elephant":"a gigantic herbivore"}
print(mammals["cat"])

"""
a cute animal
"""
print(mammals["lion"])

"""
king of the jungle
"""

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape","kiwi"]

sizes = [9.8, 10.1, 13.2, 8.7, 20.5]

fruits_sizes = {'fruits': fruits, 'size': sizes}

"""
df = dataframe
"""

import pandas as pd

df = pd.DataFrame.from_dict(fruits_sizes)


print(df['fruits'])
print(df['size'])
print(df['fruits'].min())
print(df['size'].mean())
print(df.describe())
print(df[df["size"] > 10])
print(df[1:3])

prices = [10.0, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns = ["size"], inplace = True)


######################################################################





































