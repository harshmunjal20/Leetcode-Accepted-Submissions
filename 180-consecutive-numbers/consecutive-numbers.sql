# Write your MySQL query statement below
WITH ConsecutiveNumsTable AS (
    SELECT id, num,
    LEAD(num, 1) OVER(ORDER BY id) AS next_id_num,
    LEAD(num, 2) OVER(ORDER BY id) AS next_next_id_num
    FROM Logs
)

SELECT DISTINCT  num AS ConsecutiveNums FROM ConsecutiveNumsTable 
WHERE num = next_id_num AND num = next_next_id_num