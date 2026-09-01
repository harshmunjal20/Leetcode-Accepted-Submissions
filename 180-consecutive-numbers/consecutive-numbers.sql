# Write your MySQL query statement below
# using window function LEAD(num, offset)

WITH ConsecutiveNumsTable AS (
    SELECT num, 
    LEAD(num, 1) OVER() AS next_day_num,
    LEAD(num, 2) OVER() AS next_next_day_num
    FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROM ConsecutiveNumsTable
WHERE num = next_day_num AND num = next_next_day_num