import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go
import warnings
warnings.filterwarnings("ignore")
import numpy as np
df = pd.read_csv('syn_fd.csv')
trace1 = go.Mesh3d(x=df['amount'][:200000], y=df['oldbalanceOrg'][:200000], z=df['isFraud'][:200000],
                   opacity=0.5,
                   color='rgba(244,22,100,0.6)'
                  )
trace2 = go.Mesh3d(x=df['amount'][:200000], y=df['newbalanceDest'][:200000], z=df['isFlaggedFraud'][:200000],
                   opacity=0.5,
                   color='rgba(45, 205, 180,0.7)'
                  )
layout = go.Layout(
                    scene = dict(
                    ),
                    width=700,
                    margin=dict(
                    r=20, l=10,
                    b=10, t=10)
                  )
fig = go.Figure(data=[trace1,trace2], layout=layout)
py.iplot(fig, filename='3d-axis-range3')