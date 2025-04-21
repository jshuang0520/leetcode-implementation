-- https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
-- SELECT s.student_id, s.student_name, e.subject_name, COUNT(1) AS attended_exams
-- FROM Students AS s
-- LEFT JOIN Examinations AS e
--   ON s.student_id = e.student_id
-- GROUP BY (s.student_id, e.subject_name)

-- WITH group_exam_cnt AS (
--     SELECT e.student_id, e.subject_name, COUNT(1) AS attended_exams
--     FROM Examinations AS e
--     CROSS JOIN Subjects AS s
--       ON e.subject_name = s.subject_name
--     GROUP BY e.student_id, e.subject_name
-- )
-- SELECT s.student_id, s.student_name, t.subject_name, t.attended_exams
-- FROM Students AS s
-- LEFT JOIN group_exam_cnt AS t
--   ON s.student_id = t.student_id
-- ORDER BY (s.student_id) AND (t.subject_name)




-- WITH tbl_exams AS (
--     SELECT 
--       e.student_id, 
--       e.subject_name, 
--       COUNT(1) AS attended_exams
--     FROM Examinations AS e
--     CROSS JOIN Subjects AS s
--       ON e.subject_name = s.subject_name
--     GROUP BY student_id, subject_name
-- )  -- now it is incorrect (but we need this step to let each student has each subject), since it's corrupted: there are unexpected attended_exams now
-- -- thus, we use left join to fix this "corrupted data"
-- SELECT * FROM tbl_exams
-- -- SELECT 
-- --   s.student_id, 
-- --   s.student_name, 
-- --   e.subject_name, 
-- --   e.attended_exams
-- -- --   CASE 
-- -- --     WHEN e.attended_exams IS NOT NULL THEN e.attended_exams
-- -- --     ELSE 0
-- -- --   END AS attended_exams
-- -- FROM Students AS s
-- -- LEFT JOIN tbl_exams AS e
-- --   ON s.student_id = e.student_id
-- -- ORDER BY s.student_id, e.subject_name


-- SELECT 
--   e.student_id, 
--   s.student_name, 
--   e.subject_name, 
--   attended_exams
-- FROM Examinations AS e
-- LEFT JOIN Students AS s
--   ON e.student_id = s.student_id


SELECT 
  s.student_id, 
  s.student_name, 
  su.subject_name, 
  IFNULL(COUNT(e.subject_name), 0) AS attended_exams
FROM Students AS s
CROSS JOIN Subjects AS su
LEFT JOIN Examinations AS e
  ON s.student_id = e.student_id
  AND su.subject_name = e.subject_name  -- why need this?
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name