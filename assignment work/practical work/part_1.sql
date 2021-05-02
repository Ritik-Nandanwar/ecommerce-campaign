SELECT
     Shopper_first_name AS [first name]
     ,Shopper_surname AS [surname]
     ,Shopper_email_address AS [email address]
     ,(strftime('%Y', 'now') - strftime('%Y', Date_of_birth) ) - (strftime('%m-%d', 'now') < strftime('%m-%d', Date_of_Birth) ) AS [age]
     ,date_joined AS [date joined]
     FROM Shoppers
     WHERE Date_joined >= '2020-01-01' OR Date_of_birth > '1990-01-01'
     ORDER BY Date_of_birth, Shopper_surname
     ;
/* b) The website requires a customer account history page which will accept the shopper id as a parameter.
 Write a query to retrieve the first name and surname for a specific shopper along with details of all the orders they’ve placed, 
 displaying the order no, order date, product description, seller name, quantity ordered, price (right-justified with two decimal
  places and prefixed by a £ sign) and ordered product status. Print date columns in the format DD-MM-YYYY. Sort the results by 
  order date showing the most recent order first. Test your query by prompting for the user to input a shopper account ref and produce results for shopper ids 10000 and 10019.*/

SELECT 
    s.shopper_first_name AS [First Name]
    ,s.shopper_surname AS [Surname]
    ,so.Order_id AS [Order ID]
    ,so.Order_date AS [Order Date]
    ,p.product_description AS [Product Description]
    ,sell.Seller_name AS [Seller Name]
    ,op.Quantity AS [Quantity]
    ,op.Ordered_product_status AS [Order Status]
    ,PRINTF("£%.2f",ps.Price) AS [Price] 
    FROM shopper_orders so
        INNER JOIN
        shoppers s ON s.shopper_id = so.shopper_id
        INNER JOIN
        ordered_products op ON op.order_id = so.order_id
        INNER JOIN
        products p ON p.product_id = op.product_id
        INNER JOIN
        product_sellers ps ON ps.product_id = op.product_id
        INNER JOIN
        sellers sell ON sell.seller_id = ps.seller_id
        WHERE s.shopper_id = '10000'
        ORDER BY so.Order_date DESC
;
        


/*c) The business relationship manager has asked you to write a summary report on the sellers and products that they have had sold since 1st June 2019.
Display the seller account ref, seller name, product code, product description, number of orders, total quantity sold and total value of all sales
 (right-justified with two decimal places and prefixed by a £ sign) for each product they sell. You should also include products that a seller sells but has
  had no orders for and show any NULL values as 0. Sort results by seller name and then product description. */
  
SELECT
    s.Seller_account_ref AS [seller Account Ref]
    ,s.Seller_name  AS [Seller Name]
    ,p.product_code AS [Product Code]
    ,p.product_description AS [Product Description]
    ,PRINTF("£%.2f",(op.quantity*op.price)) AS [total Sales]
    ,op.quantity
    FROM sellers s
        INNER JOIN
        ordered_products op ON op.seller_id = s.seller_id
        INNER JOIN
        products p ON p.product_id = op.product_id
        INNER JOIN
        shopper_orders so ON so.order_id = op.order_id
        WHERE so.order_date > '2019-05-01' OR op.quantity = NULL
;
  


/*d) The head of sales wants a report showing the products that have an average quantity sold that is less than the average quantity sold for the category that the product is in.
 Cancelled orders should be excluded from the calculations. Any products that haven’t sold at all should also be displayed with an average quantity of 0. 
 Display the category description, product code, product description and average quantity sold and show results in category description, then product description order */
 
SELECT 
     category_description AS [category description]
     ,product_description AS [product description]
     ,product_code AS [product code]
     ,IFNULL(AVG(op.quantity),'0' ) AS [average quantity sold]
 FROM Products p
     INNER JOIN
     categories c ON c.category_id = p.category_id
     INNER JOIN
     ordered_products op ON op.product_id = p.product_id
 GROUP BY category_description
 HAVING AVG(op.quantity) > op.quantity
;
             