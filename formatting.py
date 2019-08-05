import pandas as pd

# read in the data
df = pd.read_csv('./datasets/Metro_Interstate_Traffic_Volume.csv.gz', compression='gzip')

print(df.columns)
df['date_time'] = pd.to_datetime(df['date_time'])