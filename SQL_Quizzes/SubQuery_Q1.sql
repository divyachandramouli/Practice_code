SubQuery Q1
/* Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales */
SELECT t1.Region_name, t1.Sales_rep_name

FROM

	(SELECT Region_name,  MAX(Sales) AS Max_sales
	 FROM
			(SELECT  r.name Region_name, s.name Sales_rep_name,SUM(o. total_amt_usd) Sales
             FROM sales_reps s
             JOIN region r
        	ON s.region_id=r.id
         	JOIN accounts a
         	ON a.sales_rep_id=s.id
         	JOIN orders o
         	ON o.account_id=a.id
       	    GROUP BY 2,1
             ) t1
    GROUP BY 1) t2

JOIN

			(SELECT  r.name Region_name, s.name Sales_rep_name,SUM(o. total_amt_usd) Sales
             FROM sales_reps s
             JOIN region r
        	ON s.region_id=r.id
         	JOIN accounts a
         	ON a.sales_rep_id=s.id
         	JOIN orders o
         	ON o.account_id=a.id
       	    GROUP BY 2,1
             ) t1

 ON t1.Region_name = t2.Region_name AND t1. Sales=t2.Max_Sales
 GROUP BY 1,2
