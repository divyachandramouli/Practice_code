SubQuery Q6
What is the lifetime average amount spent in terms of total_amt_usd for only the companies that spent more than the average of all orders.


SELECT AVG(t1.tot_sp)

FROM

(SELECT a.id AS acc_id , sum(o.total_amt_usd) AS tot_sp
FROM accounts a
JOIN orders o 
ON o.account_id = a.id 
GROUP BY a.id
HAVING  sum(o.total_amt_usd) > AVG(o.total_amt_usd)) t1



      69568.447891566265