import csv

input_file_path = '27\\today.csv' 
output_file_path = 'today.txt'

import pandas as pd


df = pd.read_csv(input_file_path)

df_unique = df.drop_duplicates(subset=['text_content'])

df_unique.to_csv(output_file_path, index=False)

print(f'Cleaned data saved to {output_file_path}')

