import pandas as pd
df = pd.read_csv('syn_fd.csv')

dfFraudTransfer = df.loc[(df.isFraud == 1) & (df.type == 'TRANSFER')]
dfFraudCashout = df.loc[(df.isFraud == 1) & (df.type == 'CASH_OUT')]
dfTransfer = df.loc[df.type == 'TRANSFER']
dfFlagged = df.loc[df.isFlaggedFraud == 1]
dfNotFlagged = df.loc[df.isFlaggedFraud == 0]
dfNotFraud = df.loc[df.isFraud == 0]

#Fraudulent TRANSFERs whose destination accounts are originators of \
#genuine CASH_OUTs
dfprint= dfFraudTransfer.loc[dfFraudTransfer.nameDest.\
    isin(dfNotFraud.loc[dfNotFraud.type == 'CASH_OUT'].nameOrig.drop_duplicates())]

#fraudulent TRANSFER to C423543548 occured at step = 486 whereas \genuine CASH_OUT from this account occured earlier at step
dfprint1=dfNotFraud.loc[(dfNotFraud.type == 'CASH_OUT')].step.values
print dfprint1