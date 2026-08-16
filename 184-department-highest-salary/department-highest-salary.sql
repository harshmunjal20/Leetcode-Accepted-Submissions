# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, Temp.Salary FROM Employee e
INNER JOIN Department d INNER JOIN
(SELECT departmentId, MAX(Salary) AS salary FROM Employee GROUP BY departmentId) AS Temp
ON e.departmentId = d.id AND d.id = temp.departmentId AND e.salary = temp.salary;