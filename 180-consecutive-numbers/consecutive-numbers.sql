# Write your MySQL query statement below
# using window function LEAD(num, offset)

WITH consecutiveNumsTable AS (
    SELECT id, num, 
    LEAD(num, 1) OVER() AS next_Day_num,
    LEAD(num, 2) OVER() AS next_next_Day_num
    FROM Logs
)

SELECT DISTINCT num
AS ConsecutiveNums
FROM consecutiveNumsTable
WHERE num = next_day_num AND num = next_next_Day_num