# Write your MySQL query statement below
SELECT (SELECT DISTINCT Salary FROM Employee e1 WHERE 2 = (SELECT COUNT(DISTINCT Salary) FROM Employee e2 WHERE e2.salary >= e1.salary)) AS SecondHighestSalary