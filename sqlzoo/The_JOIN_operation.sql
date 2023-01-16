
-- https://sqlzoo.net/wiki/The_JOIN_operation

--1
SELECT matchid, player
FROM goal t1
LEFT JOIN eteam t2
  ON t1.teamid = t2.id
WHERE t1.teamid = 'GER'

--notes. WHERE 要在 JOIN 之後
--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'LEFT JOIN eteam t2 ON t1.teamid = t2.id' at line 4
--SELECT matchid, player
--FROM goal t1
--WHERE t1.teamid = 'GER'
--LEFT JOIN eteam t2
--  ON t1.teamid = t2.id


--2
SELECT id, stadium, team1, team2
FROM game t1
WHERE id = 1012

--3
SELECT player, teamid, stadium, mdate
FROM goal t1
LEFT JOIN game t2
  ON t1.matchid = t2.id
WHERE t1.teamid = 'Ger'

--4
SELECT t2.team1, t2.team2, t1.player
FROM goal t1
LEFT JOIN game t2
  ON t1.matchid = t2.id
WHERE player LIKE 'Mario%'

--5
SELECT t1.player, teamid, coach, gtime
FROM goal t1
LEFT JOIN eteam t2
  ON t1.teamid = t2.id
WHERE t1. gtime <= 10

--6
--List the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.
SELECT mdate, t2.teamname
FROM game t1
LEFT JOIN eteam t2
  ON t1.team1 = t2.id  -- notice. statement "ON t2.team2 = t2.id" would be wrong because the question asked 'Fernando Santos' was the "team1" coach.
WHERE t2.coach = 'Fernando Santos'

--7
SELECT t1.player
FROM goal t1
LEFT JOIN game t2
  ON t1.matchid = t2.id
WHERE t2.stadium = 'National Stadium, Warsaw'


--8
--The example query shows all goals scored in the Germany-Greece quarterfinal.
--Instead show the name of all players who scored a goal against Germany.
--
--HINT
--Select goals scored only by non-German players in matches where GER was the id of either team1 or team2.
--You can use teamid!='GER' to prevent listing German players.
--You can use DISTINCT to stop players being listed twice.

SELECT DISTINCT(t1.player)
FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- in this typesetting, it is clear to know that we select from a "joined table"
WHERE ((t2.team1 = 'GER') OR (t2.team2 = 'GER')) AND (t1.teamid!='GER')  -- we want to select players score "against GER", so we first select matches include GER (team1 or team2 = GER), and then exclude records from GER players (with condition teamid!='GER')


--SELECT DISTINCT(t1.player)
--FROM game t1
--LEFT JOIN goal t2
--  ON t1.matchid = t2.id
--WHERE (team1='GER' AND team2='GRE') OR (team1='GRE' AND team2='GER')

--SELECT t1.player
--FROM goal t1
--LEFT JOIN game t2
--  ON t1.matchid = t2.id
--WHERE (t2.team1 = 'GER') AND (t2.team2 = 'GRE')

--SELECT t1.player
--FROM goal t1
--LEFT JOIN game t2
--  ON t1.teamid = t2.team1
--WHERE (t2.team1 = 'Gre') AND (t2.team2 = 'Ger')


--9
--Show teamname and the total number of goals scored.
SELECT t2.teamname, COUNT(1)
FROM goal t1 LEFT JOIN eteam t2 ON t1.teamid = t2.id
GROUP BY t2.teamname

--Wrong answer. Some of the data is incorrect.
--SELECT t2.teamname, SUM(gtime)
--FROM goal t1
--LEFT JOIN eteam t2
--  ON t1.teamid = t2.id
--GROUP BY t2.teamname

--Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'gisq.t2.teamname' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
--SELECT teamname, SUM(gtime)
--FROM goal t1
--LEFT JOIN eteam t2
--  ON t1.teamid = t2.id
--GROUP BY t1.teamid


--10
--Show the stadium and the number of goals scored in each stadium.
SELECT stadium, COUNT(1)
FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
GROUP BY t2.stadium


--11
--For every match involving 'POL', show the matchid, date and the number of goals scored.
SELECT t1.matchid, t2.mdate, COUNT(gtime)
FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
WHERE (t2.team1 = 'POL') OR (t2.team2 = 'POL')
GROUP BY t2.id, t2.mdate

--Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'gisq.t2.mdate' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
--SELECT t1.matchid, t2.mdate, COUNT(gtime)
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
--WHERE (t2.team1 = 'POL')
--GROUP BY t1.matchid

--In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'gisq.t1.matchid'; this is incompatible with sql_mode=only_full_group_by
--SELECT t1.matchid, t2.mdate, COUNT(gtime)
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
--WHERE (t2.team1 = 'POL') OR ((t2.team2 = 'POL'))

--Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'gisq.t2.mdate' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
--SELECT matchid, mdate, COUNT(gtime)
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
--WHERE (t2.team1 = 'POL') OR (t2.team2 = 'POL')
--GROUP BY t2.id


--12
--For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'
SELECT t1.matchid, t2.mdate, COUNT(gtime)
FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
WHERE t1.teamid = 'GER'  -- 剛剛隊伍名稱用到上一題的了
GROUP BY t1.matchid, t2.mdate

--wrong answer
--SELECT t1.matchid, t2.mdate, COUNT(gtime)
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
--WHERE t1.teamid = 'POL'
--GROUP BY t1.matchid, t2.mdate

--Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'gisq.t1.matchid' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
--SELECT t1.matchid, t2.mdate, COUNT(gtime)
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id
--WHERE t1.teamid = 'POL'
--GROUP BY t2.id, t2.mdate  -- notice. 即使欄位是相同意義，注意到 前面 SELECT t1.matchid 但是後面 GROUP BY t2.id -> sql 會辨認不出來，說不認識這個欄位


--13
--List every match with the goals scored by each team as shown. This will use "CASE WHEN" which has not been explained in any previous exercises.
--mdate	team1	score1	team2	score2
--1 July 2012	ESP	4	ITA	0
--10 June 2012	ESP	1	ITA	1
--10 June 2012	IRL	1	CRO	3

-- notice. 當 SELECT statement 一但變長容易忘記逗號變成 syntax error（當不只是選簡短的欄位名稱，而是當欄位涉及到 CASE WHEN ... THEN ... ELSE ... END，也跟選欄位一樣，記得加上逗號）


--https://sqlzoo.net/wiki/The_JOIN_operation?answer=1
SELECT mdate,
  team1,
  SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) score1,
  team2,
  SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) score2
  FROM game LEFT JOIN goal ON matchid = id
GROUP BY mdate, matchid, team1, team2


SELECT t2.mdate,
       t2.team1,
       SUM(CASE WHEN (t1.teamid = t2.team1) THEN 1 ELSE 0 END) score1,
       t2.team2,
       SUM(CASE WHEN (t1.teamid = t2.team2) THEN 1 ELSE 0 END) score2
FROM game t2 LEFT JOIN goal t1 ON t1.matchid = t2.id
GROUP BY t2.mdate, t1.matchid, t2.team1, t2.team2

-- wrong answer
--SELECT t2.mdate,
--       t2.team1,
--       SUM(CASE WHEN (t1.teamid = t2.team1) THEN 1 ELSE 0 END) score1,
--       t2.team2,
--       SUM(CASE WHEN (t1.teamid = t2.team2) THEN 1 ELSE 0 END) score2
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- left join is wrong, we use right join here. Using left join can cause duplicate data
--GROUP BY t2.mdate, t1.matchid, t2.team1, t2.team2
--ORDER BY t2.mdate, t1.matchid, t2.team1, t2.team2  -- since the date "mdate" is in the format "8 June 2012", if we order by "mdate" again, it would sort by 日期 into 1, 11, 12, 2, 3, ..., so we don't order by it again after group by


--Error: Expression #4 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'gisq.t1.teamid' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
--SELECT t2.mdate,
--       t2.team1,
--       t2.team2,
--       CASE WHEN (t1.teamid = t2.team1) THEN SUM(1) ELSE SUM(0) END team1_score,  -- the statement should be SUM(CASE ... WHEN ... THEN ... ELSE ... END)
--       CASE WHEN (t1.teamid = t2.team2) THEN SUM(1) ELSE SUM(0) END team2_score   -- the statement should be SUM(CASE ... WHEN ... THEN ... ELSE ... END)
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- this goal table left join game table would cause duplicate data
--GROUP BY t2.mdate, t2.team1, t2.team2


-- wrong answer
--SELECT t2.mdate,
--       t2.team1,
--       t2.team2,
--       CASE WHEN (t1.teamid = t2.team1) THEN 1 ELSE 0 END team1_score,
--       CASE WHEN (t1.teamid = t2.team2) THEN 1 ELSE 0 END team2_score
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- this statement doesn't include "group by" part


--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'CASE WHEN (t1.teamid = t2.team2) THEN 1
--            ELSE 0
--       END AS team2_' at line 7
--SELECT t2.mdate,
--       t2.team1,
--       t2.team2,
--       CASE WHEN (t1.teamid = t2.team1) THEN 1
--            ELSE 0
--       END AS team1_score                       -- 這邊SELECT欄位忘記加逗號，導致 sql syntax error
--       CASE WHEN (t1.teamid = t2.team2) THEN 1
--            ELSE 0
--       END AS team2_score
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- this goal table left join game table would cause duplicate data
--GROUP BY t2.id, t2.mdate


--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AS team1_score
--            WHEN (t1.teamid = t2.team2) THEN COUNT(t2.team2) AS ' at line 4
--SELECT t2.mdate,
--       t2.team1,
--       t2.team2,
--       CASE WHEN (t1.teamid = t2.team1) THEN COUNT(t2.team1) AS team1_score  --(1)這邊最後選出兩個欄位: team1_score, team2_score，就應該 SELECT 兩欄，不然這樣 case when 最後只會選出一個欄位而已（無法同時代表 team1_score 和 team2_score）； (2) the statement should be SUM(CASE ... WHEN ... THEN ... ELSE ... END)
--            WHEN (t1.teamid = t2.team2) THEN COUNT(t2.team2) AS team2_score
--            ELSE NULL
--       END
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- this goal table left join game table would cause duplicate data
--GROUP BY t2.id, t2.mdate


--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AS team1_score
--            WHEN t2.team2 THEN COUNT(t2.team2) AS team2_score
-- ' at line 4
--SELECT t2.mdate,
--       t2.team1,
--       t2.team2,
--       CASE WHEN t2.team1 THEN COUNT(t2.team1) AS team1_score  --(1)這邊最後選出兩個欄位: team1_score, team2_score，就應該 SELECT 兩欄，不然這樣 case when 最後只會選出一個欄位而已（無法同時代表 team1_score 和 team2_score）； (2) the statement should be SUM(CASE ... WHEN ... THEN ... ELSE ... END)
--            WHEN t2.team2 THEN COUNT(t2.team2) AS team2_score
--            ELSE NULL
--       END
--FROM goal t1 LEFT JOIN game t2 ON t1.matchid = t2.id  -- this goal table left join game table would cause duplicate data
--GROUP BY t2.id, t2.mdate





-- to check answers, go to 'cheat mode':
--In the tutorials it is possible to see the correct solutions by having the smiley laugh. Also if you can't get him to smile just enter '?answer=1' to the url.
