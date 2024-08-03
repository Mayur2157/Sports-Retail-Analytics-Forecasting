import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Function to get MySQL data
def get_data(query):
    # Connect to MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mayur2157',
        database='sports_retail'
    )
    # Fetch data
    data = pd.read_sql(query, connection)
    # Close connection
    connection.close()
    return data

# Query to get revenue data for Footwear and Clothing categories
query = """
    SELECT category, revenue
    FROM products
    JOIN sales ON products.product_id = sales.product_id
    WHERE category IN ('Footwear', 'Clothing')
"""

# Fetch data
data = get_data(query)

# Calculate median revenue by category
median_revenue = data.groupby('category')['revenue'].median().reset_index()
median_revenue.columns = ['category', 'median_revenue']

# Visualize the median revenue
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='median_revenue', data=median_revenue)
plt.title('Median Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Median Revenue')
plt.show()
