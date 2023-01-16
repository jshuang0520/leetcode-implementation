
-- https://sqlzoo.net/wiki/More_JOIN_operations


--1
SELECT id, title
FROM movie
WHERE yr = 1962


--2
SELECT yr
FROM movie
WHERE title = 'Citizen Kane'


--3
SELECT id, title, yr
FROM movie t1
WHERE title LIKE '%Star Trek%'
ORDER BY yr


--4
SELECT id
FROM actor
WHERE name = 'Glenn Close'


--5
SELECT id
FROM movie
WHERE title = 'Casablanca'


--6
--Obtain the cast list for 'Casablanca'.
--what is a cast list?
SELECT t3.name
FROM movie t1 LEFT JOIN casting t2 ON t1.id= t2.movieid LEFT JOIN actor t3 ON t3.id = t2.actorid
WHERE t1.title = 'Casablanca'


--7
--Obtain the cast list for the film 'Alien'
SELECT t3.name
FROM movie t1 LEFT JOIN casting t2 ON t1.id= t2.movieid LEFT JOIN actor t3 ON t3.id = t2.actorid
WHERE t1.title = 'Alien'


--8
--List the films in which 'Harrison Ford' has appeared
SELECT t1.title
FROM movie t1 LEFT JOIN casting t2 ON t1.id= t2.movieid LEFT JOIN actor t3 ON t3.id = t2.actorid
WHERE t3.name= 'Harrison Ford'


--9
--List the films where 'Harrison Ford' has appeared - but not in the starring role.
--[Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]
SELECT title
FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
WHERE (t3.name = 'Harrison Ford') AND (t2.ord <> 1)


--10
--List the films together with the leading star for all 1962 films.
SELECT t1.title, t3.name
FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
WHERE (t1.yr = 1962) AND (t2.ord = 1)  -- ord = 1 means "the leading star"


--Wrong answer. Some of the data is incorrect.
--SELECT t1.title, t3.name
--FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
--WHERE t1.yr = 1962


--11
--Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
SELECT t1.yr, COUNT(*) AS num_movies
FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
WHERE (t3.name = 'Rock Hudson')
GROUP BY t1.yr
HAVING num_movies > 2


--12 Lead actor in Julie Andrews movies
--List the film title and the leading actor for all of the films 'Julie Andrews' played in.

-- TODO: a faster query


-- my correct answer  # TODO: but it is a slow query, we should enhance the performance later
SELECT t1.title, t3.name
FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
WHERE (t1.id IN (SELECT t1.id FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id WHERE t3.name = 'Julie Andrews'))
  AND (t2.ord = 1)

-- official answer
SELECT title, name
  FROM movie, casting, actor
  WHERE movieid=movie.id
    AND actorid=actor.id
    AND ord=1
    AND movieid IN (SELECT movieid
                    FROM casting, actor
                    WHERE actorid=actor.id
                    AND name='Julie Andrews')

--wrong answer
--SELECT t1.title, t3.name
--FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
--WHERE (t3.name = 'Julie Andrews')  -- this would SELECT every movies that 'Julie Andrews' showed up, which is a different meaning from the original question


--wrong answer
--SELECT t1.title, t3.name
--FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
--WHERE (t2.ord = 1) AND (t3.name = 'Julie Andrews')  -- this would SELECT movies that are lead by 'Julie Andrews', which is a different meaning from the original question


--13
--Obtain a list, in alphabetical order, of actors who've had at least 15 starring roles.

-- my correct answer
SELECT t2.name
FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id
WHERE t1.ord = 1  -- that is what "starring" means, it is equivalent to "leading actor"
GROUP BY t2.name
HAVING COUNT(t1.movieid) >= 15

-- my correct answer
SELECT t3.name
FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id  -- 多 join 一張表
WHERE t2.ord = 1  -- that is what "starring" means, it is equivalent to "leading actor"
GROUP BY t3.name
HAVING COUNT(t2.movieid) >= 15


--Wrong answer. Some of the data is incorrect.
--SELECT t2.name
--FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id
--GROUP BY t2.name
--HAVING COUNT(DISTINCT(t1.movieid)) >= 15  -- should not use distinct
-- ------------> 比較：當 query 有或沒有加上 DISTINCT 的差別:
--HAVING COUNT(t2.movieid) vs HAVING COUNT(DISTINCT t2.movieid)，差看 SELECT COUNT(t2.name) 數量
--18 -> 16
--22 -> 22
--31 -> 18
--29 -> 17


--Wrong answer. Some of the data is incorrect.
--SELECT t2.name
--FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id
--GROUP BY t2.name
--HAVING COUNT(*) >= 15


--Wrong answer. Some of the data is incorrect.
--SELECT t3.name
--FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
--GROUP BY t3.name
--HAVING COUNT(*) >= 15


--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AS num >= 15
--ORDER BY num' at line 4
--SELECT t3.name
--FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid LEFT JOIN actor t3 ON t2.actorid = t3.id
--GROUP BY t3.name
--HAVING COUNT(*) AS num >= 15  -- we can't give it an alias ("num") here
--ORDER BY num                  -- we can't give it an alias ("num") here


--14
--List the films released in the year 1978 ordered by the number of actors in the cast, then by title.
SELECT t1.title, COUNT(t2.actorid) AS cnt
FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid
WHERE t1.yr = 1978
GROUP BY t1.title
ORDER BY cnt DESC, t1.title


--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DECS, t1.title' at line 5
--SELECT t1.title, COUNT(t2.actorid)
--FROM movie t1 LEFT JOIN casting t2 ON t1.id = t2.movieid
--WHERE t1.id = 1978                         -- should be yr=1978
--GROUP BY t1.title
--ORDER BY COUNT(t2.actorid) DECS, t1.title  -- syntax error due to typo "DECS"


--15
--List all the people who have worked with 'Art Garfunkel'.

-- TODO: a faster query
-- mysql join with condition



-- official answer
SELECT DISTINCT d.name
FROM actor d
   JOIN casting a ON (a.actorid=d.id)
   JOIN casting b on (a.movieid=b.movieid)
   JOIN actor c on (b.actorid=c.id and c.name='Art Garfunkel')  -- google: [mysql join with condition](https://stackoverflow.com/questions/13817481/mysql-join-with-condition)
WHERE d.id!=c.id
--改寫上面的 official answer
SELECT t1.name
FROM actor t1
LEFT JOIN casting t2 ON t1.id = t2.actorid
LEFT JOIN casting t3 ON t2.movieid = t3.movieid  -- table "casting" self join
LEFT JOIN actor t4 ON (t3.actorid = t4.id AND t4.name = 'Art Garfunkel')  -- table "actor" self join, 同時加上限制條件
WHERE t1.id <> t4.id  -- select people other than 'Art Garfunkel' herself, i.e., her co-workers


-- my correct answer  # TODO: but it is a slow query, we should enhance the performance later
SELECT t2.name
FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id
WHERE t1.movieid IN (SELECT t1.movieid FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id WHERE t2.name = 'Art Garfunkel')
  AND (t2.name <> 'Art Garfunkel')


--wrong answer
--SELECT t2.name
--FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id
--WHERE t1.movieid IN (SELECT t1.movieid FROM casting t1 LEFT JOIN actor t2 ON t1.actorid = t2.id WHERE t2.name = 'Art Garfunkel')  -- if we forget to exclude 'Art Garfunkel' herself, we can still see her name on the list. Thus, this list provides not only her co-workers, but also herself
