/* 
Customer Table

customer_id	first_name	last_name	age	country
1	           John	        Doe	  31	USA
2         	Robert	      Luna	22	USA
3	          David	     Robinson	22	UK
4	          John	   Reinhardt	25	UK
5	          Betty	         Doe	28	UAE

Orders
order_id	item	   amount	customer_id
1	        Keyboard	400	    4
2	           Mouse	300	    4
3	          Monitor	12000	  3
4	         Keyboard	400	    1
5	         Mousepad	250	    2


OUTPUT:
-------
first_name	last_name	Amount
David	      Robinson	12000
John	      Reinhardt	400
*/


SELECT Customers.first_name, Customers.last_name,MAX(Orders.amount) AS Amount From Customers 
join Orders on Orders.customer_id = Customers.customer_id
where Orders.amount > 300
UNION ALL
SELECT Customers.first_name, Customers.last_name,MIN(Orders.amount) From Customers 
join Orders on Orders.customer_id = Customers.customer_id
where Orders.amount > 300;
