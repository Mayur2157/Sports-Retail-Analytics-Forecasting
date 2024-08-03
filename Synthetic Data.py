import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Helper functions
def random_price():
    return round(random.uniform(20, 200), 2)

def random_discount():
    return round(random.uniform(0, 30), 2)

def random_rating():
    return round(random.uniform(1, 5), 2)

def random_review_count():
    return random.randint(0, 500)

def random_description():
    return fake.text(max_nb_chars=200)

# Constants
NUM_PRODUCTS = 1000
NUM_SALES = 5000
NUM_REVIEWS = 3000

# Generate products data
brands = ['Nike', 'Adidas', 'Puma', 'Under Armour', 'Reebok']
categories = ['Footwear', 'Clothing', 'Accessories']

products = pd.DataFrame({
    'product_id': range(1, NUM_PRODUCTS + 1),
    'brand': [random.choice(brands) for _ in range(NUM_PRODUCTS)],
    'category': [random.choice(categories) for _ in range(NUM_PRODUCTS)],
    'price': [random_price() for _ in range(NUM_PRODUCTS)],
    'description': [random_description() for _ in range(NUM_PRODUCTS)]
})

# Generate sales data
sales = pd.DataFrame({
    'sale_id': range(1, NUM_SALES + 1),
    'product_id': [random.randint(1, NUM_PRODUCTS) for _ in range(NUM_SALES)],
    'sale_date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(NUM_SALES)],
    'revenue': [random_price() for _ in range(NUM_SALES)],
    'discount': [random_discount() for _ in range(NUM_SALES)]
})

# Generate reviews data
reviews = pd.DataFrame({
    'review_id': range(1, NUM_REVIEWS + 1),
    'product_id': [random.randint(1, NUM_PRODUCTS) for _ in range(NUM_REVIEWS)],
    'review_date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(NUM_REVIEWS)],
    'rating': [random_rating() for _ in range(NUM_REVIEWS)],
    'review_count': [random_review_count() for _ in range(NUM_REVIEWS)]
})

# Save to CSV files
products.to_csv('products.csv', index=False)
sales.to_csv('sales.csv', index=False)
reviews.to_csv('reviews.csv', index=False)

print("Synthetic datasets created successfully!")
