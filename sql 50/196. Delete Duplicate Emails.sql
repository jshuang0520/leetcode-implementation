-- https://leetcode.com/problems/delete-duplicate-emails/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
-- SELECT MIN(id), email
-- FROM Person
-- GROUP BY email

-- SELECT id, email
-- FROM Person
-- GROUP BY email
-- HAVING MIN(id)

-- SELECT id, email
-- FROM Person
-- GROUP BY email


-- here is the mistake: Runtime Error: You can't specify target table for update in FROM clause (you cannot in-place update the table which is the same as the one specified in your FROM statement)
-- DELETE FROM Person
-- WHERE id NOT IN (
--     SELECT MIN(id) AS id
--     FROM Person
--     GROUP BY email
-- );  -- FIXME: Runtime Error: You can't specify target table 'Person' for update in FROM clause


-- correct answer
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
    ) AS keep  -- thus we make another temp table
);

-- correct answer
WITH tbl_non_duplicated_id AS (
    SELECT MIN(id) AS id
    FROM Person
    GROUP BY email
)
DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM tbl_non_duplicated_id -- thus we make another temp table
);