# ✅ Full Logical Processing Order (with JOINs included)

Here's a more complete version of SQL's logical processing steps:

1. FROM  
2. JOIN / ON  
3. WHERE  
4. GROUP BY  
5. HAVING  
6. SELECT  
7. DISTINCT  
8. ORDER BY  
9. LIMIT / OFFSET

```sql
6. SELECT
7. DISTINCT

1. FROM
2. JOIN / ON
3. WHERE

4. GROUP BY
5. HAVING

8. ORDER BY
9. LIMIT / OFFSET
```

---

## ⛄ WITH statement - temp table

❌ No, you cannot use multiple separate WITH statements in a single SQL query  
✅ Instead, you should combine them into one WITH clause, separating multiple CTEs with commas:

```sql
WITH tbl_start AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'start'
), tbl_end AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'end'
)
```

---

## 🔀 LAG function

```sql
LAG(column_1) OVER (ORDER BY column_2) AS col_alias
```

---

## 📅 DATEDIFF

To find "yesterday":

```sql
DATEDIFF(recordDate, previous_Date) = 1
```

```sql
DATEDIFF(date1, date2) = date1 - date2 (in days)
DATEDIFF('2025-04-19', date) = '2025-04-19' - date
```

Remember to wrap literal dates in single quotes.

---

## 🤯 (bonus IS NULL) ≠ (bonus = NULL)

| Expression        | Result   |
|------------------|----------|
| bonus IS NULL     | ✅ TRUE/FALSE |
| bonus = NULL      | ❌ UNKNOWN |
| bonus != NULL     | ❌ UNKNOWN |
| bonus IS NOT NULL | ✅ TRUE/FALSE |

---

## 🔍 Finding Keywords in a VARCHAR Column

- ✅ `NOT LIKE '%math%'` — partial match  
- ✅ `NOT IN ('math')` — exact match  
- ✅ Add `IS NOT NULL` if needed

```sql
WHERE column_name NOT LIKE '%math%' AND column_name IS NOT NULL
```

---

## 📉 Select odd-numbered IDs

```sql
WHERE id % 2 = 1
```

---

## 📅 Join with a time period

```sql
JOIN Prices AS p
  ON u.product_id = p.product_id
 AND u.purchase_date BETWEEN p.start_date AND p.end_date
```

---

## 🧠 Why Use ON + AND in JOIN?

Think of `ON` as the **join's WHERE clause** — it defines how to match rows:

```sql
JOIN table2
  ON table1.id = table2.id
 AND table1.date BETWEEN ...
```

---

## 🛠️ Replacing NULLs

```sql
IFNULL(SUM(p.price * u.units), 0) / NULLIF(SUM(u.units), 0)

COALESCE(expr1, expr2, ..., exprN)
-- returns the first non-NULL value
-- e.g. COALESCE(bonus, 0)
```

---

## 📤 when the query result is a scalar, how to bring it out?

Using scalar subqueries (when JOIN not possible)

**Option 1**: scalar subquery in SELECT

```sql
SELECT
  contest_id,
  ROUND(COUNT(*) / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id;
```

**Option 2**: CROSS JOIN a one-row (scalar result) CTE

```sql
WITH total_usr AS (
  SELECT COUNT(*) AS total_user_num FROM Users
)
SELECT r.contest_id, COUNT(*) / t.total_user_num AS percentage
FROM Register AS r
CROSS JOIN total_usr AS t
GROUP BY r.contest_id;
```

---

## 🧠 Variables in MySQL

- session variable
- local variable
- global variable

| Type       | Syntax                  | Scope     | Persistence         | Use Case                        |
|------------|-------------------------|-----------|----------------------|----------------------------------|
| `@var`     | `SET @var = value`      | Session   | Until disconnect     | Ad-hoc or scripting              |
| `DECLARE`  | In BEGIN...END block    | Local     | Procedure lifetime   | Stored procedures, triggers     |

### session variable: @

✅ In MySQL, you can declare and use variables like this:
🔹 1. Assigning a value to a variable:
```sql
SET @total_users = (SELECT COUNT(*) FROM Users);
Now @total_users holds the count of users.
```

🔐 Is @x Global or Local?

Property	Explanation
Local?	❌ No — it's not block-scoped (like inside a procedure or a script section)
Global?	❌ No — it doesn’t affect other sessions
Session?	✅ Yes — persists in your current session only

⚠️ Impacts & Cautions

Safe in simple scripts: You can use them in scripts (e.g., in MySQL Workbench, or CLI) to store intermediate values.
Not thread-safe: In multi-user apps (e.g., web apps), avoid relying on @ variables — use local variables inside procedures or transactions instead.
Won’t persist if you disconnect: Once you close your session/connection, the variable is gone.


### local variable (only in stored procedures):

```sql
DECLARE total_users INT;
SET total_users = (SELECT COUNT(*) FROM Users);
```

But this only works inside:
- Stored procedures
- Triggers
- BEGIN...END blocks

---

## 🔗 Vertical Concatenation (UNION)

Example:

```sql
SELECT id FROM table1
UNION ALL
SELECT id FROM table2
ORDER BY id;
```

- ✅ `UNION` → removes duplicates; sort order is not guaranteed unless you add ORDER BY
- ✅ `UNION ALL` → returns all rows (faster)
