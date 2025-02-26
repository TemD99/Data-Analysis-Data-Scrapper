# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:34:01 2023

@author: Temitayo
"""

import pandas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pandas.read_csv("C:/Users/Temitayo/Desktop/DVM/DVM/work/Researchproject/AI_Companies.csv")
subset_df = df.head(10)

df['EMPLOYEES'] = pd.to_numeric(df['EMPLOYEES'], errors='coerce')
subset_df = df.head(20)

plt.figure(figsize=(10, 6)) # Increase the figure size
plt.bar(subset_df['NAME'], subset_df['EMPLOYEES'], color='skyblue', edgecolor='blue') # Change bar color
plt.xlabel('Company Name', fontsize=12) # Increase font size
plt.ylabel('Number of Employees', fontsize=12) # Increase font size
plt.title('Number of Employees by Company', fontsize=14, fontweight='bold') # Increase font size and add bold
plt.xticks(rotation=90, fontsize=10) # Rotate x-axis labels
plt.yticks(fontsize=10) # Customize y-axis labels
plt.ylim(0, subset_df['EMPLOYEES'].max() + 1000) # Add space at the top
plt.grid(axis='y', linestyle='--') # Add horizontal grid lines
plt.tight_layout() # Adjust layout to avoid overlap
plt.show()



def convert_funding(value):
    try:
        number, magnitude = value.split(' ')
        number = float(number)
        if magnitude == 'M':
            number *= 1e6
        return number
    except:
        return value

df['FUNDING'] = df['FUNDING'].apply(convert_funding)
subset_df = df.head(10)

plt.figure(figsize=(10, 6)) 
plt.plot(subset_df['NAME'], subset_df['FUNDING'], color='green', marker='o', linestyle='-', linewidth=2) # Customize line
plt.xlabel('Company Name', fontsize=12)
plt.ylabel('Funding (in USD)', fontsize=12) 
plt.title('Funding by Company', fontsize=14, fontweight='bold') 
plt.xticks(rotation=90, fontsize=10) 
plt.yticks(fontsize=10) 
plt.grid(axis='both', linestyle='--') 
plt.tight_layout() #
plt.show()