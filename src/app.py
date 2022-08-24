from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)