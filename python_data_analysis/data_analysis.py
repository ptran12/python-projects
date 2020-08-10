import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

excel_file_1 = 'shift-data.xlsx'
excel_file_2 = 'third-shift-data.xlsx'

df_first_shit = pd.read_excel(excel_file_1, sheet_name = 'first')
df_second_shift = pd.read_excel(excel_file_1, sheet_name = 'second')
df_third_shift = pd.read_excel(excel_file_2)


print(df_first_shit)