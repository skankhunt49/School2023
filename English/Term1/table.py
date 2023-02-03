import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#define figure and axes
fig, ax = plt.subplots()

#create values for table
table_data=[
    ["Player 1", 30],
    ["Player 2", 20],
    ["Player 3", 33],
    ["Player 4", 25],
    ["Player 5", 12]
]

#create table
table = ax.table(cellText=table_data, loc='center')

#modify table
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')

#display table
plt.show()
