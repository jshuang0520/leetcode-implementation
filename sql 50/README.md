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

> ❗ **Important:** the order of execution for each sql statement
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

## ⛄ WITH statement - create temp table(s)

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

for example:
```sql
SELECT id
FROM (
    SELECT 
        id, 
        temperature, 
        LAG(temperature) OVER (ORDER BY recordDate) AS lag_temp
    FROM Weather
) AS T
WHERE temperature > lag_temp;
```

---

## 📅 date operation

### filter dates 

- formula
```sql
-- method 1
WHERE ('YYYY-MM-DD' <= order_date) AND (order_date <= 'YYYY-MM-DD')
-- method 2
WHERE YEAR(order_date)='2020' AND MONTH(order_date)='02'
```

- example: [1327. List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/description)

```sql
WITH tbl_Feb_order AS (
    SELECT product_id, unit
    FROM Orders
    -- WHERE order_date BETWEEN 2020-02-01 AND 2020-02-30  -- incorrect format for dates, since single quotes are needed
    -- WHERE order_date BETWEEN '2020-02-01' AND '2020-02-28'  -- not so sure how many days are there in Feb, but those two dates are included: it is equivalent to WHERE ('2020-02-01' <= order_date) AND (order_date < '2020-03-01')

    WHERE YEAR(order_date)='2020' AND MONTH(order_date)='02'
    -- WHERE ('2020-02-01' <= order_date) AND (order_date < '2020-03-01')
)
SELECT 
  p.product_name, 
  SUM(o.unit) AS unit
FROM Products AS p
-- LEFT JOIN tbl_Feb_order AS o  -- wrong, LEFT JOIN will get an incorrect answer here
RIGHT JOIN tbl_Feb_order AS o
  ON p.product_id = o.product_id
GROUP BY product_name
HAVING unit >= 100
ORDER BY unit DESC
```


### DATEDIFF

To find "yesterday":

```sql
DATEDIFF(recordDate, previous_Date) = 1
```

```sql
DATEDIFF(date1, date2) = date1 - date2 (in days)
DATEDIFF('2025-04-19', date) = '2025-04-19' - date
```

Remember to wrap literal dates in single quotes.


### DATE_SUB

```sql
SELECT 
    date,
    DATE_SUB(date, INTERVAL 1 DAY) AS yesterday
FROM your_table;
```


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

## NULL handling

### syntax ("IS" NULL) ≠ ("=" NULL)

🤯 (WHERE col IS NULL) ≠ (WHERE col = NULL)

| Expression        | Result   |
|------------------|----------|
| bonus IS NULL     | ✅ TRUE/FALSE |
| bonus = NULL      | ❌ UNKNOWN |
| bonus != NULL     | ❌ UNKNOWN |
| bonus IS NOT NULL | ✅ TRUE/FALSE |


### 🛠️ Replacing NULLs

- IFNULL(query, the_value_to_fill_if_null)
```sql
IFNULL(SUM(p.price * u.units), 0) / NULLIF(SUM(u.units), 0)
```

- COALESCE(expr1, ..., exprN) returns the first non-NULL value
```sql
COALESCE(expr1, expr2, ..., exprN)
-- returns the first non-NULL value
-- e.g. COALESCE(bonus, 0)
```

---

## String operations

### regular expression (REGEXP Syntax)
🔣 Common REGEXP Symbols and Meanings

| Symbol        | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| `^`           | Start of string (**outside** brackets)                                  |
| `[^...]`      | NOT (negation) **inside** a character set `[^...]`                      |
| `$`           | End of string                                                           |
| `[]`          | Character set — match **one** character from the set                    |
| `[^...]`      | Negated character set — match one character **not** in the set          |
| `\|`           | OR — used between alternatives                                          |
| `()`          | Grouping pattern logic                                                  |
| `?`           | Match **zero or one (0 or 1)** of the preceding character (optional)             |
| `*`           | Match **zero or more (appearance ≥ 0)** of the preceding character or group              |
| `+`           | Match **one or more (appearance ≥ 1)** of the preceding character or group               |
| `.`           | Match **any single character** except newline (`\n`)                  |

🧠 Key Differences Between Similar Patterns

- `*` = (appearance ≥ 0), can match nothing
- `+` = (appearance ≥ 1), must match at least once

| Pattern     | Meaning                                      | ✅ Matches        | ❌ Doesn’t Match    |
|-------------|----------------------------------------------|----------------|------------------|
| `a?`        | 0 or 1 `a`                                   | `""`, `a`       | `aa`, `b`        |
| `a*`        | 0 or more `a`                                | `""`, `a`, `aaa`| `b`              |
| `a+`        | 1 or more `a`                                | `a`, `aa`       | `""`, `b`        |
| `a.`        | `a` followed by any one character            | `ab`, `a1`      | `a`              |
| `a.*b`      | `a`, anything in between, then `b`           | `ab`, `axxb`    | `b`, `a`         |


Pattern | Input | Match? | Why
|-------|-------|-------|-------|
a* | "" | ✅ | 0 as is okay
a* | aaa | ✅ | 3 as
a+ | "" | ❌ | Needs at least one a
a+ | aa | ✅ | Two as is fine

#### Escape symbol in `SQL doing REGEXP`: use double back slahes `\\` e.g. `\\.`

- Escape the dot if you want a literal period

```sql
REGEXP 'example\\.com'
```
✅ Matches `example.com`  
❌ Doesn't match `exampleXcom`

- MySQL interprets `\.` as an escaped dot in the SQL string, not in regex
❌ wrong way in sql doing REGEXP
```sql
SELECT 'example.com' REGEXP 'example\.com';  -- ❌ Likely syntax error or wrong match
```

✅ Example in MySQL:

```sql
SELECT 'example.com' REGEXP 'example\\.com';  -- ✅ Matches
```
Here’s what’s happening:
- `example\\.com` → MySQL string parser turns this into → `example\.com`
- The regex engine then sees → `\.` → which matches a literal `.`


Context | Regex for literal dot | Notes
|-------|-------|-------|
MySQL | `example\\.com` | Use double backslash
Python regex | `r'example\.com'` | Use raw string or escape it

- Example: [1527. Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/description)

```sql
SELECT patient_id, patient_name, conditions
FROM Patients
-- WHERE conditions LIKE '%DIAB1%'  -- this is wrong, since it will match 'ABCDIAB10000' and that not we want
WHERE conditions REGEXP '(^| )DIAB1[A-Z0-9]*( |$)'
```

#### ✅ Example 1: Match "DIAB1" token with proper boundaries

```sql
WHERE conditions REGEXP '(^| )DIAB1[^ ]*($| )'
```

- `(^| )` — beginning of string or a space
- `DIAB1` — must literally start with "DIAB1"
- `[^ ]*` — zero or more non-space characters (the rest of the code)
  - that is to say, `DIAB1[^ ]*` means `DIAB1` followed by any non-space characters 
- `($| )` — must be followed by end-of-string or a space

❌ Does NOT match:
- `ASDIAB1BB`  → embedded in another word
- `0DIAB1A`    → no boundary before `DIAB1`


🧠 Bonus: Case-insensitive matching

```sql
WHERE LOWER(conditions) REGEXP '(^| )diab1[^ ]*($| )'
```

or using collation (MySQL 8+):

```sql
WHERE conditions COLLATE utf8mb4_general_ci REGEXP '(^| )DIAB1[^ ]*($| )'
```

🧪 More Examples

| REGEXP Expression                     | ✅ Matches                                     |
|--------------------------------------|---------------------------------------------|
| `^abc`                               | Strings that **start with** `abc`           |
| `abc$`                               | Strings that **end with** `abc`             |
| `a|b`                                | Strings that contain `a` **or** `b`         |
| `[ABC]`                              | One character that is either A, B, or C     |
| `[^ABC]`                             | One character that is **not** A, B, or C    |
| `DIAB1[^ ]*`                         | `DIAB1` followed by any non-space characters |

### concat strings

- example: [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/description)

- GROUP_CONCAT to get them sorted lexicographically, and then concat those strings
```sql
GROUP_CONCAT(col ORDER BY col ASC SEPARATOR ',') AS new_column
```

```sql
SELECT 
  sell_date,
  COUNT(DISTINCT(product)) AS num_sold,
  GROUP_CONCAT(DISTINCT(product) ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
```

### getting substrings

- example: [1667. Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description/)

#### SUBSTRING
✅ SUBSTRING(str, start, length)
```sql
SUBSTRING(string, start_position, [length])
```
- if the last argument, length, is not specified, select it till the end

```sql
SELECT SUBSTRING('HelloWorld', 2, 3);  -- Result: 'ell'
-- Starts at position 2 → 'e', and takes 3 characters → 'e', 'l', 'l'


SELECT SUBSTRING('HelloWorld', 6);     -- Result: 'World'
-- Starts at position 6 → returns the rest of the string
```

```sql
SELECT 
  user_id, 
  CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id
```

#### LEFT
✅ LEFT(str, length)
```sql
LEFT(string, n)
```
- Starts from position 1 (the beginning of the string)
- Returns n characters

```sql
SELECT LEFT('HelloWorld', 5);  -- Result: 'Hello'
```

### alter alphabet's cases

- UPPER()
- LOWER()

### keyword matching in a certain pattern

🔍 Finding Keywords in a VARCHAR Column

- ✅ `NOT LIKE '%math%'` — partial match  
- ✅ `NOT IN ('math')` — exact match  
- ✅ Add `IS NOT NULL` if needed

```sql
WHERE column_name NOT LIKE '%math%' AND column_name IS NOT NULL
```

---

## Math operations

📉 Select odd-numbered IDs

```sql
WHERE id % 2 = 1
```

---

## apply a scalar result into other queries

### 📤 1. Using scalar subqueries (when JOIN not possible)

#### **Option 1**: scalar subquery in SELECT

```sql
SELECT
  contest_id,
  ROUND(COUNT(*) / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id;
```

#### **Option 2**: CROSS JOIN a one-row (scalar result) CTE

```sql
WITH total_usr AS (
  SELECT COUNT(*) AS total_user_num FROM Users
)
SELECT r.contest_id, COUNT(*) / t.total_user_num AS percentage
FROM Register AS r
CROSS JOIN total_usr AS t
GROUP BY r.contest_id;
```

### 📤 2. make use of [variables](#variables-in-mysql)

---

## Variables in MySQL

🧠 Variables in MySQL
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

| Property | Explanation                                                                 |
|----------|-----------------------------------------------------------------------------|
| Local?   | ❌ No — it's not block-scoped (like inside a procedure or a script section) |
| Global?  | ❌ No — it doesn’t affect other sessions                                     |
| Session? | ✅ Yes — persists in your current session only                               |


⚠️ Impacts & Cautions

- Safe in simple scripts: You can use them in scripts (e.g., in MySQL Workbench, or CLI) to store intermediate values.
- Not thread-safe: In multi-user apps (e.g., web apps), avoid relying on @ variables — use local variables inside procedures or transactions instead.
- Won’t persist if you disconnect: Once you close your session/connection, the variable is gone.


### local variable (only in "stored procedures", "triggers", and "BEGIN...END blocks"):

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
📤 how to concat results vertically (vertical concatenation)?
✅ Use UNION or UNION ALL

### Example Input and Output for Vertical Concatenation

for example,

Input

Given Result 1 from a query,

| id       |
|----------|
| 1        |
| 2        |

and Result 2 from another query,

| id       |
|----------|
| 3        |

how can I concat these two result sets vertically to get the following answer?

Expected Output

| id            |
|---------------|
| 1             |
| 2             |
| 3             |

Example:

```sql
SELECT id FROM table1
UNION ALL
SELECT id FROM table2
ORDER BY id;
```

- conclusion
  - ✅ `UNION` → slower, removes duplicates, not sorted (unless you add ORDER BY)
  - ✅ `UNION ALL` → faster, returns all rows


### UNION
🔹 If you want unique values only (no duplicates):
```sql
SELECT id FROM table1
UNION
SELECT id FROM table2;
```

- This removes duplicates.
- Sort order is not guaranteed unless you add ORDER BY.

### UNION ALL
🔹 If you want to keep all values including duplicates:

```sql
SELECT id FROM table1
UNION ALL
SELECT id FROM table2;
```

- Faster than UNION (no deduplication).
- Returns all rows.


## multiple condition handling - (CASE ((WHEN condition THEN value)*N (ELSE value)) END) AS new_column

- structure

```sql
SELECT
  CASE 
    WHEN (condition) THEN value
    WHEN (condition) THEN value
    ELSE value
  END AS a_new_column
FROM a_table
```

```sql
SELECT 
  x, y, z,
  CASE 
    WHEN (x + y > z AND y + z > x AND x + z > y) THEN 'Yes'
    ELSE 'No'
  END AS triangle
FROM Triangle;
```


```sql
SELECT 
  x, y, z,
  CASE 
    WHEN (x + y > z AND y + z > x AND x + z > y) THEN 'Yes'
    ELSE 'No'
  END AS triangle
FROM Triangle;
```


## SELF JOIN

- example: [1978. Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/)

- let's break it down

```sql
SELECT *
FROM Employees AS e1
LEFT JOIN Employees AS e2
  ON e1.manager_id = e2.employee_id
```

```
Since we LEFT JOIN ON:

           e1.manager_id             =           e2.employee_id
           ─────────────                         ─────────────-

```

the table should be interpreted like this:

| e1.employee_id | e1.name    | e1.manager_id | e1.salary | e2.employee_id | e2.name    | e2.manager_id | e2.salary |
| ----------- | --------- | ---------- | ------ | ----------- | ------- | ---------- | ------ |

| employee_id | name      | manager_id | salary | employee_id | name    | manager_id | salary |
| ----------- | --------- | ---------- | ------ | ----------- | ------- | ---------- | ------ |
| 3           | Mila      | 9          | 60301  | 9           | Mikaela | null       | 50937  |
| 12          | Antonella | null       | 31000  | null        | null    | null       | null   |
| 13          | Emery     | null       | 67084  | null        | null    | null       | null   |
| 1           | Kalel     | 11         | 21241  | 11          | Joziah  | 6          | 28485  |
| 9           | Mikaela   | null       | 50937  | null        | null    | null       | null   |
| 11          | Joziah    | 6          | 28485  | null        | null    | null       | null   |


let's highlight the following people

and further check who's manager has left: for those (e1.manager_id IS NOT NULL) AND (e2.employee_id IS NULL)

```
Since we LEFT JOIN ON:

           e1.manager_id             =           e2.employee_id
           ─────────────                         ─────────────-

```

| employee_id | name      | manager_id | salary | employee_id | name    | manager_id | salary |
| ----------- | --------- | ---------- | ------ | ----------- | ------- | ---------- | ------ |
| 1           | Kalel     | 11         | 21241  | 11          | Joziah  | 6          | 28485  |
| 11          | Joziah    | 6          | 28485  | null        | null    | null       | null   |


```sql
SELECT e1.employee_id
FROM Employees AS e1
LEFT JOIN Employees AS e2
  ON e1.manager_id = e2.employee_id
WHERE (e1.salary < 30000)
  AND (e1.manager_id IS NOT NULL)
  AND (e2.employee_id IS NULL)
ORDER BY employee_id
```

## Drop Duplicates: in-place DELETE

- note. you cannot in-place update the table which is the same as the one specified in your FROM statement
- ❌ wrong query
```sql
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id) AS id
    FROM Person
    GROUP BY email
);  -- Runtime Error: You can't specify target table 'Person' for update in FROM clause
```
since following error will occur
```Runtime Error: You can't specify target table 'Person' for update in FROM clause```


### ✅ solution: create another temp table
```sql
WITH tbl_non_duplicated_id AS (
    SELECT MIN(id) AS id
    FROM Person
    GROUP BY email
)  -- thus we make another temp table
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM tbl_non_duplicated_id -- and make use of that temp table here
);
```