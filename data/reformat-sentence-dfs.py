import pandas as pd

file_name = "data/short_excerpts_df.csv"

data_df = pd.read_csv(file_name)

data_df['ACCOUNT'] = [1 if label == "True" else label for label in data_df['ACCOUNT']]
data_df['ACCOUNT'] = [0 if label == "False" else label for label in data_df['ACCOUNT']]
data_df['ACCOUNT'] = [int(label) for label in data_df['ACCOUNT']]

data_df.to_csv(file_name)