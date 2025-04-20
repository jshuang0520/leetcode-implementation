https://leetcode.com/problems/rising-temperature/solutions/5353703/easiest-basic-sql-solution-4-approaches-beginner-level-to-advance/?envType=study-plan-v2&envId=top-sql-50

Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).


Intuition

The problem requires us to find all the dates with higher temperatures compared to their previous dates (yesterday). To solve this, we need to compare each dates temperature with the temperature of the previous date.

Approach

To solve the problem, we can use the following approach:

Join the Weather table with itself, denoting the first occurrence as w1 and the second occurrence as w2.
Compare the dates of w1 and w2 using the DATEDIFF() function to check if they are consecutive days (with a difference of 1 day).
Add a condition in the WHERE clause to select the rows where the temperature of w1 is greater than the temperature of w2.
Select the id of w1 as the result.
The SQL query for the above approach is as follows:

# method 1
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperatur

# method 2
SELECT W1.id
FROM Weather W1
JOIN Weather W2
ON W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 DAY)
WHERE W1.temperature > W2.temperature;

# method 3
-- Create a CTE to calculate the previous day\'s temperature and date
WITH q1 AS (
  SELECT 
      *,
      LAG(temperature) OVER (ORDER BY recordDate) AS previous_day_temperature,
      LAG(recordDate) OVER (ORDER BY recordDate) AS previous_Date
  FROM Weather
)

-- Select the IDs where the temperature is higher than the previous day
-- and the previous day exists (difference is exactly 1 day)
SELECT id
FROM q1
WHERE temperature > previous_day_temperature
AND DATEDIFF(recordDate, previous_Date) = 1;



# the following is a wrong answer because:
-- SELECT T.id
-- FROM (SELECT id, LAG(temperature) OVER(ORDER BY recordDate) AS lag_temp
-- FROM Weather
-- WHERE lag_temp > temperature  # Unknown column 'lag_temp' in 'where clause'
-- ) AS T
-- =====================
Long Answer: SQL Query Processing Order
SQL does not execute clauses top-down. It uses a specific logical processing order, and here’s a simplified version of it:
1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
