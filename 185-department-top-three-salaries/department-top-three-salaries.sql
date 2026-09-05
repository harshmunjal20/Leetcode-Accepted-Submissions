# Write your MySQL query statement below
# getting top 3 salaries

WITH ranked_salaries AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
    DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee e
    INNER JOIN Department d
    ON e.departmentId = d.id
)

SELECT Department, Employee, Salary 
FROM ranked_salaries
WHERE salary_rank <= 3

-- top 3 in overall
-- SELECT salary FROM (
--     SELECT salary, id, 
--     DENSE_RANK() OVER(ORDER BY Salary DESC) AS salary_rank
--     FROM Department
-- ) AS salary_ranks_table
-- WHERE salary_rank <= 3