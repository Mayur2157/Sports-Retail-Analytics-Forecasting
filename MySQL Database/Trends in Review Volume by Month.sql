SELECT EXTRACT(YEAR FROM review_date) AS year, EXTRACT(MONTH FROM review_date) AS month, COUNT(review_id) AS review_count
FROM reviews
GROUP BY year, month
ORDER BY year, month;
