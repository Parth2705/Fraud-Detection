import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from plotly import tools
df = pd.read_csv('syn_fd.csv')

dftype = df['type']
# dfIsFlaggedFraud = df['isFlaggedFraud']
# dfTyIs=[]
# # print type(dftype)
dftypecount=[]
dfNotFlaggedPay = df.loc[(df['isFlaggedFraud'] == 0) & (df['type'] == 'PAYMENT')]
dfFlaggedPay = df.loc[(df['isFlaggedFraud'] == 1) & (df['type'] == 'PAYMENT')]
dfNotFlaggedTr = df.loc[(df['isFlaggedFraud'] == 0) & (df['type'] == 'TRANSFER')]
dfFlaggedTr = df.loc[(df['isFlaggedFraud'] == 1) & (df['type'] == 'TRANSFER')]
dfNotFlaggedCO = df.loc[(df['isFlaggedFraud'] == 0) & (df['type'] == 'CASH_OUT')]
dfFlaggedCO = df.loc[(df['isFlaggedFraud'] == 1) & (df['type'] == 'CASH_OUT')]
dfNotFlaggedCI = df.loc[(df['isFlaggedFraud'] == 0) & (df['type'] == 'CASH_IN')]
dfFlaggedCI = df.loc[(df['isFlaggedFraud'] == 1) & (df['type'] == 'CASH_IN')]
dfNotFlaggedDB = df.loc[(df['isFlaggedFraud'] == 0) & (df['type'] == 'DEBIT')]
dfFlaggedDB = df.loc[(df['isFlaggedFraud'] == 1) & (df['type'] == 'DEBIT')]
# Fraud Coloumn
dfNotFraudPay = df.loc[(df['isFraud'] == 0) & (df['type'] == 'PAYMENT')]
dfFraudPay = df.loc[(df['isFraud'] == 1) & (df['type'] == 'PAYMENT')]
dfNotFraudTr = df.loc[(df['isFraud'] == 0) & (df['type'] == 'TRANSFER')]
dfFraudTr = df.loc[(df['isFraud'] == 1) & (df['type'] == 'TRANSFER')]
dfNotFraudCO = df.loc[(df['isFraud'] == 0) & (df['type'] == 'CASH_OUT')]
dfFraudCO = df.loc[(df['isFraud'] == 1) & (df['type'] == 'CASH_OUT')]
dfNotFraudCI = df.loc[(df['isFraud'] == 0) & (df['type'] == 'CASH_IN')]
dfFraudCI = df.loc[(df['isFraud'] == 1) & (df['type'] == 'CASH_IN')]
dfNotFraudDB = df.loc[(df['isFraud'] == 0) & (df['type'] == 'DEBIT')]
dfFraudDB = df.loc[(df['isFraud'] == 1) & (df['type'] == 'DEBIT')]

dfNotFraudPay = df.loc[(df['isFraud'] == 0) & (df['type'] == 'PAYMENT')]
dfFraudPay = df.loc[(df['isFraud'] == 1) & (df['type'] == 'PAYMENT')]
dfNotFraudTr = df.loc[(df['isFraud'] == 0) & (df['type'] == 'TRANSFER')]
dfFraudTr = df.loc[(df['isFraud'] == 1) & (df['type'] == 'TRANSFER')]
dfNotFraudCO = df.loc[(df['isFraud'] == 0) & (df['type'] == 'CASH_OUT')]
dfFraudCO = df.loc[(df['isFraud'] == 1) & (df['type'] == 'CASH_OUT')]
dfNotFraudCI = df.loc[(df['isFraud'] == 0) & (df['type'] == 'CASH_IN')]
dfFraudCI = df.loc[(df['isFraud'] == 1) & (df['type'] == 'CASH_IN')]
dfNotFraudDB = df.loc[(df['isFraud'] == 0) & (df['type'] == 'DEBIT')]
dfFraudDB = df.loc[(df['isFraud'] == 1) & (df['type'] == 'DEBIT')]

# Name of origin
dfCustPay = df.loc[ (df['type'] == 'PAYMENT')&(df['nameOrig'].str.contains('C'))]
dfMerchPay = df.loc[ (df['type'] == 'PAYMENT')&(df['nameOrig'].str.contains('M'))]
dfCustTr = df.loc[ (df['type'] == 'TRANSFER')&(df['nameOrig'].str.contains('C'))]
dfMerchTr = df.loc[ (df['type'] == 'TRANSFER')&(df['nameOrig'].str.contains('M'))]
dfCustCO = df.loc[ (df['type'] == 'CASH_OUT')&(df['nameOrig'].str.contains('C'))]
dfMerchCO = df.loc[ (df['type'] == 'CASH_OUT')&(df['nameOrig'].str.contains('M'))]
dfCustCI = df.loc[ (df['type'] == 'CASH_IN')&(df['nameOrig'].str.contains('C'))]
dfMerchCI = df.loc[ (df['type'] == 'CASH_IN')&(df['nameOrig'].str.contains('M'))]
dfCustDB = df.loc[ (df['type'] == 'DEBIT')&(df['nameOrig'].str.contains('C'))]
dfMerchDB = df.loc[ (df['type'] == 'DEBIT') & (df['nameOrig'].str.contains('M'))]

#name of dest
dfDestCustPay = df.loc[ (df['type'] == 'PAYMENT')&(df['nameDest'].str.contains('C'))]
dfDestMerchPay = df.loc[ (df['type'] == 'PAYMENT')&(df['nameDest'].str.contains('M'))]
dfDestCustTr = df.loc[ (df['type'] == 'TRANSFER')&(df['nameDest'].str.contains('C'))]
dfDestMerchTr = df.loc[ (df['type'] == 'TRANSFER')&(df['nameDest'].str.contains('M'))]
dfDestCustCO = df.loc[ (df['type'] == 'CASH_OUT')&(df['nameDest'].str.contains('C'))]
dfDestMerchCO = df.loc[ (df['type'] == 'CASH_OUT')&(df['nameDest'].str.contains('M'))]
dfDestCustCI = df.loc[ (df['type'] == 'CASH_IN')&(df['nameDest'].str.contains('C'))]
dfDestMerchCI = df.loc[ (df['type'] == 'CASH_IN')&(df['nameDest'].str.contains('M'))]
dfDestCustDB = df.loc[ (df['type'] == 'DEBIT')&(df['nameDest'].str.contains('C'))]
dfDestMerchDB = df.loc[ (df['type'] == 'DEBIT') & (df['nameDest'].str.contains('M'))]
print dftype.drop_duplicates()
print (dfNotFlaggedPay['type'].count())
trace_Merch= go.Bar(
    y=[dfMerchPay['type'].count(),dfMerchTr['type'].count(),dfMerchCI['type'].count(),\
       dfMerchCO['type'].count(),dfMerchDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Merchant Origin Transactions',
    marker=dict(
        color='rgb(5, 127, 105)'
    )
)
trace_Cust= go.Bar(
    y=[dfCustPay['type'].count(),dfCustTr['type'].count(),dfCustCI['type'].count(),\
       dfCustCO['type'].count(),dfCustDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Customer Origin Transactions',
    marker=dict(
        color='rgb(1, 68, 37)'
    )
)
traceD_Merch= go.Bar(
    y=[dfDestMerchPay['type'].count(),dfDestMerchTr['type'].count(),dfDestMerchCI['type'].count(),\
       dfDestMerchCO['type'].count(),dfDestMerchDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Merchant Destination Transactions',
    marker=dict(
        color='rgb(5, 127, 105)'
    )
)
traceD_Cust= go.Bar(
    y=[dfDestCustPay['type'].count(),dfDestCustTr['type'].count(),dfDestCustCI['type'].count(),\
       dfDestCustCO['type'].count(),dfDestCustDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Customer Destination Transactions',
    marker=dict(
        color='rgb(2, 98, 137)'
    )
)
trace1 = go.Bar(
    y=[dfNotFlaggedPay['type'].count(),dfNotFlaggedTr['type'].count(),dfNotFlaggedCI['type'].count(),\
       dfNotFlaggedCO['type'].count(),dfNotFlaggedDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Not Flagged Fraud',
    marker=dict(
        color='rgb(55, 83, 109)'
    )
)
trace2 = go.Bar(
    y=[dfFlaggedPay['type'].count(),dfFlaggedTr['type'].count(),dfFlaggedCI['type'].count(),\
       dfFlaggedCO['type'].count(),dfFlaggedDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Flagged Fraud',
    marker=dict(
        color='rgb(26, 118, 255)'
    )
)
trace3 = go.Bar(
    y=[dfNotFraudPay['type'].count(),dfNotFraudTr['type'].count(),dfNotFraudCI['type'].count(),\
       dfNotFraudCO['type'].count(),dfNotFraudDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Not Fraud',
    marker=dict(
        color='rgb(45, 182, 237)'
    )
)
trace4 = go.Bar(
    y=[dfFraudPay['type'].count(),dfFraudTr['type'].count(),dfFraudCI['type'].count(),\
       dfFraudCO['type'].count(),dfFraudDB['type'].count()],
    x=['PAYMENT','TRANSFER','CASH_IN','CASH_OUT','DEBIT'],
    name='Fraud',
    marker=dict(
        color='rgb(3, 114, 122)'
    )
)

layout = go.Layout(
    title='Number of Not_Fraud Flags per payment type',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='No of Transactions',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)
layout1 = go.Layout(
    title='name of Originator per type',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='No of Transactions',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)
fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Flagged Not Fraud', 'Flagged Fraud', 'Not Fraud', 'Fraud'))
fig1 = tools.make_subplots(rows=2, cols=2, subplot_titles=( 'Merchant Origin', 'Customer Origin','Merchant Destination', 'Customer Destination '))

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

# fig of name
fig1.append_trace(trace_Merch, 1, 1)
fig1.append_trace(trace_Cust, 1, 2)
fig1.append_trace(traceD_Merch, 2, 1)
fig1.append_trace(traceD_Cust, 2, 2)
py.iplot(fig, filename='Payment_Fraud Bar Chart')
py.iplot(fig1, filename='Name of Originator Bar Chart')