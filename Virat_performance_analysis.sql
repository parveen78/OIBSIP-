CREATE DATABASE T20;
USE T20;
Select * from Virat_perform;

#Problem 1: Analysis of Virat's top 5 ground performance in the year 2021?
select ground,sum(Runs) AS Total_runs from Virat_perform where year=2021 
group by ground 
order by Total_runs DESC limit 5;

#Problem 2: Analyze Virat batting performance data and show great performance monthly and quarterly in the year 2018?
SELECT
      monthname(date) AS month,
      quarter(date) AS quarter,
      year,
      runs from virat_perform;

#Problem 3: In which opposition team did Virat have the most top 5 batting performances in the year 2021?
select opponent,max(runs) AS MAX_runs from virat_perform where Year=2021 
group by opponent
order by Max_runs
Desc Limit 5;


#Problem 4 : How many cricket matches did Virat play for India in the year 2017, 2018, 2019 & 2020 ?
SELECT year,COUNT(*) AS matches_played FROM Virat_perform
WHERE year IN (2017, 2018, 2019, 2020)
GROUP BY year
ORDER BY matches_played DESC;

