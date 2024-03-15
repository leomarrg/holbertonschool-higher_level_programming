-- script that lists all records with score above 10 --
SELECT `name`, `score`
FROM second_table
WHERE `score` >= 10
ORDER BY `score` DESC;
