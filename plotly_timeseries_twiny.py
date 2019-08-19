import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

hob = pd.read_csv('H26_20190531.csv', skiprows=2, usecols=[1, 2, 3],
                              names=['time', 'T', 'RH'],
                              index_col='time', parse_dates=True)
hob = hob.resample('W').mean()
fig = make_subplots(specs=[[{"secondary_y": True}]])
#fig = go.Figure(go.Scatter(x=hob.index, y=hob['T']))

fig.add_trace(go.Scatter(
                x=hob.index,
                y=hob['T'],
                name="Temperature"),secondary_y=False)

fig.add_trace(go.Scatter(
                x=hob.index,
                y=hob['RH'],
                name="RH",
                #line_color='deepskyblue',
                opacity=0.8),secondary_y=True)

fig.update_xaxes(title_text="Datetime - UTC")
fig.update_yaxes(title_text="Temperature (°C)", secondary_y=False)
fig.update_yaxes(title_text="RH (%)", secondary_y=True)

fig.update_layout(title_text='H26')
pio.write_html(fig, file='H26_temp_rh.html', auto_open=True)

