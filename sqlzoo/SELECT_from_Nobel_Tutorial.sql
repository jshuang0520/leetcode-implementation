
-- https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial

--1
SELECT *
FROM nobel
WHERE yr = 1950

--2
SELECT winner
FROM nobel
WHERE yr = 1962
  AND subject = 'literature'

--3
SELECT yr, subject
FROM nobel
WHERE winner = 'Albert Einstein'

--4
SELECT winner
FROM nobel
WHERE (subject = 'peace')
  AND (yr >= 2000)

--5
SELECT *
FROM nobel
WHERE subject = 'literature'
  AND yr BETWEEN 1980 AND 1989

--6
SELECT *
FROM nobel
WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter', 'Barack Obama')

--7
SELECT winner
FROM nobel
WHERE winner LIKE 'John %'

--8
SELECT yr, subject, winner
FROM nobel
WHERE ((subject = 'physics') AND (yr = 1980))
  OR ((subject = 'chemistry') AND (yr = 1984))


--9
SELECT yr, subject, winner
FROM nobel
WHERE yr = 1980
  AND subject NOT IN ('chemistry', 'medicine')

--10
SELECT yr, subject, winner
FROM nobel
WHERE (subject = 'Medicine' AND yr < 1910)
  OR (subject = 'Literature' AND yr >= 2004)

--11
--Find all details of the prize won by PETER GRÜNBERG
--Non-ASCII characters
--The u in his name has an umlaut. You may find this link useful https://en.wikipedia.org/wiki/%C3%9C#Keyboarding
SELECT *
FROM nobel
WHERE winner = 'PETER GRÜNBERG'

--12
--Escaping single quotes
--You can't put a single quote in a quote string directly. You can use two single quotes within a quoted string.
SELECT *
FROM nobel
WHERE winner = 'EUGENE O\'NEILL'

--13
SELECT winner, yr, subject
FROM nobel
WHERE winner LIKE 'Sir %'
ORDER BY yr DESC, winner ASC
-- note. it is "order by", not "sort by"

--14 (wrong answer at first try)
-- (hint) The expression column_name IN ('value_1','value_2') can be used as a value - it will be 0 or 1.
SELECT winner, subject
  FROM nobel
 WHERE yr=1984
 ORDER BY subject IN ('physics','chemistry') ASC, subject ASC, winner ASC

-- (hint) The expression subject IN ('chemistry','physics') can be used as a value - it will be 0 or 1.
--SELECT winner, subject, subject IN ('physics','chemistry')
--  FROM nobel
-- WHERE yr=1984
-- ORDER BY subject,winner
-- (table result)
--winner            subject     subject IN ('physics','chemistry')
--Bruce Merrifield  Chemistry   1
--Richard Stone     Economics   0

--(wrong answer at first try)
--SELECT winner, subject
--FROM nobel
--WHERE yr = 1984
--ORDER BY CASE WHEN subject IN ('chemistry', 'physics') THEN subject END ASC
--google: [mysql order by column with condition](https://stackoverflow.com/questions/32670432/mysql-order-by-with-condition)

--quiz