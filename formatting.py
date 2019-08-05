import pandas as pd
from datetime import datetime, timedelta

# read in the data
df = pd.read_csv('./datasets/Metro_Interstate_Traffic_Volume.csv.gz', compression='gzip')

print(df.columns)
df['date_time'] = pd.to_datetime(df['date_time'])


start_date = df['date_time'].min()
end_date = df['date_time'].max()


def date_range(start_date, end_date):
    delta = timedelta(hours=1)
    full_dt_list = list()
    current_date = start_date
    while current_date < end_date:
        full_dt_list.append(current_date)
        current_date += delta
    return full_dt_list


full_time_df = pd.DataFrame()
full_time_df['datetime'] = date_range(start_date, end_date)