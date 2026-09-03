WITH CumulativeTable AS (
    SELECT person_name, SUM(Weight) OVER(ORDER BY turn) AS running_weight FROM Queue
)

SELECT person_name FROM CumulativeTable WHERE running_weight = (SELECT MAX(running_weight) FROM CumulativeTable WHERE running_weight <= 1000)