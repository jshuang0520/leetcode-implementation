-- https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below

-- ❌ No, you cannot use multiple separate WITH statements in a single SQL query like this:
-- WITH tbl_start AS (
--     SELECT *
--     FROM Activity
--     WHERE activity_type = 'start'
-- )
-- WITH tbl_end AS (
--     SELECT *
--     FROM Activity
--     WHERE activity_type = 'end'
-- )

-- ✅ Instead, you should combine them into one WITH clause, separating multiple CTEs with commas:
WITH tbl_start AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'start'
), tbl_end AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'end'
)
SELECT s.machine_id, ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM tbl_start AS s
LEFT JOIN tbl_end AS e
  ON (s.machine_id = e.machine_id) AND (s.process_id = e.process_id)
GROUP BY s.machine_id