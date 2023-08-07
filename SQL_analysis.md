## Analysing Data using SQL

#### Task 1. How many olympics games have been held?
<pre>
SELECT COUNT(DISTINCT Games)
FROM olympics_history
</pre>

#### Task 2. List down all Olympics games held so far. Order the result by year.
<pre>
SELECT DISTINCT Year, Season, City
FROM olympics_history
ORDER BY Year
</pre>

#### Task 3. Mention the total no of nations who participated in each olympics game?. Order the results by games.
<pre>
SELECT t1.Games, COUNT(DISTINCT t2.region)
FROM olympics_history AS t1
LEFT JOIN olympics_history_noc_regions AS t2
  ON t1.NOC = t2.NOC
GROUP BY t1.Games
ORDER BY 1
</pre>

#### Task 4. Which nation has participated in all of the olympic games? and order the output by first column which is fetched
<pre>
WITH T1
AS (SELECT NOC
FROM olympics_history
GROUP BY Games, NOC)
SELECT T2.region, COUNT(*) AS num_games
FROM T1
LEFT JOIN olympics_history_noc_regions AS T2
  ON T1.NOC = T2.NOC
GROUP BY T1.NOC
HAVING num_games = (SELECT COUNT(DISTINCT Games) FROM olympics_history)
</pre>

#### Task 5. How many unique athletes have won a gold medal in the Olympics?
<pre>
SELECT COUNT(DISTINCT Name)
FROM olympics_history
WHERE Medal = 'Gold'
</pre>

#### Task 6. Which Sports were just played only once in the olympics? and Order the output by Sports. output should include number of games and games.
<pre>
WITH T1
AS (SELECT Games, Sport
FROM olympics_history
GROUP BY Games, Sport)
SELECT Sport, COUNT(*) AS num_games, Games
FROM T1
GROUP BY Sport
HAVING num_games = 1
ORDER BY Sport
</pre>

#### Task 7. Fetch the total no of sports played in each olympic games. Order by no of sports by descending.
<pre>
WITH T1
AS (SELECT Games, Sport
FROM olympics_history
GROUP BY Games, Sport)
SELECT Games, COUNT(*) AS num_sports
FROM T1
GROUP BY Games
</pre>

#### Task 8. Fetch oldest athletes to win a gold medal
<pre>
SELECT Name, Sex, Age, Team, Games, City, Sport, Event, Medal, 1 AS rnk
FROM olympics_history
WHERE Medal = "Gold"
ORDER BY Age DESC
LIMIT 1
</pre>

#### Task 9. Top 5 athletes who have won the most gold medals. Order the results by gold medals in descending.
<pre>
WITH t1
AS (SELECT Name, Team, COUNT(*) AS total_medal,
  DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS medal_rank
FROM olympics_history
WHERE Medal = "Gold"
GROUP BY Name, Team)
SELECT Name, Team, total_medal
FROM t1
ORDER BY total_medal DESC
LIMIT 5
</pre>

#### Task 10. Top 5 athletes who have won the most medals (gold/silver/bronze). Order the results by medals in descending.
<pre>
WITH t1
AS (SELECT Name, Team, COUNT(*) AS total_medal,
  DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS medal_rank
FROM olympics_history
WHERE Medal <> 'Medal-less'
GROUP BY Name, Team, Sport)
SELECT Name, Team, total_medal
FROM t1
ORDER BY total_medal DESC
LIMIT 5
</pre>

#### Task 11. Top 5 most successful countries in olympics. Success is defined by no of medals won.
<pre>
WITH t1
AS (SELECT region, COUNT(*) AS total_medal,
  DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS medal_rank
FROM olympics_history AS a
LEFT JOIN olympics_history_noc_regions AS b
  ON a.NOC = b.NOC
WHERE Medal <> 'Medal-less'
GROUP BY region)
SELECT region, total_medal, medal_rank
FROM t1
ORDER BY total_medal DESC
LIMIT 5
</pre>

#### Task 12. In which Sport/event, India has won highest medals.
<pre>
SELECT Sport, COUNT(*)
FROM olympics_history
WHERE Team = 'India'
AND Medal <> "Medal-less"
GROUP BY Sport
LIMIT 1
</pre>

#### Task 13.Break down all olympic games where india won medal for Hockey and how many medals in each olympic games and order the result by no of medals in descending.
<pre>
SELECT Team, Sport, Games, COUNT(*) AS total_medals
FROM olympics_history
WHERE Team = 'India'
AND Medal <> "Medal-less"
AND Sport = 'Hockey'
GROUP BY Games, Team, Sport
ORDER BY 2 DESC
</pre>
