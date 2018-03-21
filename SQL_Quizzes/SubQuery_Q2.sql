SubQuery Q2
/*For the region with the largest sales total_amt_usd, how many total orders were placed? */

SELECT r.name, SUM(o.total_amt_usd) AS sales, sum(o.total) AS order_count
FROM orders o
JOIN accounts a 
ON a.id =o.account_id
JOIN sales_reps s
ON s.id=a.sales_rep_id
JOIN region r
ON r.id=s.region_id
GROUP BY r.name
ORDER BY sales DESC
LIMIT 1