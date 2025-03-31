import pandas as pd

file_path = 'Data/winequality-red.csv'
df = pd.read_csv(file_path, sep=';')

print("--- Head ---")
print(df.head())

print("\n--- Info ---")
df.info()

print("\n--- Describe ---")
print(df.describe())

print("\n--- Quality Counts ---")
print(df['quality'].value_counts().sort_index())
