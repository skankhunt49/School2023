import matplotlib.pyplot as plt
import numpy as np
import math
from gekko import GEKKO
import pandas as pd

cont = "y"
contWhole = "y"



while contWhole == "y" :
  contWhole = input("Continue? y or n :")
  print ("Choose Mode graphing, normal or algebraic")
  mode = input("Mode :")

#when it iterates the whole loop it misses the if statement
  if mode == "graphing" :
    pass

  elif mode == "normal" :
    while cont == "y" :
      print("Input First Value :")
      value1 = float(input())
      operator = input("Input Operator :")
      print("Input Second Value :")
      value2 = float(input())

      if operator == "+" :
        result = value1 + value2
        print(result)
        cont = input("Continue? y or n :")
      elif operator == "-" :
        result = value1 - value2
        print(result)
        cont = input("Continue? y or n :")
      elif operator == "*" :
        result = value2 * value1
        print(result)
        cont = input("Continue? y or n :")
      elif operator == "/" :
        result = value1 / value2
        print(result)
        cont = input("Continue? y or n :")
      elif operator == "^" :
        result = pow(value1, value2)
        print(result)
        cont = input("Continue? y or n :")
      else :
        print("ERROR")

  elif mode == "algebraic" :
    pass
  else :
    print("ERROR")