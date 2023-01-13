
-- https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial

--1
SELECT name, continent, population
FROM world

--2
SELECT name
FROM world
WHERE population >= 200000000

--3
SELECT name, (GDP/population) AS per_capita_GDP
FROM world
WHERE population >= 200000000

--4
SELECT name, (population/1000000) AS population
FROM world
WHERE continent = 'South America'

--5
SELECT name, population
FROM world
WHERE name IN ('France', 'Germany', 'Italy')

--6
SELECT name
FROM world
WHERE name LIKE '%United%'

--7 (wrong answer at first try)
--Two ways to be big: A country is big if it has an area of more than 3 million sq km or it has a population of more than 250 million.
--Show the countries that are big by area or big by population. Show name, population and area.
SELECT name, population, area
FROM world
WHERE (area > 3000000) OR (population > 250000000)

--(wrong answer at first try)
--SELECT name, population, area
--FROM world
--WHERE (population > 3000000) OR (population > 250000000)

--8 (wrong answer at first try)
SELECT name, population, area
FROM world
WHERE ((area > 3000000) OR (population > 250000000))
AND NOT ((area > 3000000) AND (population > 250000000))

--(wrong answer at first try)
--SELECT name, population, area
--FROM world
--WHERE ((population > 3000000) OR (population > 250000000))
--AND NOT ((population > 3000000) AND (population > 250000000))

--9
SELECT
  name,
  ROUND((population/1000000), 2) AS population,
  ROUND((GDP/1000000000), 2) AS GDP
FROM world
WHERE continent = 'South America'

--10
--Show the name and per-capita GDP for those countries with a GDP of at least one trillion (1000000000000; that is 12 zeros). Round this value to the nearest 1000.
--Show per-capita GDP for the trillion dollar countries to the nearest $1000.
SELECT
  name,
  ROUND((GDP/population)/1000, 0)*1000 AS per_capita_GDP
FROM world
WHERE GDP >= 1000000000000

--11
--Greece has capital Athens.
--Each of the strings 'Greece', and 'Athens' has 6 characters.
--Show the name and capital where the name and the capital have the same number of characters.
--You can use the LENGTH function to find the number of characters in a string
SELECT name, capital
FROM world
WHERE LENGTH(name) = LENGTH(capital)

--12 (couldn't solve it at first glance)
SELECT name, capital
FROM world
WHERE (LEFT(name, 1) = LEFT(capital, 1))
AND NOT (name = capital)

--(You have an error in your SQL syntax)
--SELECT name, capital
--FROM world
--WHERE (LEFT(name) = LEFT(capital))
--AND (name <> capital)

--13
--Equatorial Guinea and Dominican Republic have all of the vowels (a e i o u) in the name. They don't count because they have more than one word in the name.
--Find the country that has all the vowels and no spaces in its name.
--You can use the phrase name NOT LIKE '%a%' to exclude characters from your results.
--The query shown misses countries like Bahamas and Belarus because they contain at least one 'a'
SELECT name
FROM world
WHERE (name LIKE '%a%')
AND (name LIKE '%e%')
AND (name LIKE '%i%')
AND (name LIKE '%o%')
AND (name LIKE '%u%')
AND (name NOT LIKE '% %')

--quiz
