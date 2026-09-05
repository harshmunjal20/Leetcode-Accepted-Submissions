# Write your MySQL query statement below
SELECT requester_id AS id, COUNT(accepter_id) AS num FROM (SELECT * FROM RequestAccepted
UNION
SELECT accepter_id AS requester_id, requester_id AS accepter_id, accept_date FROM RequestAccepted) AS Temp
GROUP BY requester_id ORDER BY num DESC LIMIT 1