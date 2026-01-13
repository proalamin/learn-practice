-- show all databases
SHOW DATABASES;

-- create database
CREATE DATABASE databaseName;

-- use database
USE northwind;

-- delete database
DROP DATABASE databaseName;

-- show all tables
SHOW TABLES;

-- create table
CREATE TABLE tableName (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT
);

-- describe table structure
DESCRIBE customers;

-- rename table
RENAME TABLE tableName TO newTableName;

-- delete table
DROP TABLE tableName;

-- add column
ALTER TABLE tableName ADD columnName VARCHAR(50);

-- modify column
ALTER TABLE tableName MODIFY columnName INT;

-- rename column
ALTER TABLE tableName RENAME COLUMN columnName TO newColumnName;

-- delete column
ALTER TABLE tableName DROP columnName;

-- insert single record
INSERT INTO tableName (name, age)
VALUES ('Al Amin', 22);

-- insert multiple records
INSERT INTO tableName (name, age) VALUES
('Rahim', 21),
('Karim', 23);

-- select all data from a table
SELECT * FROM customers;

-- select specific columns
SELECT first_name, last_name, city FROM customers;

-- select with condition
SELECT first_name, last_name, city FROM customers WHERE city="Seattle";

-- select with AND
SELECT * FROM customers WHERE city="Seattle" AND first_name="Anna";

-- select with OR
SELECT * FROM customers WHERE city="Seattle" OR city="New York";

-- order by ascending
SELECT * FROM customers ORDER BY first_name ASC;

-- order by descending
SELECT * FROM customers ORDER BY first_name DESC;

-- limit result
SELECT * FROM customers LIMIT 5;



-- update record
UPDATE customers
SET company = "Company Tesla"
WHERE first_name = 'Anna';

-- delete specific record
DELETE FROM tableName WHERE name = 'Karim';

-- delete all records
DELETE FROM tableName;


-- primary key
id INT PRIMARY KEY;

-- foreign key
FOREIGN KEY (dept_id) REFERENCES department(dept_id);

-- unique constraint
email VARCHAR(50) UNIQUE;

-- not null constraint
name VARCHAR(50) NOT NULL;


-- count function
SELECT COUNT(*) FROM orders;

-- sum function
SELECT SUM(shipping_fee) FROM orders;

-- average function
SELECT AVG(shipping_fee) FROM orders;

-- max function
SELECT MAX(shipping_fee) FROM orders;

-- min function
SELECT MIN(shipping_fee) FROM orders;


-- subquery
SELECT * FROM orders
WHERE shipping_fee > (SELECT AVG(shipping_fee) FROM orders);

-- like operator
SELECT * FROM customers WHERE first_name LIKE 'An%';


-- between operator
SELECT * FROM orders WHERE shipping_fee BETWEEN 20 AND 50;

-- not between operator
SELECT * FROM orders WHERE shipping_fee NOT BETWEEN 20 AND 50;

-- in operator
SELECT * FROM orders WHERE ship_city IN ('Seattle', 'New York');

-- not in operator
SELECT * FROM orders WHERE ship_city NOT IN ('Seattle', 'New York');


-- is null
SELECT * FROM products WHERE minimum_reorder_quantity IS NULL;

-- is not null
SELECT * FROM products WHERE quantity_per_unit IS NOT NULL;


-- create view
CREATE VIEW viewName AS
SELECT first_name, city FROM customers;

-- select from view
SELECT * FROM viewName;



-- group by
SELECT city, COUNT(*)
FROM customers
GROUP BY city;

-- having clause (show city where city count >1)
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 1;


-- inner join
SELECT *
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;


-- left join
SELECT *
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id;


-- right join
SELECT *
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id;

-- join with selected columns
SELECT first_name,shipping_fee, payment_type
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;

-- join with alias
SELECT c.first_name, o.order_date
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;


-- multiple joins
SELECT c.first_name, o.id, p.product_name
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
INNER JOIN products p ON o.id = p.id;


SELECT 
    c.first_name,
    o.id AS order_id,
    p.product_name
FROM customers c
INNER JOIN orders o
        ON c.id = o.customer_id
INNER JOIN order_details od
        ON o.id = od.order_id
INNER JOIN products p
        ON od.product_id = p.id
ORDER BY c.first_name, o.id;
