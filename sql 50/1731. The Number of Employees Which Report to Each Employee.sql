-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
WITH tbl_manager_id AS (
    -- SELECT employee_id, name
    -- FROM Employees
    -- WHERE reports_to IS NULL

    -- SELECT employee_id, name
    -- FROM (SELECT DISTINCT(reports_to) FROM Employees) AS T

    SELECT T.reports_to
    FROM (SELECT DISTINCT(reports_to) FROM Employees) AS T
), tbl_managers AS (
    SELECT DISTINCT employee_id, name
    FROM Employees AS e
    RIGHT JOIN tbl_manager_id AS m
      ON e.employee_id = m.reports_to

), tbl_reports_to AS (
    SELECT 
      reports_to,
      COUNT(1) AS reports_count,
      ROUND(AVG(age)) AS average_age
    FROM Employees
    GROUP BY reports_to
)
SELECT m.employee_id, m.name, r.reports_count, r.average_age
FROM tbl_managers AS m
-- LEFT JOIN tbl_reports_to AS r
INNER JOIN tbl_reports_to AS r
  ON m.employee_id = r.reports_to
ORDER BY employee_id ASC