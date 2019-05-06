import pandas as pd
import json
import cPickle as pk
import datetime
import plotly
plotly.tools.set_credentials_file(username='Parth2705', api_key='b76SlksEiwZMVfOQhVuN')
import plotly.plotly as py
import plotly.graph_objs as go
from collections import Counter
import warnings
warnings.filterwarnings("ignore")
file="consumer_complaints.csv"

def now():
    tmp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return tmp

def my_file_read(file):
    df = pd.read_csv(file)
    print("{}: {} has {} observations and {} columns".format(now(), file, df.shape[0], df.shape[1]))
    print("{}: Column name checking::: {}".format(now(), df.columns.tolist()))
    return df
def checking_na(df):
    try:
        if (isinstance(df, pd.DataFrame)):
            df_na_bool = pd.concat([df.isnull().any(), df.isnull().sum(), (df.isnull().sum()/df.shape[0])*100],
                                   axis=1, keys=['df_bool', 'df_amt', 'missing_ratio_percent'])
            df_na_bool = df_na_bool.loc[df_na_bool['df_bool'] == True]
            return df_na_bool
        else:
            print("{}: The input is not panda DataFrame".format(now()))

    except (UnboundLocalError, RuntimeError):
        print("{}: Something is wrong".format(now()))
data=my_file_read(file)
checking_na(data)


for col in data.columns:
    data[col] = data[col].astype(str)
state_count={}

for s in data['state']:
    if s in state_count:
        state_count[s]+=1
    else:
        state_count[s]=1
print str(state_count)

state_list=[]
for i,j in state_count.iteritems():
    state_list.append ((i,j))
colorscale = [[0.0,"#f7fbff"],[0.05,"#ebf3fb"],[0.11,"#deebf7"],[0.16,"#d2e3f3"],[0.22,"#c6dbef"],[0.27,"#b3d2e9"],[0.33,"#9ecae1"],
              [0.38,"#85bcdb"],[0.45,"#6baed6"],[0.57,"#57a0ce"],[0.62,"#4292c6"],[0.68,"#3082be"],[0.73,"#2171b5"],[0.79,"#1361a9"],
              [0.84,"#08519c"],[0.90,"#0b4083"],[1.0,"#08306b"]]
scl=[[0.0, 'rgb(165,0,38)'], [0.1111111111111111, 'rgb(215,48,39)'], [0.2222222222222222, 'rgb(244,109,67)'], [0.3333333333333333, 'rgb(253,174,97)'], [0.4444444444444444, 'rgb(254,224,144)'], [0.5555555555555556, 'rgb(224,243,248)'], [0.6666666666666666, 'rgb(171,217,233)'], [0.7777777777777778, 'rgb(116,173,209)'], [0.8888888888888888, 'rgb(69,117,180)'], [1.0, 'rgb(49,54,149)']]
print state_count.keys()
data1 = [go.Choropleth(
    colorscale = colorscale,
    autocolorscale = False,
    locations = state_count.keys(),
    z=state_count.values(),
    text=state_count.keys(),
    locationmode = 'USA-states',
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,225)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "No of Complaints")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = 'Consumer Complaints by State<br>(Hover for breakdown)'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(0, 0, 255)'),
)

fig = go.Figure(data = data1, layout = layout)
py.iplot(fig, filename = 'd3-cloropleth-map')