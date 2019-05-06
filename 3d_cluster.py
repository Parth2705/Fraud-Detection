import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
import numpy as np
df = pd.read_csv('syn_fd.csv')
# print df.head()
colors = np.random.rand(10)
scatter = dict(
    mode = "markers",
    name = "y",
    type = "scatter3d",
    x=df['amount'][:40000], y=df['isFraud'][:40000], z=df['isFlaggedFraud'][:40000],
    marker = dict( size=2, color="rgb(23, 190, 207)" )
)
clusters = dict(
    alphahull = 7,
    name = "y",
    opacity = 0.1,
    type = "mesh3d",
    x=df['amount'][:40000], y=df['isFraud'][:40000], z=df['oldbalanceOrg'][:40000]
)
layout = dict(
    title = '3d point clustering',
    scene = dict(
        xaxis = dict( zeroline=False ),
        yaxis = dict( zeroline=False ),
        zaxis = dict( zeroline=False ),
    )
)
fig1 = dict( data=[scatter, clusters], layout=layout )

py.iplot(fig1, filename='3d point clustering')
print df['isFraud'].size
z1=np.random.rand(40000)
z= np.random.rand(df['amount'].size)
# print z
trace1 = go.Scatter3d(
    x=df['amount'][:40000], y=df['isFraud'][:40000], z=df['oldbalanceOrg'][:40000],
    mode='markers',
    marker=dict(
        size=12,
        color=z1,
        colorscale='Viridis',
        opacity=0.7# set color to an array/list of desired values
           # choose a colorscale

    )
)

data122 = [trace1]
layout1 = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    ),
    scene = dict(
                    xaxis = dict(
                        title='Amount'),
                    yaxis = dict(
                        title='is Fraud'),
                    zaxis = dict(
                        title='Original Balance'),)
)
fig = go.Figure(data=data122, layout=layout1)
py.iplot(fig, filename='sad')
fig1 = go.Figure()

fig1.add_scatter(x=df['amount'],
                y=df['isFraud'],
                mode='markers',
                marker={
                        'color': z,
                        'opacity': 0.6,

                       });
iplot(fig1)
pio.write_image(fig1, 'fig1.png')