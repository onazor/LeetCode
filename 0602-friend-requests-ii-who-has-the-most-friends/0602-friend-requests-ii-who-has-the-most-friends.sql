# Write your MySQL query statement below
WITH all_people as (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
)
SELECT id, COUNT(*) AS num
FROM all_people
GROUP BY id
ORDER BY num DESC
LIMIT 1;