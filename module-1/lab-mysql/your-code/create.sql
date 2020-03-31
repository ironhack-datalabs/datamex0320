#Crear database:
create database lab_mysql;

#Crear tabla "cars"
create table cars (vehicleid INT(20), manufacturer VARCHAR(20), model VARCHAR(20), years INT(4), color VARCHAR(20) );

#Verificar que se creó la tabla con las columnas que especifiqué
SELECT *
FROM lab_mysql.cars;

#Crear tabla de Customer
CREATE TABLE customer(cutomerID int(12), cutomername VARCHAR(30), phone CHAR(12), email char(20), address varchar(40), city varchar(20), state varchar(20), country varchar(20), zipcode char(5));

#Crear tabla de sales person
CREATE TABLE salesperson(tsalesID int(2),staffID int(12), staffname VARCHAR(30), store VARCHAR(12));

#Crear tabla de invoices
CREATE TABLE invoices(tinvoicesID int(2),invoicenumber int(12), idates date, car int(2), customer int(2), salesperson int(2));