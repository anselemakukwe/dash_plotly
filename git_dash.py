import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('stock_data.csv')

cols = df.columns[1:-1]
opts = [{'label': i, 'value': i} for i in cols]

df['Date'] = pd.to_datetime(df.Date)
#dates = ['2015-02-17', '2015-05-17', '2015-08-17', '2015-11-17',
#        '2016-02-17', '2016-05-17', '2016-08-17', '2016-11-17', '2017-02-17']

trace_1 = go.Scatter(x=df.Date, y=df['AAPL.High'],
                     name='AAPL HIGH',
                     line=dict(width=2,
                               color='rgb(229, 151, 50)'))
layout = go.Layout(title='Time Series Plot',
                   hovermode='closest')
fig = go.Figure(data=[trace_1], layout=layout)

app.layout = html.Div([
    html.Div([
        html.H1("This is a Stock Dashboard"),
        html.P("Dash is so cool!!")
    ],
        style={'padding': '50px',
               'backgroundColor': '#3aaab2'}),
    dcc.Graph(id='plot', figure=fig),
    html.P([
        html.Label("Choose a feature"),
        dcc.Dropdown(id='opt', options=opts,
                     value=opts[0]['value'])
    ], style={'width': '400px',
              'fontSize': '20px',
              'padding-left': '100px',
              'display': 'inline-block'})
    ])

@app.callback(Output('plot', 'figure'),
              [Input('opt', 'value')])
def update_figure(input1):
    trace_1 = go.Scatter(x=df.Date, y=df['AAPL.High'],
                         name='AAPL HIGH',
                         line=dict(width=2,
                                   color='rgb(229, 151, 50)'))
    trace_2 = go.Scatter(x=df.Date, y=df[input1],
                         name=input1,
                         line=dict(width=2,
                                   color='rgb(106, 181, 135)'))
    fig = go.Figure(data=[trace_1, trace_2], layout=layout)
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)