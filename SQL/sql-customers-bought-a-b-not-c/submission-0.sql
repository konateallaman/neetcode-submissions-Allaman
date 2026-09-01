-- Write your query below
SELECT customer_id,customer_name
FROM customers
WHERE customer_id IN(SELECT customer_id
                        FROM orders
                        WHERE product_name='A'
                        INTERSECT
                        SELECT customer_id
                        FROM orders
                        WHERE product_name='B'
                        EXCEPT
                        SELECT customer_id
                        FROM orders
                        WHERE product_name='C'
 )
ORDER BY customer_name;
