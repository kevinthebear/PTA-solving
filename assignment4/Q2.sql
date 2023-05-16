SELECT rosterstatus, AVG(EXTRACT(year from birthdate)) AS avg_year
FROM player_info
WHERE rosterstatus = 'Active'
GROUP BY rosterstatus