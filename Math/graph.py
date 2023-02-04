import matplotlib.pyplot as plt
import numpy as np


#sets up 4 by 2 subplots
fig, axes = plt.subplots(4, 2, figsize=(8,8))

#plots height with respect to t and titles
def plot(title, x, y, pos0, pos1) :
  axes[pos0, pos1].set_title(title)
  axes[pos0, pos1].plot(x, y)