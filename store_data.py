import pandas as pd


df = pd.read_csv('syn_fd.csv')
print df.head()

for s in df['amount']:
