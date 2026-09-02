# Write your MySQL query statement below
SELECT ROUND(COUNT(A1.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity A1 
INNER JOIN Activity A2 
ON A1.player_id = A2.player_id
AND DATE_ADD(A1.event_date, INTERVAL 1 DAY) = A2.event_date
WHERE (A1.player_id, A1.event_date) IN 
(SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id)