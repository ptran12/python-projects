import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

excel_file_1 = '2018-2019_NBA Player_Stats.xlsx'

df_nba_data = pd.read_excel(excel_file_1, sheet_name = 'Sheet1')

# print(df_nba_data)
print(df_nba_data.iloc[1])
# print(df_nba_data.head(2))


# pivot = df_nba_data.groupby(['PPGPointsPoints per game.']).mean()
# print(pivot)