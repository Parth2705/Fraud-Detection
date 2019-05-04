import pandas as pd
import plotly.plotly as py
df=pd.read_csv("syn_fd.csv")
def getType():
    types=[]
    for n in df['type']:
        if n not in types:
            types.append(n)
    print types
    return types
def getGraph(type1):
    fill_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
    types=type1


    gf=df[:40000]
    gf = gf.groupby('type')
    data=[]
    for type, fill_color in zip(types[::-1], fill_colors):
        group = gf.get_group(type)
        amount = group['amount'].tolist()
        length = len(amount)
        amount_cord = [type] * length
        isFraud = group['isFraud'].tolist()
        zeros = [0] * length

        data.append(dict(
            type='scatter3d',
            mode='lines',
            x=amount + amount[::-1] + [amount[0]],  # year loop: in incr. order then in decr. order then years[0]
            y=amount_cord * 2 + [amount_cord[0]],
            z=isFraud + zeros + [isFraud[0]],
            name='',
            surfaceaxis=1,  # add a surface axis ('1' refers to axes[1] i.e. the y-axis)
            surfacecolor=fill_color,
            line=dict(
                color='black',
                width=4
            ),
        ))
    layout = dict(
        title='Population from 1957 to 2007 [Gapminder]',
        showlegend=False,
        scene=dict(
            xaxis=dict(title=''),
            yaxis=dict(title=''),
            zaxis=dict(title=''),
            camera=dict(
                eye=dict(x=-1.7, y=-1.7, z=0.5)
            )
        )
    )

    fig = dict(data=data, layout=layout)

    # IPython notebook
    # py.iplot(fig, filename='filled-3d-lines')

    py.iplot(fig, filename='filled-3d-lines')


gtype=getType()
getGraph(gtype)

