import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('syn_fd.csv')

# dftype = df['type']
# dfIsFlaggedFraud = df['isFlaggedFraud']
# dfTyIs=[]
# # print type(dftype)
# dfNotFlagged = df.loc[(df['isFlaggedFraud'] == 0) & (df.type)]
# # print dfFlagged
# df_flagNotFraud = dfNotFlagged.groupby(['type']).sum().isFlaggedFraud

# print df_flagNotFraud

types = []
for n in df['type']:
    if n not in types:
        types.append(n)
print types


gf1 = df.groupby('type')
data = []
for type1 in types[::-1]:
    group = gf1.get_group(type1)
    # print group
    amount = group['isFlaggedFraud'].tolist()
    length = len(amount)
    amount_cord = [type1] * length
    isFraud = group['isFraud'].tolist()
    zeros = [0] * length
print isFraud
print "\n"
print zeros
print "\n"
print amount
print "\n"
print amount_cord
    #
    # data.append(dict(
    #     type='scatter3d',
    #     mode='lines',
    #     z=amount + amount[::-1] + [amount[0]],  # year loop: in incr. order then in decr. order then years[0]
    #     y=amount_cord * 2 + [amount_cord[0]],
    #     x=isFraud + zeros + [isFraud[0]],
    #     name='',
    #     surfaceaxis=1,  # add a surface axis ('1' refers to axes[1] i.e. the y-axis)
    #     surfacecolor=fill_color,
    #     line=dict(
    #         color='black',
    #         width=4
    #     ),
    # ))
# trace1 = go.Bar(
#     x=df_flagFraud['type'],
#     y=df_flagFraud[1],
#     name='Flagged Fraud',
#     marker=dict(
#         color='rgb(55, 83, 109)'
#     )
# )
# trace2 = go.Bar(
#     x=df_flagNotFraud[0],
#     y=df_flagNotFraud[1],
#     name='Flagged Not Fraud',
#     marker=dict(
#         color='rgb(26, 118, 255)'
#     )
# )
# data = [trace1, trace2]
# layout = go.Layout(
#     title='Number of Fraud Flags per payment type',
#     xaxis=dict(
#         tickfont=dict(
#             size=14,
#             color='rgb(107, 107, 107)'
#         )
#     ),
#     yaxis=dict(
#         title='No of Transactions',
#         titlefont=dict(
#             size=16,
#             color='rgb(107, 107, 107)'
#         ),
#         tickfont=dict(
#             size=14,
#             color='rgb(107, 107, 107)'
#         )
#     ),
#     legend=dict(
#         x=0,
#         y=1.0,
#         bgcolor='rgba(255, 255, 255, 0)',
#         bordercolor='rgba(255, 255, 255, 0)'
#     ),
#     barmode='group',
#     bargap=0.15,
#     bargroupgap=0.1
# )
#
# fig = go.Figure(data=data, layout=layout)
# py.iplot(fig, filename='style-bar')