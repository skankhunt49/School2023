import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

plt.rcParams["figure.figsize"] = [15.0, 15.0]
plt.rcParams["figure.autolayout"] = True

#define figure and axes
fig, ax = plt.subplots()

#create values for table
table_data=[
    ["Advancement", "Date", "Category", "Advantages"],
    ["Spinning Jenny", "1760", "Feeding for weavers", "faster and more efficient"],
    ["Flying Shuttle", "1730s","weaving", "faster"],
    ["Water Frame", "1769", "thread making", "stronger"],
    ["Mule", "1779", "Cotton Production Overall", "Flexibility"]
]

#create table
table = ax.table(cellText=table_data, loc='center')

#modify table
table.set_fontsize(60)
table.scale(1, 2)
ax.axis('off')

#display table
plt.show()
