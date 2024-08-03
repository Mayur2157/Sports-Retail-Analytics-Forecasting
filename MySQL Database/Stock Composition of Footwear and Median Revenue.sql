-- Initialize variables
SET @rownum := 0, @total_rows := 0;

-- Calculate the count of footwear products and the median revenue
SELECT COUNT(product_id) AS footwear_count,
       AVG(revenue) AS median_revenue
FROM (
    SELECT revenue,
           @rownum := @rownum + 1 AS row_number,
           @total_rows := @rownum
    FROM sales
    JOIN products ON sales.product_id = products.product_id
    WHERE category = 'Footwear'
    ORDER BY revenue
) AS subquery
WHERE row_number IN (FLOOR((@total_rows + 1) / 2), FLOOR((@total_rows + 2) / 2));
