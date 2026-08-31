# Write your MySQL query statement below
SELECT (SELECT Salary FROM (SELECT DISTINCT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) AS rnk FROM Employee) AS t WHERE t.rnk = 2) AS SecondHighestSalary