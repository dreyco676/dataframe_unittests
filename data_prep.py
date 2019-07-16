import pandas as pd

# read in the data
df = pd.read_csv('./datasets/titanic.csv.gz', compression='gzip')

# make 50% of the data as 'historical'
hist_df = df.sample(frac=.5)

# make 50% of the data as 'new'
new_df = df.sample(frac=.5)