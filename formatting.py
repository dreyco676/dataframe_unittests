import pandas as pd

# read in the data
df = pd.read_csv('./datasets/Metro_Interstate_Traffic_Volume.csv.gz', compression='gzip')

print(df.columns)
df['date_time'] = pd.to_datetime(df['date_time'])

import datetime

start = df['date_time'].min()
end = df['date_time'].max()
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

full_time_df = pd.DataFrame()
full_time_df['datetime'] = date_generated