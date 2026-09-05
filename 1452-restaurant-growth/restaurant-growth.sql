SELECT DISTINCT c1.visited_on, SUM(c2.amount) AS amount, ROUND(sum(c2.amount) / 7, 2) AS average_amount
FROM Customer c1
JOIN Customer c2 
WHERE DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6 AND DATEDIFF( c1.visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6
GROUP BY c1.visited_on, c1.customer_id