# Write your MySQL query statement below
SELECT id, CASE 
    WHEN id % 2 = 1 THEN COALESCE((SELECT Student FROM Seat s2 WHERE s2.id = s1.id + 1), s1.student)
    ELSE (SELECT student FROM Seat s3 WHERE s3.id = s1.id - 1)
    END AS student
FROM Seat s1
ORDER BY id 
