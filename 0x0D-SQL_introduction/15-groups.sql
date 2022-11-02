-- a script that lists the number of records with the same score in the table second_table
-- in database hbtn_0c_0 in MYsql server
SELECT `score`, COUNT(*) AS `number`
GROUP BY `score`
ORDER BY `number` DESC;
