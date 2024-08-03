import pandas as pd
from sqlalchemy import create_engine

def get_data(query):
    engine = create_engine('mysql+mysqlconnector://root:Mayur2157@localhost/sports_retail')
    data = pd.read_sql(query, engine)
    return data



def get_filtered_data(category, start_date, end_date):
    query = f"""
        SELECT category, revenue, sale_date
        FROM products
        JOIN sales ON products.product_id = sales.product_id
        WHERE category = '{category}' AND sale_date BETWEEN '{start_date}' AND '{end_date}'
    """
    return get_data(query)
