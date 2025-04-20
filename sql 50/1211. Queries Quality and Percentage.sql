-- https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
-- SET @total_users = (SELECT COUNT(*) FROM Users);
WITH poor_query_tbl AS (
    SELECT query_name, COUNT(1) AS poor_query_num
    FROM Queries
    WHERE rating < 3
    GROUP BY query_name
), query_quality_tbl AS (
    SELECT 
      query_name, 
      COUNT(1) AS query_num,
      ROUND((SUM(rating / position) / COUNT(1)), 2) AS quality
    FROM Queries
    GROUP BY query_name
)

SELECT 
  q.query_name, 
  quality, 
--   ROUND((p.poor_query_num / q.query_num) * 100, 2) AS poor_query_percentage
  IFNULL(ROUND((p.poor_query_num / q.query_num) * 100, 2), 0) AS poor_query_percentage
FROM query_quality_tbl AS q
LEFT JOIN poor_query_tbl AS p
  ON q.query_name = p.query_name
