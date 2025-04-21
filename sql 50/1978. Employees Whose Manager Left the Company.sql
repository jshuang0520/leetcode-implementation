-- https://leetcode.com/problems/employees-whose-manager-left-the-company/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below

-- self join

-- let's break it down
SELECT *
FROM Employees AS e1
LEFT JOIN Employees AS e2
  ON e1.manager_id = e2.employee_id
```markdown
since we LEFT JOIN ON    e1.manager_id          =                 e2.employee_id
                                                |
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

since we LEFT JOIN ON    e1.manager_id          =                 e2.employee_id
                                                |
| employee_id | name      | manager_id | salary | employee_id | name    | manager_id | salary |
| ----------- | --------- | ---------- | ------ | ----------- | ------- | ---------- | ------ |
| 1           | Kalel     | 11         | 21241  | 11          | Joziah  | 6          | 28485  |
| 11          | Joziah    | 6          | 28485  | null        | null    | null       | null   |
```

SELECT e1.employee_id
FROM Employees AS e1
LEFT JOIN Employees AS e2
  ON e1.manager_id = e2.employee_id
WHERE (e1.salary < 30000)
  AND (e1.manager_id IS NOT NULL)
  AND (e2.employee_id IS NULL)
ORDER BY employee_id

-- create temp table
WITH

-- subquery
SELECT employee_id
FROM Employees
WHERE (salary < 30000) 
  AND (manager_id NOT IN (
    SELECT DISTINCT(employee_id)
    FROM Employees
    )
  )
ORDER BY employee_id