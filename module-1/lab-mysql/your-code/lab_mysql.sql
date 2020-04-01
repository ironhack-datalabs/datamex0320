USE lab_mysql;

#doc de tipo .mysql

#crea database del lab_mysql
#create database lab_mysql;


#se crearán 4 tablas: cars, customer, salesperson, invoices con entidades dadas en read.me

#crea tabla “cars”
#con primary key a VIN:
create table cars ( VIN varchar(255) NOT NULL, Manufacterer varchar(255) NULL, Model varchar(255) NOT NULL, Year varchar(255)NULL, Color varchar(255)NULL, PRIMARY KEY(VIN));

#verificar que se creó la tabla: show tables;


#tabla customer
create table Customers(CustomerID int, Name varchar(255),PhoneNumber varchar(255), email varchar(25), Address varchar(255), City varchar(255), State_Province varchar(255), country varchar(25), zipPostal varchar(25), primary key(CustomerID));


#crear tabla de salespersons

create table Salespersons ( StaffID varchar(255), Name varchar(255), Store varchar(255), primary key(StaffID));




create table Invoices (Invoice_Number int, Date varchar(225),  Car varchar(255), Customer varchar(255),Salesperson varchar(255));


#En mysql 8.0.19 localhost/lab_mysql/cars
‘’’INSERT INTO cars(manufacture, model)
	VALUES(Volkswagen, Peugeot, Ford), (Tiguan, Rifter, Fusion);
#O uno por uno: 
	values(volkswagen);
	Values(Peugeot);

SELECT * FROM lab_mysql.cars;
‘’’


