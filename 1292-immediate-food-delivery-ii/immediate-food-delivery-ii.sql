# Write your MySQL query statement below
SELECT ROUND(COUNT(CASE WHEN (customer_id, customer_pref_delivery_date) IN (SELECT customer_id, MIN(order_date) AS first_date FROM Delivery d GROUP BY customer_id) THEN 1 END) * 100.0 / COUNT(DISTINCT customer_id), 2) AS immediate_percentage FROM Delivery
