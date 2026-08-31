# Write your MySQL query statement below
SELECT (SELECT Salary FROM (SELECT DISTINCT salary , DENSE_RANK() OVER(ORDER BY Salary DESC) AS rnk FROM Employee) AS T WHERE T.rnk = 2) AS SecondHighestSalary