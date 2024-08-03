SELECT revenue, review_count
FROM sales
JOIN reviews ON sales.product_id = reviews.product_id;
