import pandas as pd
import openpyxl
input_file_path = 'today.txt'
output_file_path = 'Facebook 2.xlsx' 

# Read CSV into DataFrame
df = pd.read_csv(input_file_path)

# Save DataFrame to Excel
df.to_excel(output_file_path, index=False)

print(f'Cleaned data saved to {output_file_path}')
