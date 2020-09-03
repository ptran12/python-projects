import pandas as pd
import csv as cs

Table_Name = 'NBA_Players'

df = pd.read_csv('test.csv', header = 0)
# print(df.head())

# create output file 
with open("output.txt", "w"):
    for index, row in df.iterrows():
        print('INSET INTO ' + Table_Name + '(\'Passenger\',\'Pclass\',\'Name\') VALUES (',
            row['Passenger'], ',',row['Pclass'],',\''+row['Name']+'\');', file=open("output.text", "a"))

