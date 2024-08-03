CREATE DATABASE sports_retail;
-- Switch to your new database
USE sports_retail;

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    brand VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    description TEXT
);

-- Create sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    revenue DECIMAL(10, 2),
    discount DECIMAL(5, 2)
);

-- Create reviews table
CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    product_id INT,
    review_date DATE,
    rating DECIMAL(3, 2),
    review_count INT
);
