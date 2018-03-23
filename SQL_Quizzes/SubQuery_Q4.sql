SubQuery Q4
For the customer that spent the most (in total of their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?


SELECT t1.acc_name, w.channel, COUNT(*)
FROM web_events w
JOIN
(SELECT a.id AS acc_id, a.name AS acc_name, sum(o.total_amt_usd) AS tot_spent
FROM accounts a
JOIN orders o 
ON o.account_id = a.id
GROUP BY a.id, a.name
ORDER BY 3 DESC
LIMIT 1) t1 
ON w.account_id=t1.acc_id
GROUP BY 1,2


