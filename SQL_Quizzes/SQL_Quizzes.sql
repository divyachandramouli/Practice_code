SQL_Quizzes.sql

SELECT RIGHT (website,3) , COUNT(*)
FROM accounts
GROUP BY 1