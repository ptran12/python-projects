import pandas as pd

excel_file_path = 'pmsm_temperature_data.csv'

df = pd.read_csv(excel_file_path)
print(df.columns)

# testing commit 