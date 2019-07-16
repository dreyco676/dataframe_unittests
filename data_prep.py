import pandas as pd

df = pd.read_csv('./datasets/train.csv')

df.to_csv('./datasets/titanic.csv.gz', compression='gzip')