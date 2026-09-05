# Write your MySQL query statement below
# getting top 3 salaries

WITH CTE AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
    DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Department d
    INNER JOIN employee e
    ON d.id = e.departmentId 
)

SELECT Department, Employee, Salary 
FROM CTE 
WHERE salary_rank <= 3