
-- https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial

--1
SELECT SUM(population) AS population
FROM world

--2
SELECT DISTINCT(continent)
FROM world

--3
SELECT SUM(gdp)
FROM world
WHERE continent = 'Africa'

--4
SELECT COUNT(1)
FROM world
WHERE area >= 1000000

--5
SELECT SUM(population) AS population
FROM world
WHERE name IN ('Estonia', 'Latvia', 'Lithuania')

--6 (couldn't solve it at first glance)
--For each continent show the continent and number of countries.
SELECT continent, COUNT(DISTINCT(name))
FROM world
GROUP BY continent

--In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'gisq.world.continent'; this is incompatible with sql_mode=only_full_group_by
--SELECT continent, COUNT(DISTINCT(name))
--FROM world

--7 (couldn't solve it at first glance)
--For each continent show the continent and number of countries with populations of at least 10 million.
SELECT continent, COUNT(DISTINCT(name))
FROM world
WHERE population >= 10000000
GROUP BY continent

--In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'gisq.world.continent'; this is incompatible with sql_mode=only_full_group_by
--SELECT continent, COUNT(DISTINCT(name))
--FROM world
--WHERE population >= 10000000

--8
SELECT continent
FROM world
GROUP BY continent
HAVING SUM(population) >= 100000000
