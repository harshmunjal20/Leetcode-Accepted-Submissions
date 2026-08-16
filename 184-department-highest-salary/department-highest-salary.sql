-- # Write your MySQL query statement below
-- WITH CTE AS (SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary FROM Employee e INNER JOIN Department d ON e.departmentId = d.id)

-- SELECT Department, Employee, MAX(Salary) AS Salary FROM CTE GROUP BY Department;
SELECT d.name AS Department, e.name AS Employee, temp.max_salary AS Salary FROM Employee e INNER JOIN Department d INNER JOIN (SELECT MAX(Salary) AS max_salary, departmentId FROM Employee GROUP BY departmentId) AS Temp ON e.departmentId = d.id AND d.id = temp.departmentId WHERE e.salary = temp.max_salary;

