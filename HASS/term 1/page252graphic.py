import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

plt.rcParams["figure.figsize"] = [15.0, 15.0]
plt.rcParams["figure.autolayout"] = True

#define figure and axes
fig, ax = plt.subplots()

#create values for table
table_data=[
    ["Why??", "Industrial Revolution Flourishes In Britain", "Why??"],
    ["Prime Cause :", "British Imperialism", "The Reach and Power of the British Empire"],
    ["Second Cause :", "Population Grows","Large Amounts of Exploitable Labour"],
    ["Third Cause : ", "Abundance of Natural Resources", "Allows Construction and Power to Flourish"]
]

#create table
table = ax.table(cellText=table_data, loc='center')

#modify table
table.set_fontsize(60)
table.scale(1, 2)
ax.axis('off')

#display table
plt.show()
