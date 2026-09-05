# Write your MySQL query statement below
-- WITH CTE AS (
--     SELECT salary, 
--     RANK() OVER(ORDER BY SALARY DESC) AS currRank
--     FROM Employee
-- )

-- SELECT salary AS SecondHighestSalary 
-- FROM CTE 
-- WHERE currRank = 2

SELECT  (SELECT DISTINCT salary AS SecondHighestSalary
FROM Employee e1
WHERE 1 = (
    SELECT COUNT(DISTINCT Salary) 
    FROM Employee e2
    WHERE e2.salary > e1.salary
)) AS SecondHighestSalary