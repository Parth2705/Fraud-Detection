import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go
import warnings
warnings.filterwarnings("ignore")
import numpy as np
df = pd.read_csv('syn_fd.csv')
trace1 = go.Mesh3d(x=df['amount'][:40000], y=df['isFraud'][:40000], z=df['isFlaggedFraud'][:40000],
                   opacity=0.5,
                   color='rgba(244,22,100,0.6)'
                  )

layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        nticks=4, range = [-100,100],),
                    yaxis = dict(
                        nticks=4, range = [-50,100],),
                    zaxis = dict(
                        nticks=4, range = [-100,100],),),
                    width=700,
                    margin=dict(
                    r=20, l=10,
                    b=10, t=10)
                  )
fig = go.Figure(data=[trace1], layout=layout)
py.iplot(fig, filename='3d-axis-range')