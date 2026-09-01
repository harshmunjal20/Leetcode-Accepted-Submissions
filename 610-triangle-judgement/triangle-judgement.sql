# Write your MySQL query statement below
SELECT x, y, z, (if (x + y <= z OR x + z <= y OR y + z <= x, "No", "Yes")) AS "triangle" FROM Triangle