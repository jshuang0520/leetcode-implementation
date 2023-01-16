
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
FROM goal t1
LEFT JOIN eteam t2
  ON t1.teamid = t2.id
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
Show the stadium and the number of goals scored in each stadium.
SELECT stadium, COUNT(1)
FROM goal t1
LEFT JOIN game t2
  ON t1.matchid = t2.id
GROUP BY t2.stadium