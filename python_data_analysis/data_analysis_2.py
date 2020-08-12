import pandas as pd

excel_file_path = 'pmsm_temperature_data.csv'

df = pd.read_csv(excel_file_path)
print(df.columns)

df_info = df.info()
print(df_info)

print(df.describe()['i_d'])

grouped_df = df.groupby(['profile_id']).max()
print (grouped_df['torque'])
# max torque grouped on the profile_ids