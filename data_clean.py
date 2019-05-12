import pandas as pd
df = pd.read_csv('syn_fd.csv')
import warnings
warnings.filterwarnings(action='ignore')
import numpy as np
df=df.drop(['nameOrig', 'nameDest', 'isFlaggedFraud'],axis=1)
#print df.info()

new_df=df.loc[(df.type == 'TRANSFER') | (df.type == 'CASH_OUT')]
new_df.loc[new_df.type == 'TRANSFER', 'type'] = 0
new_df.loc[new_df.type == 'CASH_OUT', 'type'] = 1
new_df.type = new_df.type.astype(int)

new_dffraud = new_df.loc[(new_df.isFraud == 1)]
new_dfnonFraud = new_df.loc[(new_df.isFraud == 0)]

print len(new_dffraud.loc[(new_dffraud.oldbalanceDest == 0) & \
(new_dffraud.newbalanceDest == 0) & (new_dffraud.amount)])

print len(new_dffraud[(new_dffraud['amount'] != 0)])

print len(new_dfnonFraud.loc[(new_dfnonFraud.oldbalanceDest == 0) & \
(new_dfnonFraud.newbalanceDest == 0) & (new_dfnonFraud.amount)])

print len(new_dfnonFraud[(new_dfnonFraud['amount'] != 0)])

new_df.loc[(new_df.oldbalanceDest == 0) & (new_df.newbalanceDest == 0) & (new_df.amount != 0), ['oldbalanceDest', 'newbalanceDest']] = - 1

new_df.loc[(new_df.oldbalanceOrg == 0) & (new_df.newbalanceOrig == 0) & (new_df.amount != 0), ['oldbalanceOrg', 'newbalanceOrig']] = np.nan

print new_df[::5]