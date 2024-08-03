SELECT LENGTH(description) AS description_length, AVG(rating) AS avg_rating, COUNT(review_id) AS review_count
FROM products
JOIN reviews ON products.product_id = reviews.product_id
GROUP BY description_length;
