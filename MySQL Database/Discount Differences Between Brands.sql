SELECT brand, AVG(discount) AS avg_discount
FROM sales
JOIN products ON sales.product_id = products.product_id
WHERE brand IN ('Nike', 'Adidas')
GROUP BY brand;
