
-- https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial

--1
SELECT name
FROM world
WHERE population > (SELECT population FROM world WHERE name = 'Russia')

--2
SELECT name
FROM world
WHERE continent = 'Europe'
  AND gdp/population > (SELECT gdp/population FROM world WHERE name = 'United Kingdom')


--3
SELECT name, continent
FROM world
WHERE continent IN (SELECT continent FROM world WHERE name IN('Argentina', 'Australia'))
ORDER BY name ASC

--4 (couldn't solve it at first glance)
SELECT name, population
FROM world
WHERE population > (SELECT population FROM world WHERE name = 'United Kingdom')
  AND population < (SELECT population FROM world WHERE name = 'Germany')

-- notes. "BETWEEN A AND B" includes the boundaries
--SELECT name, population
--FROM world
--WHERE population BETWEEN (SELECT population FROM world WHERE name = 'United Kingdom')
--                 AND (SELECT population FROM world WHERE name = 'Germany')

--5 (couldn't solve it at first glance)
--Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.
--Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.
--The format should be Name, Percentage for example:
--name	percentage
--Albania	3%
--Andorra	0%

-- try more than 5 times
SELECT name, CONCAT(ROUND((population/(SELECT population FROM world WHERE name = 'Germany'))*100, 0), '%') AS Percentage
FROM world
WHERE continent = 'Europe'

--I have no idea how to solve it.
--SELECT name, (population/total AS percentage)
--FROM world
--WHERE

------------------------------------------------------------------------------------------------------------------------
--We can use the word ALL to allow >= or > or < or <=to act over a list. For example, you can find the largest country in the world, by population with this query:
SELECT name
FROM world
WHERE population >= ALL(SELECT population
                        FROM world
                        WHERE population>0)
--You need the condition population>0 in the sub-query as some countries have null for population.
------------------------------------------------------------------------------------------------------------------------

--6
--Which countries have a GDP greater than every country in Europe?
--[Give the name only.] (Some countries may have NULL gdp values)
--sol 1
SELECT name
FROM world
WHERE gdp > ALL(SELECT gdp
                FROM world
                WHERE continent = 'Europe' AND gdp > 0)
--sol 2
SELECT name
FROM world
WHERE gdp > (SELECT gdp FROM world WHERE continent = 'Europe' ORDER BY gdp DESC LIMIT 1)

--misunderstood the question (couldn't solve it at first glance)
--SELECT name
--FROM world
--WHERE continent = 'Europe'
--ORDER BY gdp DESC
--LIMIT 1


--7 (couldn't solve it at first glance)
--Find the largest country (by area) in each continent, show the continent, the name and the area:
-- try more than 5 times, and refer to ans to get this answer
SELECT continent, name, area
FROM world t1
WHERE area IN (SELECT MAX(area)
               FROM world t2
               WHERE t1.continent = t2.continent)

--https://github.com/codyloyd/sqlzoo-solutions/blob/master/SQLZOO_solutions.md#select-in-select
SELECT continent, name, area
FROM world x
WHERE area >= ALL(SELECT area
                  FROM world y
                  WHERE y.continent=x.continent
                  AND area>0)

-- [mysql Find the largest country in each continent](https://stackoverflow.com/questions/50517185/sqlzoo-using-groupby-to-find-the-largest-country-in-a-continent-is-this-possib)
SELECT continent, name, area
FROM world
WHERE area IN (SELECT MAX(area) FROM world GROUP BY continent)

--(couldn't solve it at first glance)
--SELECT name, continent, area
--FROM world
--WHERE area


--8
--List each continent and the name of the country that comes first alphabetically.
-- [first country of each continent (alphabetically)](https://stackoverflow.com/questions/44897979/sql-zoo-list-each-continent-and-the-name-of-the-country-that-comes-first-alphabe)
--explanation
--Japan gets filtered out because Japan <= All(Afghanistan,Taiwan,Japan) is false since Japan is not less or equal to Afghanistan (A comes before J)
--Taiwan gets filtered out because Taiwan <= All(Afghanistan,Taiwan,Japan) is false since Taiwan is not less or equal to Afghanistan.
SELECT continent, name
FROM world t1
WHERE name <= ALL (SELECT name FROM world t2 WHERE t1.continent = t2.continent)
ORDER BY continent

--Expression #2 of SELECT list is not in GROUP BY clause and contains non-aggregated column 'gisq.t1.name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
--SELECT continent, name
--FROM world t1
--GROUP BY continent
--ORDER BY name LIMIT 1

--This version of MySQL doesn't yet support 'LIMIT & IN/ALL/ANY/SOME subquery'
--SELECT continent, name
--FROM world t1
--WHERE name IN (SELECT name FROM world t2 WHERE t1.continent = t2.continent ORDER BY name LIMIT 1)

--misunderstood the question (couldn't solve it at first glance)
--SELECT continent, name
--FROM world
--ORDER BY name, continent


--9 (couldn't solve it at first glance)
--Find the continents where all countries have a population <= 25000000.
--Then find the names of the countries associated with these continents. Show name, continent and population.
--try more than 5 times, and refer to ans to get this answer
SELECT name, continent, population
FROM world t1
WHERE 25000000 >= ALL(SELECT population FROM world t2 WHERE (t1.continent = t2.continent) AND (t2.population > 0)) -- add (t2.population > 0) to prevent some records with NULL population

-- note. it would be a syntax error if ALL (...) <= 25000000; however, it would be correct if we use 25000000 >= ALL (...)
--SELECT name, continent, population
--FROM world t1
--WHERE ALL(SELECT population FROM world t2 WHERE (t1.continent = t2.continent) AND (t2.population > 0)) <= 25000000


-- https://github.com/codyloyd/sqlzoo-solutions/blob/master/SQLZOO_solutions.md#select-in-select
SELECT name, continent, population
FROM world x
WHERE 25000000 >= ALL(SELECT population
	                  FROM world y
		              WHERE x.continent = y.continent
                      AND y.population>0);

--You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ALL (t1.continent = t2.continent AND population <= 25000000))' at line 3
--SELECT name, continent, population
--FROM world t1
--WHERE continent IN (SELECT continent FROM world t2 WHERE ALL (t1.continent = t2.continent AND population <= 25000000))

-- (couldn't solve it at first glance)
--SELECT name, continent, population
--FROM world
--WHERE name IN (SELECT name FROM world WHERE population <= 25000000)

--10
--Some countries have populations more than three times that of all of their neighbours (in the same continent).
--Give the countries and continents.
SELECT name, continent
FROM world t1
WHERE population > ALL (SELECT population*3 FROM world t2 WHERE t1.continent = t2.continent and t1.name != t2.name)

-- wrong answer
--SELECT name, continent
--FROM world t1
--WHERE population >= ALL (SELECT population*3 FROM world t2 WHERE t1.continent = t2.continent)
