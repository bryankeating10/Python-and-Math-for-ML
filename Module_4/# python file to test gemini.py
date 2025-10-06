# python file to test gemini

# This is my practice using series datatype

import pandas as pd
import numpy as np

data = np.array(['g','e','m','i','n','i'])
ser1 = pd.Series(data)
print(ser1)

ser2 = pd.Series(data, index=[10,11,12,13,14,15])
print(ser2)

addition = pd.concat([ser1,ser2])
print(addition)

# String element-wise addition
new_series = pd.Series({1:'g',2:'e',3:'m',4:'i',5:'n',6:'i',10:'g',11:'e',12:'m',13:'i',14:'n',15:'i'})
print(new_series)
ew_add = addition + new_series
print(ew_add)
ew_add *= 2
print(ew_add)

stopped_using_gemini = ew_add[ew_add != 'geminigemini']
print(stopped_using_gemini)
