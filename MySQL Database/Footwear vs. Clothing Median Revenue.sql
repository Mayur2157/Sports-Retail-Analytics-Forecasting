-- Initialize variables
SET @rownum := 0, @total_rows := 0, @prev_category := '';

-- Calculate the median revenue for Footwear and Clothing
SELECT category, AVG(revenue) AS median_revenue
FROM (
    SELECT category, revenue,
           @rownum := IF(@prev_category = category, @rownum + 1, 1) AS row_number,
           @total_rows := IF(@prev_category = category, @total_rows + 1, 1),
           @prev_category := category
    FROM (SELECT @rownum := 0, @total_rows := 0, @prev_category := '') AS vars,
         (SELECT category, revenue
          FROM products
          JOIN sales ON products.product_id = sales.product_id
          WHERE category IN ('Footwear', 'Clothing')
          ORDER BY category, revenue) AS ordered_revenue
) AS ranked_revenue
WHERE row_number IN (FLOOR((@total_rows + 1) / 2), FLOOR((@total_rows + 2) / 2))
GROUP BY category;
