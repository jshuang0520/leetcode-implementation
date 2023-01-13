--Beats 78.89%
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*)>=3;

--Time taken - 00 : 10 : 03
----Beats 18.25%
--TODO: there's no need to select it again (subquery is redundant)
--SELECT t.actor_id, t.director_id
--FROM (
--    SELECT actor_id, director_id, COUNT(*)
--    FROM ActorDirector
--    GROUP BY actor_id, director_id
--    HAVING COUNT(*) >= 3
--) AS t


--FIXME: 4 / 12 testcases passed: because "" should not be added to express column names: e.g., "actor_id", "director_id"
--SELECT t.actor_id, t.director_id
--FROM (
--    SELECT actor_id, director_id, COUNT(*)
--    FROM ActorDirector
--    GROUP BY "actor_id", "director_id"
--    HAVING COUNT(*) >= 3
--) AS t
