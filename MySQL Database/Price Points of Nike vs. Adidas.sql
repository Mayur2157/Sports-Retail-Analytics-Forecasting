SELECT brand, AVG(price) AS avg_price
FROM products
WHERE brand IN ('Nike', 'Adidas')
GROUP BY brand;
