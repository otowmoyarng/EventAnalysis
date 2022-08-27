from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__)

df = pd.read_csv('../csv/import.csv')

fig = px.bar(df, x="Target", y="Count", color="EventSite", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='イベント参加件数'),
    html.Div(children='Dash: A web application framework for your data.'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)