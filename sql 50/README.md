# ✅ Full Logical Processing Order (with JOINs included)
Here’s a more complete version of SQL’s logical processing steps:

1. FROM
2. JOIN / ON
3. WHERE

4. GROUP BY
5. HAVING

6. SELECT

7. DISTINCT

8. ORDER BY

9. LIMIT / OFFSET


"""
6. SELECT
7. DISTINCT

1. FROM
2. JOIN / ON
3. WHERE

4. GROUP BY
5. HAVING

8. ORDER BY
9. LIMIT / OFFSET
"""


# WITH statement - temp table
❌ No, you cannot use multiple separate WITH statements in a single SQL query
✅ Instead, you should combine them into one WITH clause, separating multiple CTEs with commas:
WITH tbl_start AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'start'
), tbl_end AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'end'
)


# LAG function
LAG(column_1) OVER (ORDER BY column_2) AS col_alias


# DATEDIFF
-- to find "yesterday": DATEDIFF(...) = 1
DATEDIFF(recordDate, previous_Date) = 1

DATEDIFF(date1, date2) = date1 - date2 (in days)
DATEDIFF('2025-04-19', date) = '2025-04-19' - date (in days)  # we need the single quote for the date itself

# (bonus IS NULL) ≠ (bonus = NULL)
🤯 Why is that?
✅ bonus IS NULL
This is the correct way to check for a NULL value.

❌ bonus = NULL
This always results in UNKNOWN, not TRUE, even if bonus is NULL.

🔍 Here's why — Three-Valued Logic in SQL
SQL uses three-valued logic:

- TRUE

- FALSE

- UNKNOWN


✅ Correct Comparisons with NULL

Expression	Result
- bonus IS NULL	TRUE / FALSE

- bonus = NULL	UNKNOWN

- bonus != NULL	UNKNOWN

- bonus IS NOT NULL	TRUE / FALSE

# how to find if a keyword is not in a column which its schema is VARCHAR?
✅ 1. NOT LIKE for partial match
✅ 2. NOT IN for exact match
✅ 3. Use IS NULL to cover nulls too
WHERE column_name NOT LIKE '%math%' AND column_name IS NOT NULL

# how to select an odd-number id?
WHERE id % 2 = 1

# if given a date, how should I join this row to the corresponding time period?

JOIN Prices AS p
  ON u.product_id = p.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date


🔹 Why Use ON + AND in JOIN?
When you're doing a JOIN, the ON clause defines how the two tables relate to each other — that is, the condition for matching rows.



🔍 Analogy: ON is the join's WHERE clause
It helps to think of this:

ON = "only combine rows from both tables when this condition is true"

The AND just lets you add more conditions to the same JOIN.


# Methods for Replacing NULLs

✅ IFNULL(SUM(p.price * u.units), 0) / NULLIF(SUM(u.units), 0), 

✅ COALESCE(expr1, expr2, ..., exprN) returns the first non-NULL value from the list of expressions.
e.g., COALESCE(bonus, 0)


# when the query result is a scalar, how to bring it out?
Q: I would like to bring a single value, total_user_num, for further use, and there is no chance to do the join operation, what should I do to successfully use this value in the future query?

✅ Option 1: Use a Scalar Subquery (Cleanest for Your Case)

✅ Option 2: Use a CROSS JOIN (only if you must use a CTE)
🔹 CROSS JOIN adds the scalar total_user_num to every row — no matching needed.

# notes to SELECT a subquery
SELECT 
  contest_id, 
--   ROUND((COUNT(1) / SELECT COUNT(1) FROM Users) * 100, 2)*100 AS percentage
-- # we need another set of brackets to do the subquery
  ROUND((COUNT(1) / (SELECT COUNT(1) FROM Users)) * 100, 2) AS percentage  

# notes to ORDER BY
-- ORDER BY (percentage DESC), (contest_id ASC)
ORDER BY percentage DESC, contest_id ASC


# types of variables

Variable | Syntax | Scope | Persistence | Use Case
@var | @var = val | Session | Until disconnect | Temp value in session
DECLARE var | Inside block | Local | Limited to the block | Stored procedures/functions

## session variable: @

✅ In MySQL, you can declare and use variables like this:
🔹 1. Assigning a value to a variable:
SET @total_users = (SELECT COUNT(*) FROM Users);
Now @total_users holds the count of users.

🔐 Is @x Global or Local?

Property	Explanation
Local?	❌ No — it's not block-scoped (like inside a procedure or a script section)
Global?	❌ No — it doesn’t affect other sessions
Session?	✅ Yes — persists in your current session only

⚠️ Impacts & Cautions

Safe in simple scripts: You can use them in scripts (e.g., in MySQL Workbench, or CLI) to store intermediate values.
Not thread-safe: In multi-user apps (e.g., web apps), avoid relying on @ variables — use local variables inside procedures or transactions instead.
Won’t persist if you disconnect: Once you close your session/connection, the variable is gone.


## local variable (only in stored procedures):

DECLARE total_users INT;
SET total_users = (SELECT COUNT(*) FROM Users);

But this only works inside:
- Stored procedures
- Triggers
- BEGIN...END blocks

# how to concat results vertically (vertical concatenation)?

e.g. 

result 1:

id
--
1
2

result 2:

id
--
3

after concat:

final result:

id
--
1
2
3

✅ Use UNION or UNION ALL
🔹 If you want unique values only (no duplicates):
SELECT id FROM table1
UNION
SELECT id FROM table2;

- This removes duplicates.
- Sort order is not guaranteed unless you add ORDER BY.

🔹 If you want to keep all values including duplicates:

SELECT id FROM table1
UNION ALL
SELECT id FROM table2;

- Faster than UNION (no deduplication).
- Returns all rows.
