-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50

-- # Write your MySQL query statement below
-- WITH total_usr AS (
--     SELECT COUNT(1) AS total_user_num
--     FROM Users
-- )
-- SELECT 
--   contest_id, 
--   ROUND((COUNT(1) / total_usr.total_user_num), 2) AS percentage
-- FROM Register AS r
-- GROUP BY contest_id
-- ORDER BY percentage DESC


SELECT 
  contest_id, 
--   ROUND((COUNT(1) / SELECT COUNT(1) FROM Users), 2)*100 AS percentage
  ROUND((COUNT(1) / (SELECT COUNT(1) FROM Users)) * 100, 2) AS percentage  # we need another set of brackets to do the subquery
FROM Register AS r
GROUP BY contest_id
-- ORDER BY (percentage DESC), (contest_id ASC)
ORDER BY percentage DESC, contest_id ASC

