import pandas as pd
import plotly.express as px
from data_processing import get_data  # Import get_data function

def create_customer_segmentation_figure():
    query = """
        SELECT p.category, SUM(s.revenue) AS total_revenue
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.category
    """
    data = get_data(query)
    
    # Plotting total revenue by category
    fig = px.bar(data_frame=data, x='category', y='total_revenue',
                 title='Total Revenue by Product Category')
    
    fig.update_layout(xaxis_title='Category', yaxis_title='Total Revenue')
    return fig
