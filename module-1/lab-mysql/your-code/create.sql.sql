USE lab_mysql;

CREATE TABLE cars (
vin VARCHAR(100), 
manufacterer TINYTEXT, 
model TINYTEXT, 
year YEAR, 
color TINYTEXT, 
price TINYINT(250));

CREATE TABLE Customer (
customer_id VARCHAR(100) primary key, 
customer_name TINYTEXT, 
phone TINYTEXT, 
email VARCHAR(100), 
address TINYTEXT, 
city TINYTEXT,
state TINYTEXT,
country TINYTEXT,
zip TINYTEXT);

CREATE TABLE sales_persons (
staff_id VARCHAR(100) primary key, 
staff_name TINYTEXT, 
store_name TINYTEXT
);

CREATE TABLE invoices (
invoice_number VARCHAR(100) primary key, 
date DATE, 
vin VARCHAR(100),
customer_name TINYTEXT,
staff_name TINYTEXT, 
store_name TINYTEXT
);

CREATE TABLE stores (
store_id VARCHAR(100) primary key, 
store_name TINYTEXT, 
store_address TINYTEXT,
store_city TINYTEXT,
store_state TINYTEXT, 
store_zip TINYTEXT
);


