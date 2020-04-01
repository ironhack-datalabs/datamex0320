# Create and use the lab_mysql database
CREATE DATABASE lab_mysql;
USE lab_mysql; 

# Create tables
CREATE TABLE cars
    (car_id INT(20),
    manufacturer VARCHAR(100),
    model VARCHAR(20),
    year VARCHAR(20),
    color TEXT(20),
    price DECIMAL(12,2),
    CONSTRAINT cars_pk PRIMARY KEY (car_id)
    );

CREATE TABLE customers 
    (customer_id INT(20), 
    name TEXT(100), 
    phone VARCHAR(25), 
    email VARCHAR(100), 
    addres VARCHAR(200), 
    city VARCHAR(100), 
    state TEXT(50), 
    country TEXT(50), 
    postal_code INT(20), 
    age INT(3), 
    CONSTRAINT customer_pk PRIMARY KEY (customer_id) 
    );

CREATE TABLE salespersons
    (staff_id INT(20),
    name TEXT(100),
    store VARCHAR(50),
    age INT(3),
    CONSTRAINT salespersons_pk PRIMARY KEY (staff_id)
    );

CREATE TABLE invoices
    (invoice_number INT(20),
    date_in DATE,
    car INT(20),
    customer INT(20),
    staff INT(20),
    CONSTRAINT invoice_number_pk PRIMARY KEY (invoice_number),
    CONSTRAINT car_fk FOREIGN KEY (car) REFERENCES cars(car_id),
    CONSTRAINT customer_fk FOREIGN KEY (customer) REFERENCES customers(customer_id),
    CONSTRAINT staff_fk FOREIGN KEY (staff) REFERENCES salespersons(staff_id)
    );