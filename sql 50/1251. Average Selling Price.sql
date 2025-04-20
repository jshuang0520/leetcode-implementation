-- https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50

-- # Write your MySQL query statement below
-- SELECT p.product_id, ROUND((SUM(p.price * u.units) / SUM(u.units)), 2) AS average_price
-- FROM Prices AS p
-- LEFT JOIN UnitsSold AS u
-- ON (p.product_id = u.product_id)
-- AND (u.purchase_date BETWEEN p.start_date AND p.end_date)
-- GROUP BY p.product_id

-- Output
-- | product_id | average_price |
-- | ---------- | ------------- |
-- | 1          | null          |
-- | 2          | null          |

-- Expected
-- | product_id | average_price |
-- | ---------- | ------------- |
-- | 1          | 0             |
-- | 2          | 0             |



# Write your MySQL query statement below
-- SELECT p.product_id, ROUND((SUM(p.price * u.units) / SUM(u.units)), 2) AS average_price
SELECT 
  p.product_id, 
  ROUND(IFNULL((SUM(p.price * u.units) / SUM(u.units)), 0), 2) AS average_price
FROM Prices AS p
LEFT JOIN UnitsSold AS u
ON (p.product_id = u.product_id)
AND (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY p.product_id
