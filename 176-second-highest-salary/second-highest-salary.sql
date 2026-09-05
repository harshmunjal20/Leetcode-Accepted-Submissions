# Write your MySQL query statement below
-- WITH CTE AS (
--     SELECT salary, 
--     RANK() OVER(ORDER BY SALARY DESC) AS currRank
--     FROM Employee
-- )

-- SELECT salary AS SecondHighestSalary 
-- FROM CTE 
-- WHERE currRank = 2

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(Salary) FROM Employee
)