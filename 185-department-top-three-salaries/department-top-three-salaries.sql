# Write your MySQL query statement below
WITH ranked_salaries AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, 
    DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY Salary DESC) AS salary_rank
    FROM Employee e
    INNER JOIN Department d
    ON e.departmentId = d.id
)

SELECT Department, Employee, Salary 
FROM ranked_salaries
WHERE salary_rank <= 3