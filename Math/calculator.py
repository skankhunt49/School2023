import matplotlib.pyplot as plt
import numpy as np
import math
from gekko import GEKKO
import pandas as pd

print ("Choose Mode graphing, normal or algebraic")
mode = input("Mode :")

if mode == "graphing" :
  pass
elif mode == "normal" :
  print("Input First Value :")
  value1 = input()
  operator = input("Input Operator :")
  print
elif mode == "algebraic" :
  pass
else :
  print("ERROR")