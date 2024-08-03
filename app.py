from flask import Flask, render_template
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from data_processing import get_filtered_data
from forecasting import create_forecast_figure
from clustering import create_customer_segmentation_figure

# Initialize Flask app
server = Flask(__name__)

# Initialize Dash app
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Data Analysis Dashboard"),
    dcc.Tabs([
        dcc.Tab(label='Revenue Forecast', children=[
            dcc.Graph(id='forecast-graph', figure=create_forecast_figure())
        ]),
        dcc.Tab(label='Customer Segmentation', children=[
            dcc.Graph(id='segmentation-graph', figure=create_customer_segmentation_figure())
        ]),
        dcc.Tab(label='Interactive Revenue', children=[
            dcc.Dropdown(
                id='category-dropdown',
                options=[
                    {'label': 'Footwear', 'value': 'Footwear'},
                    {'label': 'Clothing', 'value': 'Clothing'}
                ],
                value='Footwear'
            ),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date='2023-01-01',
                end_date='2023-12-31'
            ),
            dcc.Graph(id='revenue-graph')
        ])
    ])
])

# Callback to update the interactive revenue graph based on filters
@app.callback(
    Output('revenue-graph', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_graph(selected_category, start_date, end_date):
    data = get_filtered_data(selected_category, start_date, end_date)
    fig = px.bar(data, x='sale_date', y='revenue', title=f'Revenue for {selected_category}')
    return fig

# Flask route to serve the app
@server.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
