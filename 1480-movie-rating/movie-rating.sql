# Write your MySQL query statement below
(SELECT u.name AS results 
FROM Users u 
INNER JOIN MovieRating mr
ON u.user_id = mr.user_id
GROUP BY u.user_id
ORDER BY COUNT(mr.rating) DESC, u.name ASC
LIMIT 1
)

UNION ALL

(SELECT m.title AS results
FROM Movies m
INNER JOIN MovieRating mr
ON m.movie_id = mr.movie_id
WHERE created_at LIKE "2020-02-%"
GROUP BY m.movie_id
ORDER BY AVG(mr.rating) DESC, m.title ASC
LIMIT 1
)