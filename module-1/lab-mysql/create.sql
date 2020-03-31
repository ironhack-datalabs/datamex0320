create database Automobile;

create table customers (id varchar(10) NOT NULL, first_name varchar (30) NOT NULL, last_name varchar (30)NOT NULL,  primary key(id))

create table invoices 
(
invoice_number varchar (20), date_ varchar (15), customer_id varchar(20), amount varchar (20), 
primary key (invoice_number), foreign key (customer_id) references customers(id)
);   	

create table salesperson
(
id varchar (20), first_name varchar (15), last_name varchar(20),  
primary key (id)
);   

create table cars
( VIN varchar (20), make varchar (20), model varchar(20), year_ tinyint(4), primary key (VIN));

create table cars
( VIN varchar (20), make varchar (20), model varchar(20), year_ int(4), primary key (VIN));
