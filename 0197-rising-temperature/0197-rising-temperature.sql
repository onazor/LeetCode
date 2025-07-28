# Write your MySQL query statement below
select p.id
from Weather p, Weather q
where dateDiff(p.recordDate, q.recordDate) = 1 and p.temperature > q.temperature;