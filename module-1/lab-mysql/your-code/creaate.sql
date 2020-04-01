USE lab_mysql;

create table cars ( VIN varchar(25) NOT NULL, Manufacterer varchar(25) NULL, Model varchar(25) NOT NULL, Year varchar(25)NULL, Color varchar(25)NULL, PRIMARY KEY(VIN));

create table Customers(CustomerID int, Name varchar(25),PhoneNumber varchar(25), email varchar(25), Address varchar(25), City varchar(25), State_Province varchar(25), country varchar(25), zipPostal varchar(25), primary key(CustomerID));

create table Salespersons ( StaffID varchar(25), Name varchar(25), Store varchar(25), primary key(StaffID));

create table Invoices (Invoice_Number int, Date varchar(25),  Car varchar(25), Customer varchar(25),Salesperson varchar(25), primary key(Invoice_Number));



