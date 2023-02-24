import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#define figure and axes
fig, ax = plt.subplots()

#create values for table
table_data=[
    ["Plant Characteristic", "C3 Pathway","C4 Pathway","CAM Pathway" ],
    ["Photorespiration Rate", "High","Low / Negligible	","Very Low / Negligible"],
    ["Leaf Anatomy	", "Typical","Kranz	","Xeromorphic"],
    ["Typical Environments	", "All","Tropical, elevated daytime temperatures, drought","Dry, arid"],
    ["Number of Steps in Pathway", "1	","2","2"],
    ["First Molecule Produced in Pathway", "3-phophoglyceric acid", "Malic acid or aspartic acid", "	Malate"],
    ["Uses the Calvin Cycle?", "Yes", "	Yes", "	Yes"]
]

#create table
table = ax.table(cellText=table_data, loc='center')

#modify table
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')

#display table
plt.show()
