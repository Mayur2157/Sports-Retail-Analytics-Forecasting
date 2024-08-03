import pandas as pd
import plotly.graph_objects as go
from data_processing import get_data

def create_forecast_figure():
    query = """
        SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    """
    data = get_data(query)
    data['month'] = pd.to_datetime(data['month'], format='%Y-%m')
    data.set_index('month', inplace=True)

    # Check if there are enough data points
    if len(data) < 24:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['total_revenue'], mode='lines+markers', name='Actual'))
        fig.update_layout(title='Monthly Revenue (Not Enough Data for Forecast)', xaxis_title='Month', yaxis_title='Total Revenue')
        return fig

    # Exponential Smoothing Model
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    model = ExponentialSmoothing(data['total_revenue'], trend='add', seasonal='add', seasonal_periods=12)
    model_fit = model.fit()
    forecast = model_fit.forecast(12)
    forecast_index = pd.date_range(start=data.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['total_revenue'], mode='lines+markers', name='Actual'))
    fig.add_trace(go.Scatter(x=forecast_index, y=forecast, mode='lines', name='Forecast'))
    fig.update_layout(title='Monthly Revenue Forecast', xaxis_title='Month', yaxis_title='Total Revenue')
    return fig
