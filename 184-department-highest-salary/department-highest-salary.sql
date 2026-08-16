# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary FROM Employee e INNER JOIN Department d ON e.departmentId = d.id WHERE (e.departmentId, salary) IN (
SELECT departmentId, MAX(Salary) FROM employee GROUP BY departmentId);